import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class WorkflowConfigurationTests(unittest.TestCase):
    def test_translation_rules_define_style_and_required_terms(self):
        rules = (ROOT / ".github" / "profile-translation-rules.md").read_text()

        self.assertIn("自然、专业、简洁", rules)
        self.assertIn("不添加英文源稿中不存在的事实", rules)
        for preferred_translation in (
            "robotics integration：机器人系统集成",
            "safety-gated action：通过安全门控执行动作",
            "late fusion：后期融合",
            "Accepted for Oral Presentation：获口头报告录用",
        ):
            self.assertIn(preferred_translation, rules)
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
            "cancel-in-progress: true",
            "DEEPSEEK_MODEL: deepseek-v4-flash",
            "DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}",
            "python3 .github/scripts/sync_profile_readme.py",
            "git rev-parse HEAD:README.md",
            "git rev-parse origin/main:README.md",
            "git rev-parse HEAD:README.zh-CN.md",
            "git rev-parse origin/main:README.zh-CN.md",
            '"$LOCAL_SOURCE_BLOB" != "$REMOTE_SOURCE_BLOB"',
            '"$LOCAL_TARGET_BLOB" != "$REMOTE_TARGET_BLOB"',
            "createCommitOnBranch",
            "expectedHeadOid",
            "gh api graphql",
            "chore(profile): sync Chinese README",
        )
        for fragment in expected_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, workflow)
        self.assertNotIn('"$REMOTE_SHA" != "$GITHUB_SHA"', workflow)
        self.assertNotIn("gh api --method PUT", workflow)
        self.assertNotIn("models: read", workflow)
        self.assertNotIn("GITHUB_MODELS", workflow)


if __name__ == "__main__":
    unittest.main()
