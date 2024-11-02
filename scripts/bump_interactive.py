import inquirer
from bumpversion.files import resolve_file_config
from bumpversion.config import get_configuration
from bumpversion.bump import get_next_version
from bumpversion.versioning.models import Version
from bumpversion.config import get_configuration
from bumpversion.config.files import find_config_file
from bumpversion.context import get_context
from bumpversion.files import modify_files
from bumpversion.visualize import visualize
from bumpversion.hooks import (
    run_pre_commit_hooks,
    run_post_commit_hooks,
    run_setup_hooks,
)
from bumpversion.config.files import update_config_file
from bumpversion.config.files_legacy import update_ini_config_file
from bumpversion.context import get_context
from bumpversion.bump import commit_and_tag
from bumpversion.files import modify_files, resolve_file_config

import toml
from colorama import Fore


def encode_version(version: Version, config) -> str:
    return config.version_config.serialize(version, get_context(config))


# bump = "uv run bump-my-version bump"
def main():
    # region CLI bump-my-version bump
    found_config_file = find_config_file()
    if not found_config_file:
        print("No bump-my-version config file found.")
        return

    config = get_configuration(found_config_file)

    current_version_str = config.current_version
    if not current_version_str:
        print("No version found.")
        return

    version = config.version_config.parse(current_version_str)
    if not version:
        print("Invalid version.")
        return

    package_version = toml.load("pyproject.toml")["project"]["version"]
    if not package_version or package_version != config.current_version:
        print("`pyproject.toml` version does not match current version.")
        return
    # endregion

    # region CLI bump-my-version show-bump
    visualize(config=config, version_str=current_version_str, box_style="light")
    # endregion

    print()

    # region Custom CLI
    new_versions: dict[str, str] = {
        "major": encode_version(
            get_next_version(version, config, "major", None), config
        ),
        "minor": encode_version(
            get_next_version(version, config, "minor", None), config
        ),
        "patch": encode_version(
            get_next_version(version, config, "patch", None), config
        ),
    }

    version_choices = {
        **{
            f"{bump_type} (v{version})": bump_type
            for bump_type, version in new_versions.items()
        },
        "custom": "custom",
    }

    choiced = inquirer.list_input(
        message="What version to bump to?",
        choices=list(version_choices.keys()),
        carousel=True,
    )
    if not choiced or choiced not in version_choices.keys():
        print("Invalid version bump type.")
        return

    bump_type = version_choices[choiced]
    if bump_type == "custom":
        new_version_str = inquirer.text(message="Enter the new version")
    else:
        new_version_str = new_versions[bump_type]

    confirm = inquirer.confirm(
        message=f"Confirm to bump to {Fore.BLUE}v{new_version_str}{Fore.RESET} ({bump_type})?"
    )

    if not confirm:
        print("Bump cancelled.")
        return

    new_version = get_next_version(version, config, bump_type, new_version_str)
    print(
        f"Bumping from {Fore.YELLOW}v{current_version_str}{Fore.RESET} to {Fore.BLUE}v{new_version_str}{Fore.RESET}..."
    )

    if version == new_version:
        print(f"Version is already {Fore.BLUE}v{new_version_str}{Fore.RESET}.")
        return
    # endregion

    # region Start bump (do_bump())

    dry_run = False

    run_setup_hooks(config, version, dry_run)

    ctx = get_context(config, version, new_version)

    configured_files = resolve_file_config(
        config.files_to_modify, config.version_config
    )

    if bump_type:
        # filter the files that are not valid for this bump
        configured_files = [
            file
            for file in configured_files
            if bump_type in file.file_change.include_bumps  # type: ignore
        ]
        configured_files = [
            file
            for file in configured_files
            if bump_type not in file.file_change.exclude_bumps
        ]

    modify_files(configured_files, version, new_version, ctx, dry_run)
    if found_config_file and found_config_file.suffix in {".cfg", ".ini"}:
        update_ini_config_file(
            found_config_file, current_version_str, new_version_str, dry_run
        )  # pragma: no-coverage
    else:
        update_config_file(
            found_config_file, config, version, new_version, ctx, dry_run
        )

    ctx = get_context(config, version, new_version)
    ctx["new_version"] = new_version_str

    run_pre_commit_hooks(config, version, new_version, dry_run)

    commit_and_tag(config, found_config_file, configured_files, ctx, dry_run)

    run_post_commit_hooks(config, version, new_version, dry_run)

    print()

    print("Successfully bumped version to v{new_version_str}.")


if __name__ == "__main__":
    main()
