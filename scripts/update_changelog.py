import difflib
import tomllib
import sys

from pathlib import Path
from datetime import datetime


project_file = Path("pyproject.toml")
with open(project_file, "rb") as file:
    pyproject = tomllib.load(file)


CHANGELOG = Path("CHANGELOG.md")


# Replace Unreleased with current version number
def main():
    current_version = pyproject.get("project", {}).get("version")
    if not current_version:
        sys.exit("No version found in pyproject.toml")

    with CHANGELOG.open() as file:
        content = file.read()

    old_content = content

    content = content.replace(
        "## [Unreleased]",
        f"## [{current_version}] - {datetime.now().strftime('%Y-%m-%d')}",
    )

    # print diff
    diff = difflib.unified_diff(
        old_content.splitlines(), content.splitlines(), lineterm=""
    )

    with CHANGELOG.open("w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
