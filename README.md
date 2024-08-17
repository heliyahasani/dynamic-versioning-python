# Dynamic Versioning Python

[![Python CI/CD](https://github.com/heliyahasani/dynamic-versioning-python/actions/workflows/ci.yml/badge.svg)](https://github.com/heliyahasani/dynamic-versioning-python/actions/workflows/ci.yml)

## Overview

This project implements dynamic versioning for a Python package using `bump2version` and `pdm`. The versioning is automatically handled based on commit messages and is integrated with a CI/CD pipeline using GitHub Actions.

## Features

- **Automatic Version Bumping**: The version number is automatically updated based on commit messages indicating major, minor, or patch changes.
- **CI/CD Integration**: GitHub Actions is used to automate testing, versioning, and deployment.
- **Customizable**: The project can be easily customized to suit specific versioning and deployment requirements.

## Getting Started

### Prerequisites

- Python 3.8 or later
- `pdm` (Python Development Master) - a modern Python package and dependency manager
- `bump2version` - for versioning control

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/heliyahasani/dynamic-versioning-python.git
   cd dynamic-versioning-python
   ```

2. **Install Dependencies**:
   ```bash
   pdm install
   ```
3. **Running Tests**:

```bash
pdm run python -m unittest discover tests

```

4. **Version Bumping**:
   The version bumping is handled automatically in the CI/CD pipeline based on the commit message. Use the following keywords in your commit message to trigger version changes:

- [major] - Bumps the major version (e.g., 1.0.0 → 2.0.0)
- [minor] - Bumps the minor version (e.g., 1.0.0 → 1.1.0)
- [patch] - Bumps the patch version (e.g., 1.0.0 → 1.0.1)

5. **CI/CD Pipeline**:
   This project uses GitHub Actions for the CI/CD pipeline. The workflow is defined in .github/workflows/ci-cd.yml. The pipeline performs the following steps:

1. Check out the Code: Fetches the latest code from the repository.
1. Set Up Python: Configures the Python environment.
1. Install Dependencies: Installs project dependencies using pdm.
1. Version Bumping: Automatically bumps the version if the commit message contains [major], [minor], or [patch].
1. Run Tests: Executes the unit tests.
   6.Deploy to VM: If configured, the code is automatically deployed to a specified VM.
1. Deployment
1. The deployment is managed via SSH to a specified VM. The workflow automatically clones the repository or pulls the latest changes if it has already been cloned.

9.To configure the deployment, ensure the following GitHub Secrets are set:

- SSH_USER: The SSH username for the VM.
- VM_IP: The IP address of the VM.
- VM_PASSWORD: The SSH password for the VM.
