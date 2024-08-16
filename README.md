# Dynamic Versioning for Python Projects with PDM

Ilcome to the `dynamic-versioning-python-pdm` repository! This project demonstrates how to automate versioning in Python projects using PDM, Git, and GitHub Actions. By leveraging these tools, I aim to streamline the release process, ensuring consistent and automatic version management with minimal manual intervention.

## Features

- **Automated Version Bumping**: Automatically increment the version number using Git tags or Git hooks.
- **PDM Integration**: Use PDM for dependency management, packaging, and publishing to PyPI.

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

3. Insttal bump2version with pdm

```bash
  pdm add --dev bump2version
```

### Usage

1. Create .bumpversion.cfg file to include the following configuration:

```bash
[bumpversion]
current_version = 0.1.0 #Initially it should match with your pyproject.toml version
commit = True
tag = True

[bumpversion:file:pyproject.toml]
search = version = "{current_version}"
replace = version = "{new_version}"
```

2. Add your changes and commit to the repository.
3. Before pushing it you can now use bump2version to automatically bump the version in your pyproject.toml. Depending on what you want to increment, you can specify:

```bash
pdm run bump2version patch #Increment the last number (e.g., 0.1.0 to 0.1.1)
```

```bash
pdm run bump2version minor #Increment the middle number (e.g., 0.1.0 to 0.2.0)
```

```bash
pdm run bump2version major #Increment the first number (e.g., 0.1.0 to 1.0.0)

```

4. Push your code to the desire branch
