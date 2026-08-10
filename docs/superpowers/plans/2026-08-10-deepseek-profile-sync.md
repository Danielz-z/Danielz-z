# DeepSeek Profile README Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the retired GitHub Models dependency with DeepSeek V4 Flash while preserving the existing two-pass translation, validation, and atomic publication behavior.

**Architecture:** Keep the current standard-library chat-completions client shape and swap its endpoint, credentials, model configuration, and provider-specific errors. The GitHub Actions job will read a repository secret named `DEEPSEEK_API_KEY`; the built-in `GITHUB_TOKEN` remains limited to publishing the validated README.

**Tech Stack:** Python 3 standard library, `unittest`, GitHub Actions, DeepSeek OpenAI-compatible Chat Completions API.

## Global Constraints

- Use `https://api.deepseek.com/chat/completions`.
- Use `deepseek-v4-flash` with `thinking.type` set to `disabled`.
- Read the API credential only from `DEEPSEEK_API_KEY`; never commit it or print it.
- Preserve the two-pass translation/review flow, strict validation, atomic local write, and stale-run-safe GitHub publication.
- Remove the retired GitHub Models permission and configuration.

---

### Task 1: Migrate README generation to DeepSeek

**Files:**
- Modify: `tests/test_sync_profile_readme.py`
- Modify: `tests/test_workflow_configuration.py`
- Modify: `.github/scripts/sync_profile_readme.py`
- Modify: `.github/workflows/sync-profile-zh.yml`

**Interfaces:**
- Consumes: DeepSeek `POST /chat/completions` with bearer authentication.
- Produces: `DeepSeekClient.complete(system_prompt: str, user_prompt: str) -> str` and workflow variables `DEEPSEEK_API_KEY` / `DEEPSEEK_MODEL`.

- [x] **Step 1: Write failing provider-client tests**

Update the client tests to instantiate `DeepSeekClient`, require the DeepSeek endpoint, `deepseek-v4-flash`, `temperature: 0.2`, and `thinking: {"type": "disabled"}`. Update the CLI test to provide `DEEPSEEK_API_KEY` and expect the new default model. Update the workflow test to require the DeepSeek secret/model and reject GitHub Models configuration.

- [x] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_sync_profile_readme tests.test_workflow_configuration -v`

Expected: failures because `DeepSeekClient`, DeepSeek environment variables, and workflow configuration do not yet exist.

- [x] **Step 3: Implement the minimal migration**

Rename the client to `DeepSeekClient`, send requests to the DeepSeek endpoint with JSON content type and bearer authorization, add `thinking: {"type": "disabled"}`, and use DeepSeek-specific safe error messages. In `main`, require `DEEPSEEK_API_KEY` and default `DEEPSEEK_MODEL` to `deepseek-v4-flash`. In the workflow, remove `models: read`, expose the new model, and pass only `secrets.DEEPSEEK_API_KEY` to the generation step.

- [x] **Step 4: Run focused and full verification**

Run: `python3 -m unittest tests.test_sync_profile_readme tests.test_workflow_configuration -v`

Run: `python3 -m unittest discover -s tests -v`

Run: `python3 -m py_compile .github/scripts/sync_profile_readme.py tests/test_sync_profile_readme.py tests/test_workflow_configuration.py`

Expected: all 15 tests pass and Python compilation succeeds.

- [x] **Step 5: Review and commit**

Inspect the diff for credential exposure and unintended changes, then commit with `fix: migrate profile sync to DeepSeek`.
