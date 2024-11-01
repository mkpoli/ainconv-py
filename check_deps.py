"""
Check for dev dependencies in production code.
"""

import tomllib
from pathlib import Path
import sys

from modulefinder import ModuleFinder
import importlib.metadata

module_2_package = importlib.metadata.packages_distributions()

project_file = Path("pyproject.toml")
with open(project_file, "rb") as file:
    pyproject = tomllib.load(file)

# Extract dev-dependencies
dev_deps = (
    pyproject.get("tool", {})
    .get("uv", {})
    .get("dev-dependencies", [])
)
print(f"Dev dependencies: {dev_deps}")


# List of directories to check for imports
directories_to_check = ["src"]


def check_for_dev_deps_in_code(dev_deps, directories):
    finder = ModuleFinder()

    for directory in directories:
        for path in Path(directory).rglob("*.py"):
            print(f"Checking {path} ...")

            with path.open() as file:
                finder.run_script(str(path))
                for name, _ in finder.modules.items():
                    package = module_2_package.get(name, [])

                    if any(dep in package for dep in dev_deps):
                        print(f"❌ Dev dependency found in production code: {name}")
                        return True
    else:
        print("✅ No dev dependencies found in production code.")

    return False


if check_for_dev_deps_in_code(dev_deps, directories_to_check):
    sys.exit("Build failed due to dev dependency usage in production code.")
