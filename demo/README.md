# Dynamic Versioning for Python Projects with PDM

Assuming you are in different repo and want to use your package.
When calling this package the structure should look like the demo folder.
First check pyproject.toml to see how you should add the package.

```bash

pdm install

```

Afterwards you can try to use it.

```bash

from trial import basic_calculator

print(basic_calculator.sum(2, 3))

```
