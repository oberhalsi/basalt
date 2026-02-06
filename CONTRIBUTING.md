# Contributing to Basalt

First off, thank you for considering contributing to Basalt! It's people like you that make Basalt such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
  - [Git Commit Messages](#git-commit-messages)
  - [Code Style](#code-style)
- [Additional Notes](#additional-notes)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inclusive environment. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible using our bug report template.

**Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### How Do I Submit A Good Bug Report?

Bugs are tracked as [GitHub issues](https://github.com/oberhalsi/basalt/issues). Create an issue and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened.

Include details about your configuration and environment:

* **Which version of Basalt are you using?**
* **What's the name and version of the OS you're using?**
* **What's the version of Bash you're running?**

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/oberhalsi/basalt/issues). Before creating enhancement suggestions, please check the existing issues as you might find out that you don't need to create one.

#### How Do I Submit A Good Enhancement Suggestion?

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps** or provide code snippets.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** to most Basalt users.
* **List some other projects where this enhancement exists**, if applicable.

### Pull Requests

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the pull request template](.github/PULL_REQUEST_TEMPLATE.md)
2. Follow the [style guidelines](#style-guidelines)
3. After you submit your pull request, verify that all status checks are passing

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

#### Pull Request Process

1. **Fork the repository** and create your branch from `main`.
2. **Make your changes** and ensure they follow the style guidelines.
3. **Test your changes** thoroughly.
4. **Update documentation** if you're changing functionality.
5. **Write clear commit messages** following our commit message conventions.
6. **Push to your fork** and submit a pull request to the `main` branch.
7. **Wait for review** and address any feedback from maintainers.

## Development Setup

### Prerequisites

- Bash 4.0 or higher
- Git

### Setting Up Your Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/basalt.git
   cd basalt
   ```
3. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   or
   ```bash
   git checkout -b fix/issue-description
   ```

### Running Tests

Before submitting a pull request, make sure all tests pass:

```bash
# Run the test suite
./run-tests.sh
```

If there are no automated tests yet, please manually test your changes thoroughly.

## Style Guidelines

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
    * 🎨 `:art:` when improving the format/structure of the code
    * 🐛 `:bug:` when fixing a bug
    * ✨ `:sparkles:` when introducing new features
    * 📝 `:memo:` when writing docs
    * 🚀 `:rocket:` when improving performance
    * ✅ `:white_check_mark:` when adding tests
    * 🔒 `:lock:` when dealing with security
    * ⬆️ `:arrow_up:` when upgrading dependencies
    * ⬇️ `:arrow_down:` when downgrading dependencies
    * 🔧 `:wrench:` when changing configuration files

Example:
```
✨ Add support for custom configurations

- Implement config file parsing
- Add validation for user-provided configs
- Update documentation with examples

Fixes #123
```

### Code Style

* Use 4 spaces for indentation (not tabs)
* Use meaningful variable and function names
* Add comments for complex logic
* Follow existing code patterns in the repository
* Use `shellcheck` to lint your Bash code
* Keep functions small and focused on a single task
* Use proper error handling with appropriate exit codes

#### Bash-Specific Guidelines

* Always quote variables: `"$variable"` instead of `$variable`
* Use `[[` instead of `[` for conditionals
* Prefer `$(command)` over backticks
* Use `readonly` for constants
* Use `local` for function variables
* Include a shebang: `#!/usr/bin/env bash`
* Use `set -euo pipefail` for safer scripts

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

* `bug` - Issues for bugs in the code
* `enhancement` - Issues for new features or improvements
* `documentation` - Issues related to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed
* `question` - Further information is requested
* `wontfix` - This will not be worked on
* `duplicate` - This issue or pull request already exists

### Getting Help

If you need help, you can:

* Open an issue with the `question` label
* Reach out to maintainers
* Check existing documentation and issues

## Recognition

Contributors will be recognized in our README.md file. We appreciate every contribution, no matter how small!

---

Thank you for contributing to Basalt! 🎉
