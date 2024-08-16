# Dynamic Versioning for Python Projects with PDM

Ilcome to the `dynamic-versioning-python-pdm` repository! This project demonstrates how to automate versioning in Python projects using PDM, Git, and GitHub Actions. By leveraging these tools, I aim to streamline the release process, ensuring consistent and automatic version management with minimal manual intervention.

## Features

- **Automated Version Bumping**: Automatically increment the version number using Git tags or Git hooks.
- **PDM Integration**: Use PDM for dependency management, packaging, and publishing to PyPI.
- **CI/CD Pipeline**: GitHub Actions workflow included for building, versioning, and releasing package automatically.
- **Pre-commit Hooks**: Ensures that versioning is handled on every commit, keeping project up to date.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.6+](https://www.python.org/downloads/)
- [PDM](https://pdm.fming.dev/latest/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/heliyahasani/dynamic-versioning-python.git
   cd dynamic-versioning-python
   ```

2. Install dependencies using PDM:

   ```bash
   pdm install
   ```

### Usage

- **Automatically Bump Version with Git Tags**:

  Tag releases to automatically manage versions:

  ```bash
  git tag v0.1.1
  git push origin v0.1.1
  ```

- **GitHub Actions CI/CD**:

  This repository includes a GitHub Actions workflow that automates the release process. The workflow is triggered by tagging a new version:

  ```bash
  git tag v0.1.1
  git push origin v0.1.1
  ```

  The workflow will:

  - Bump the version in `pyproject.toml`
  - Build the package using PDM
  - Publish the package to PyPI

### GitHub Actions Workflow Example

Here’s an example of a GitHub Actions workflow you can include in repository to automate the release process:

```yaml
name: Release

on:
  push:
    tags:
      - "v*.*.*"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.x"

      - name: Install PDM
        run: python -m pip install pdm

      - name: Install dependencies
        run: pdm install

      - name: Bump version
        run: |
          pdm bump --patch
          git add pyproject.toml
          git commit -m "Bump version"
          git push origin main

      - name: Build package
        run: pdm build

      - name: Publish to PyPI
        env:
          PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}
        run: pdm publish --token $PYPI_TOKEN
```
