from setuptools import setup, find_packages

setup(
    name="dynamic_versioning_python",
    version="0.1.0",
    author="Heliya Hasani",
    author_email="heliyahasani@hotmail.com",
    description="Automate versioning in Python projects using PDM",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/heliyahasani/dynamic-versioning-python.git",
    packages=find_packages(),
    python_requires=">=3.8",
)


# pdm build
