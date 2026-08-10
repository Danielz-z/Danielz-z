import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class WorkflowConfigurationTests(unittest.TestCase):
    def test_translation_rules_define_style_and_required_terms(self):
        rules = (ROOT / ".github" / "profile-translation-rules.md").read_text()

        self.assertIn("自然、专业、简洁", rules)
        self.assertIn("不添加英文源稿中不存在的事实", rules)
        for term in (
            "Daniel",
            "English",
            "简体中文",
            "EEG",
            "EMG",
            "OpenPI",
            "ALOHA",
            "Astribot",
            "ZsiBot",
            "STM32",
            "π0.5",
        ):
            self.assertIn(f"- `{term}`", rules)

    def test_workflow_has_narrow_triggers_permissions_and_stale_run_guard(self):
        workflow = (
            ROOT / ".github" / "workflows" / "sync-profile-zh.yml"
        ).read_text()

        expected_fragments = (
            "workflow_dispatch:",
            "branches: [main]",
            "paths: [README.md]",
            "contents: write",
            "models: read",
            "cancel-in-progress: true",
            "GITHUB_MODELS_MODEL: openai/gpt-4.1",
            "python3 .github/scripts/sync_profile_readme.py",
            "git rev-parse HEAD:README.md",
            "git rev-parse origin/main:README.md",
            "git rev-parse origin/main:README.zh-CN.md",
            '"$LOCAL_SOURCE_BLOB" != "$REMOTE_SOURCE_BLOB"',
            "gh api --method PUT",
            "chore(profile): sync Chinese README",
        )
        for fragment in expected_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, workflow)
        self.assertNotIn('"$REMOTE_SHA" != "$GITHUB_SHA"', workflow)


if __name__ == "__main__":
    unittest.main()
