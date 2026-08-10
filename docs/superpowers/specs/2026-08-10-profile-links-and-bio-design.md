# Profile Links and Bio Design

## Goal

Fix the five public-facing notes links in both profile README languages and replace the GitHub Bio with concise, natural English.

## Scope

- In `README.md` and `README.zh-CN.md`, change only the repository segment of the five notes URLs from `Danielz-z/ai-engineering-notes` to `Danielz-z/ai-engineering-notes-public`.
- Keep each filename, link label, surrounding prose, Markdown structure, and all unrelated content unchanged.
- Update the GitHub account Bio to exactly `CS student at BJTU | Incoming M.S. student in AI at UCLA`.
- Do not modify the GitHub status, pinned repositories, security settings, or any other profile text.

## Verification

- Add a regression test that scans both README files, rejects the old repository URL, and requires all five expected public notes URLs.
- Observe that the regression test fails before the README edit and passes after it.
- Run the full repository test suite and existing bilingual structure validator.
- Verify each corrected URL returns HTTP 200 without GitHub authentication.
- Read the GitHub profile back through the API and confirm the Bio matches exactly.

## Publication

- Commit only the two README files, the focused regression test, and this design/plan documentation.
- Push the verified commit to `main` using the previously approved direct-main workflow.
- Verify local and remote `main` resolve to the same commit.
