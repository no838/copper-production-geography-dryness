# Sanitization Report

- package_root: `github_release/copper_production_geography_public_release_20260526`
- scan_date: `2026-05-26`
- scan_scope: `all text files under the public release folder`

## Checked patterns

- local filesystem paths such as `/Users/`
- personal email strings
- token / password / secret markers
- AI / assistant provenance words
- manuscript submission artifacts such as `cover letter`, `submission form`, `declaration`
- funding number strings

## Result

No credential strings, no local filesystem paths, no personal email addresses, and no funding identifiers were detected in the release package.

Two keyword hits were found in `README.md`, but both were exclusion statements rather than leaked artifacts:

- `cover letters and declarations`
- `manuscript DOCX, cover letters, declarations, or submission forms`

These lines describe what is **not** included in the public release and were retained intentionally.

## Release boundary

Included:

- derived figure-ready CSV files
- public-safe plotting code
- README and provenance notes

Excluded:

- raw climate files
- raw mine-point data
- manuscript submission files
- local caches and logs
- credentials and secrets
