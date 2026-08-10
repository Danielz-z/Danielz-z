# Profile Links and Bio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every public notes link on the bilingual GitHub profile resolve successfully and update the account Bio to the approved English wording.

**Architecture:** Treat README link correctness as repository behavior protected by a focused unit test, then update only the URL repository segment in both language files. Treat the GitHub Bio as separate account metadata, update it through the authenticated GitHub API, and read it back for exact verification.

**Tech Stack:** Markdown, Python 3 `unittest`, Git, GitHub REST API through `gh`.

## Global Constraints

- The Bio must be exactly `CS student at BJTU | Incoming M.S. student in AI at UCLA`.
- Replace only `Danielz-z/ai-engineering-notes` with `Danielz-z/ai-engineering-notes-public` in the five notes URLs in each README.
- Preserve filenames, labels, surrounding prose, Markdown structure, and all unrelated profile content.
- Do not modify GitHub status, pinned repositories, security settings, or other account metadata.
- Publish through the previously approved direct-`main` workflow.

---

### Task 1: Protect and repair public notes links

**Files:**
- Create: `tests/test_profile_content.py`
- Modify: `README.md:64-79`
- Modify: `README.zh-CN.md:64-79`

**Interfaces:**
- Consumes: the five public note filenames in both README files.
- Produces: ten links under `https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/` and a regression test rejecting the former repository URL.

- [ ] **Step 1: Write the failing regression test**

Create `tests/test_profile_content.py` with:

```python
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
```

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python3 -m unittest tests.test_profile_content -v`

Expected: FAIL because both README files still contain `https://github.com/Danielz-z/ai-engineering-notes/blob/main/`.

- [ ] **Step 3: Apply the minimal URL replacement**

In `README.md` and `README.zh-CN.md`, replace each occurrence of:

```text
https://github.com/Danielz-z/ai-engineering-notes/blob/main/
```

with:

```text
https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/
```

No surrounding text changes are permitted.

- [ ] **Step 4: Verify GREEN and existing invariants**

Run: `python3 -m unittest tests.test_profile_content -v`

Expected: PASS.

Run: `python3 -m unittest discover -s tests -v`

Expected: all tests pass.

Run the existing `validate_translation` function against `README.md`, `README.zh-CN.md`, and `.github/profile-translation-rules.md`.

Expected: bilingual structure, assets, and protected terms remain valid.

- [ ] **Step 5: Verify public availability**

For each of the five corrected URLs, run unauthenticated `curl -L` and require HTTP 200.

Expected: all five URLs return HTTP 200.

### Task 2: Update and verify GitHub Bio

**Files:**
- No repository file changes.

**Interfaces:**
- Consumes: authenticated GitHub account `Danielz-z`.
- Produces: account Bio exactly equal to `CS student at BJTU | Incoming M.S. student in AI at UCLA`.

- [ ] **Step 1: Read the current Bio**

Run: `gh api user --jq .bio`

Expected: the previous BJTU/UCLA wording is returned.

- [ ] **Step 2: Update only the Bio field**

Run:

```bash
gh api --method PATCH user \
  -f 'bio=CS student at BJTU | Incoming M.S. student in AI at UCLA'
```

Expected: GitHub returns the updated account object.

- [ ] **Step 3: Read back exact account metadata**

Run: `gh api user --jq '{login, bio}'`

Expected:

```json
{"bio":"CS student at BJTU | Incoming M.S. student in AI at UCLA","login":"Danielz-z"}
```

### Task 3: Publish and verify repository changes

**Files:**
- Commit: `README.md`
- Commit: `README.zh-CN.md`
- Commit: `tests/test_profile_content.py`
- Commit: `docs/superpowers/plans/2026-08-10-profile-links-and-bio.md`

**Interfaces:**
- Consumes: verified local `main` changes.
- Produces: synchronized local and remote `main` commits.

- [ ] **Step 1: Review the exact diff**

Run: `git diff --check`, `git diff --stat`, and `git diff` for the four intended files.

Expected: no whitespace errors and no unrelated changes.

- [ ] **Step 2: Commit the intended files**

Run:

```bash
git add README.md README.zh-CN.md tests/test_profile_content.py \
  docs/superpowers/plans/2026-08-10-profile-links-and-bio.md
git commit -m "fix: repair profile links and bio"
```

Expected: one commit containing only the intended repository changes.

- [ ] **Step 3: Push and verify remote parity**

Run: `git push origin main`, then compare `git rev-parse HEAD` with `git ls-remote origin refs/heads/main`.

Expected: local and remote commit SHAs match exactly.
