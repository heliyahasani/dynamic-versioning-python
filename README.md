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

- [Python 3.8+](https://www.python.org/downloads/)
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
