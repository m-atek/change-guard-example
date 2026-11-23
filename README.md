# change-guard example

A demonstration repository: an invented shop module, `src/pricing.py`, with a few tests. Demo project, no real data.

It shows [change-guard](https://github.com/m-atek/change-guard), a fail-to-pass check. A fail-to-pass check runs the tests a pull request brings against the code before the change: they must fail there and pass on the change.

Each open pull request adds the same bulk discount:

| Pull request | What it brings | Result |
|---|---|---|
| No test | The discount only | STOPPED (no-test), red |
| Test passes without the change | A test that never reaches the discount | STOPPED (test-passes-on-base), red |
| Test checks the change | A test that checks the discount | PASSED (ok), green |
| Recorded skip | The first change, with the skip label and a reason line | SKIPPED, green |

The check `change-guard` is required on `main`, so the two red pull requests cannot be merged.

A new installation starts in report mode: the check stays green and says what blocking mode would do. This repository is switched to blocking mode on purpose (repository variable `CHANGE_GUARD_MODE` set to `block`).

The pull requests stay open and are never merged.
