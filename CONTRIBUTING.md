# Contributing

Thanks for your interest in contributing! Please follow these guidelines.

## How to contribute
1. Fork the repository.
2. Clone your fork and set up remotes.
3. Create a feature branch: `git checkout -b feat/your-feature`.
4. Implement your changes and add tests.
5. Run linters and the full test suite locally.
6. Push your branch and submit a pull request with a clear description and references to related issues, if any.

## Code style
- Python: follow PEP 8; use `black` for formatting.
- JavaScript: use a consistent linter (ESLint recommended).

## Tests
- Add unit tests for new operations.
- Include tests for edge cases (singular matrices, non-square matrices, large sizes).

## Reporting issues
- Open an issue describing the problem and include:
  - a small reproducible example,
  - expected vs. actual behavior,
  - environment details (OS, versions).