import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]
NOTE_FILENAMES = (
    "deepface_robot_control.md",
    "pi05_aloha_finetune.md",
    "openpi_aloha_inference_deployment.md",
    "zsibot_emg_robot_control.md",
    "amorfati-ai-infra-readme.md",
)


class ProfileContentTests(unittest.TestCase):
    def test_readmes_link_to_public_notes_repository(self):
        old_prefix = "https://github.com/Danielz-z/ai-engineering-notes/blob/main/"
        public_prefix = (
            "https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/"
        )

        for readme_name in ("README.md", "README.zh-CN.md"):
            content = (ROOT / readme_name).read_text(encoding="utf-8")
            with self.subTest(readme=readme_name):
                self.assertNotIn(old_prefix, content)
                for filename in NOTE_FILENAMES:
                    self.assertIn(f"{public_prefix}{filename}", content)


if __name__ == "__main__":
    unittest.main()
