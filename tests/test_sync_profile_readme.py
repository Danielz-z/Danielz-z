import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest
from urllib.error import HTTPError


SCRIPT_PATH = (
    pathlib.Path(__file__).parents[1]
    / ".github"
    / "scripts"
    / "sync_profile_readme.py"
)
SPEC = importlib.util.spec_from_file_location("sync_profile_readme", SCRIPT_PATH)
sync_profile_readme = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync_profile_readme)


SOURCE = """<h1 align="center">Hi, I'm Daniel</h1>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a></p>

## Current Work

EEG systems using OpenPI.

Human-aware systems.

### Capabilities

* EEG control — [notes](https://example.com/notes_(v1)_en)
"""

TRANSLATION = """<h1 align="center">你好，我是 Daniel</h1>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a></p>

## 目前的工作

使用 OpenPI 构建 EEG 系统。

构建以人为本的系统。

### 主要能力

* EEG 控制 — [笔记](https://example.com/notes_(v1)_en)
"""


class ValidateTranslationTests(unittest.TestCase):
    def test_accepts_natural_translation_with_matching_structure_and_assets(self):
        sync_profile_readme.validate_translation(
            SOURCE,
            TRANSLATION,
            protected_terms=("EEG", "OpenPI"),
        )

    def test_rejects_model_commentary_or_code_fences(self):
        for wrapped in (
            f"Here is the translated README:\n\n{TRANSLATION}",
            f"```markdown\n{TRANSLATION}```\n",
        ):
            with self.subTest(prefix=wrapped[:12]):
                with self.assertRaisesRegex(
                    sync_profile_readme.TranslationError,
                    "model commentary or code fences",
                ):
                    sync_profile_readme.validate_translation(
                        SOURCE,
                        wrapped,
                        protected_terms=("EEG", "OpenPI"),
                    )

    def test_rejects_reordered_markdown_or_changed_html_structure(self):
        moved_list = TRANSLATION.replace(
            "### 主要能力\n\n* EEG 控制",
            "* EEG 控制\n\n### 主要能力",
        )
        changed_html = TRANSLATION.replace("<p>", "<div>").replace("</p>", "</div>")
        changed_attribute = TRANSLATION.replace('align="center"', 'align="left"')
        changed_list_depth = TRANSLATION.replace("* EEG 控制", "  * EEG 控制")
        missing_paragraph = TRANSLATION.replace("\n构建以人为本的系统。\n", "\n")

        for invalid in (
            moved_list,
            changed_html,
            changed_attribute,
            changed_list_depth,
            missing_paragraph,
        ):
            with self.subTest(invalid=invalid[:80]):
                with self.assertRaisesRegex(
                    sync_profile_readme.TranslationError,
                    "document structure changed",
                ):
                    sync_profile_readme.validate_translation(
                        SOURCE,
                        invalid,
                        protected_terms=("EEG", "OpenPI"),
                    )

    def test_rejects_missing_assets_and_protected_terms(self):
        for invalid in (
            TRANSLATION.replace("https://example.com/notes", "https://example.com/other"),
            TRANSLATION.replace("[笔记]", "![笔记]"),
            TRANSLATION.replace("_en)", "_changed)"),
            TRANSLATION.replace("OpenPI", "开放式策略工具"),
        ):
            with self.subTest(invalid=invalid[-80:]):
                with self.assertRaises(sync_profile_readme.TranslationError):
                    sync_profile_readme.validate_translation(
                        SOURCE,
                        invalid,
                        protected_terms=("EEG", "OpenPI"),
                    )

    def test_rejects_fewer_occurrences_of_a_protected_term(self):
        one_eeg_removed = TRANSLATION.replace("EEG 系统", "脑电系统", 1)

        with self.assertRaisesRegex(
            sync_profile_readme.TranslationError,
            "Protected term counts changed",
        ):
            sync_profile_readme.validate_translation(
                SOURCE,
                one_eeg_removed,
                protected_terms=("EEG", "OpenPI"),
            )

    def test_rejects_output_that_is_still_predominantly_english(self):
        mostly_english = """<h1 align="center">Hi, I am Daniel 中</h1>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a></p>

## Current Work

OpenPI powers EEG systems.

Human-aware systems.

### Capabilities

* EEG control — [notes](https://example.com/notes_(v1)_en)
"""

        with self.assertRaisesRegex(
            sync_profile_readme.TranslationError,
            "does not contain enough Chinese text",
        ):
            sync_profile_readme.validate_translation(
                SOURCE,
                mostly_english,
                protected_terms=("EEG", "OpenPI"),
            )


class TranslationRulesTests(unittest.TestCase):
    def test_reads_backticked_protected_terms_from_rules(self):
        rules = """# Rules

## Protected terms

- `EEG`
- `OpenPI`
- Preserve natural Chinese.
"""

        self.assertEqual(
            sync_profile_readme.parse_protected_terms(rules),
            ("EEG", "OpenPI"),
        )


class _Response:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


