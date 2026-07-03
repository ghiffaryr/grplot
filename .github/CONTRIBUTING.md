# Contributing to grplot

Thank you for your interest in contributing to grplot! Everyone is expected to abide by our [Code of Conduct](../CODE_OF_CONDUCT.md). grplot is licensed under the [BSD 3-Clause License](../LICENSE).

## How to Report Issues

Before opening a new issue, please search the [issue tracker](https://github.com/ghiffaryr/grplot/issues) to see if the problem has already been reported.

When reporting a bug, include:

- Your Python version, grplot version, and operating system
- A minimal reproducible example using built-in or synthetic data
- The full output or error message

Use the appropriate label when creating an issue: `bug` for bugs, `enhancement` for feature requests, `question` for support.

## How to Contribute Code

1. Fork the repository and clone your fork.
2. Work on the `dev` branch:
   ```
   git checkout dev
   git pull origin dev
   ```
3. Set up a development environment:
   ```
   make install-dev
   ```
4. Run tests to make sure everything passes:
   ```
   make test
   ```
5. Lint and format your code:
   ```
   make lint
   make format
   ```
6. Open a pull request against the `dev` branch with a clear description of your changes and a reference to any related issue.

### Pull Request Checklist

- Tests pass and new code is covered by tests
- Linting passes (`make lint`)
- The PR description links to the related issue
- Changes are limited to the scope described in the PR

## Questions and Support

For questions, open a GitHub issue with the `question` label.

## Use of Generative AI

Generative AI tools may be used as supportive aids for understanding code or drafting text. You are responsible for all content you contribute. Pull requests that appear to be generated without genuine understanding or engagement may be closed.