class GitHubModelsClientTests(unittest.TestCase):
    def test_sends_low_temperature_chat_request_and_returns_content(self):
        captured = {}

        def opener(request, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return _Response(
                {"choices": [{"message": {"content": TRANSLATION}}]}
            )

        client = sync_profile_readme.GitHubModelsClient(
            token="test-token",
            model="openai/gpt-4o",
            opener=opener,
        )

        result = client.complete("system prompt", "user prompt")

        self.assertEqual(result, TRANSLATION)
        self.assertEqual(captured["timeout"], 60)
        body = json.loads(captured["request"].data)
        self.assertEqual(body["model"], "openai/gpt-4o")
        self.assertEqual(body["temperature"], 0.2)
        self.assertEqual(
            body["messages"],
            [
                {"role": "system", "content": "system prompt"},
                {"role": "user", "content": "user prompt"},
            ],
        )
        self.assertEqual(
            captured["request"].get_header("Authorization"),
            "Bearer test-token",
        )

    def test_reports_http_failures_without_exposing_response_body(self):
        def opener(request, timeout):
            raise HTTPError(
                request.full_url,
                429,
                "Too Many Requests",
                hdrs=None,
                fp=io.BytesIO(b'{"secret":"must not leak"}'),
            )

        client = sync_profile_readme.GitHubModelsClient(
            token="test-token",
            model="openai/gpt-4o",
            opener=opener,
        )

        with self.assertRaisesRegex(
            sync_profile_readme.TranslationError,
            "GitHub Models request failed with HTTP 429",
        ) as raised:
            client.complete("system", "user")

        self.assertNotIn("secret", str(raised.exception))


class _FakeClient:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def complete(self, system_prompt, user_prompt):
        self.calls.append((system_prompt, user_prompt))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


class SyncFilesTests(unittest.TestCase):
    def test_runs_translation_and_review_then_atomically_updates_target(self):
        rough_translation = TRANSLATION.replace("主要能力", "能力")
        client = _FakeClient([rough_translation, TRANSLATION])

        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source_path = root / "README.md"
            target_path = root / "README.zh-CN.md"
            rules_path = root / "rules.md"
            source_path.write_text(SOURCE)
            target_path.write_text("旧的中文版\n")
            rules_path.write_text("- `EEG`\n- `OpenPI`\n")

            changed = sync_profile_readme.sync_files(
                source_path,
                target_path,
                rules_path,
                client,
            )

            self.assertTrue(changed)
            self.assertEqual(target_path.read_text(), TRANSLATION)
            self.assertEqual(len(client.calls), 2)
            self.assertIn(SOURCE, client.calls[0][1])
            self.assertIn("旧的中文版", client.calls[0][1])
            self.assertIn(rough_translation, client.calls[1][1])
            self.assertFalse(target_path.with_suffix(".md.tmp").exists())

    def test_does_not_rewrite_an_unchanged_target(self):
        client = _FakeClient([TRANSLATION, TRANSLATION])
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source_path = root / "README.md"
            target_path = root / "README.zh-CN.md"
            rules_path = root / "rules.md"
            source_path.write_text(SOURCE)
            target_path.write_text(TRANSLATION)
            rules_path.write_text("- `EEG`\n- `OpenPI`\n")
            original_stat = target_path.stat()

            changed = sync_profile_readme.sync_files(
                source_path, target_path, rules_path, client
            )

            self.assertFalse(changed)
            self.assertEqual(target_path.read_text(), TRANSLATION)
            self.assertEqual(target_path.stat().st_mtime_ns, original_stat.st_mtime_ns)

    def test_model_failure_leaves_target_byte_identical(self):
        client = _FakeClient([sync_profile_readme.TranslationError("rate limited")])
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source_path = root / "README.md"
            target_path = root / "README.zh-CN.md"
            rules_path = root / "rules.md"
            source_path.write_text(SOURCE)
            original = "旧的中文版\n".encode()
            target_path.write_bytes(original)
            rules_path.write_text("- `EEG`\n- `OpenPI`\n")

            with self.assertRaisesRegex(
                sync_profile_readme.TranslationError, "rate limited"
            ):
                sync_profile_readme.sync_files(
                    source_path, target_path, rules_path, client
                )

            self.assertEqual(target_path.read_bytes(), original)
            self.assertFalse(target_path.with_suffix(".md.tmp").exists())


class CommandLineTests(unittest.TestCase):
    def test_main_uses_environment_token_and_current_default_model(self):
        captured = {}
        fake_client = _FakeClient([TRANSLATION, TRANSLATION])

        def client_factory(token, model):
            captured["token"] = token
            captured["model"] = model
            return fake_client

        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source_path = root / "README.md"
            target_path = root / "README.zh-CN.md"
            rules_path = root / "rules.md"
            source_path.write_text(SOURCE)
            target_path.write_text("旧的中文版\n")
            rules_path.write_text("- `EEG`\n- `OpenPI`\n")

            with contextlib.redirect_stdout(io.StringIO()):
                result = sync_profile_readme.main(
                    [
                        "--source",
                        str(source_path),
                        "--target",
                        str(target_path),
                        "--rules",
                        str(rules_path),
                    ],
                    environ={
                        "GITHUB_TOKEN": "workflow-token",
                    },
                    client_factory=client_factory,
                )

        self.assertEqual(result, 0)
        self.assertEqual(captured["token"], "workflow-token")
        self.assertEqual(captured["model"], "openai/gpt-4o")


if __name__ == "__main__":
    unittest.main()
