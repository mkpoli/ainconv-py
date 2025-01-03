<!-- omit in toc -->
# Contributing Guidance

Thank you for considering contributing to `ainconv`! 😘

We are happy to have you here. This document consists of some guidelines and instructions for contributing to `ainconv`.

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them.

Even if you don't have time, you can still support the project in other ways, such as starring the project, tweeting about it, or telling your friends about it. Every little bit helps!

<!-- omit in toc -->
## Table of Contents

- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Development](#development)
  - [Making Changes](#making-changes)
  - [Improving The Documentation](#improving-the-documentation)
  - [Publish a new version](#publish-a-new-version)

## Reporting Bugs

We use GitHub issues to track bugs and errors. If you run into an issue with the project, please open an issue and provide as much information as possible. This will help us to understand the problem and fix it.

## Suggesting Enhancements

If you have an idea for a new feature or an enhancement to an existing feature, please open an issue and describe the feature you would like to see. We will discuss the idea and decide if it is a good fit for the project.

## Development

General steps to contribute to the project:

1. Fork the repository and clone it locally.
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) and install the project. (`curl -LsSf https://astral.sh/uv/install.sh | sh` and `uv sync --all-extras --dev`)
3. Make your changes and run `uv run poe test` to run the tests.
4. Submit a pull request to the main repository.

### Making Changes

When committing, please also add a line to the `CHANGELOG.md` under the `Unreleased` section, describing the changes you made. This will help the maintainers to write the release notes when the time comes.

Commit messages need to start with a capital letter and a verb in the present tense, describing the change. For example, `Add support for Katakana` or `Fix bug in Cyrillic to Latin conversion`.

### Improving The Documentation

The documentation is located at [docs/](docs/). You can make changes to the documentation by editing the `.rst` files in this directory. The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/). You can build the documentation locally by running `poetry run make html` in the `docs/` directory.

### Publish a new version
> [!NOTE]  
> You can only publish a new version if you are a maintainer of the project and have the necessary rights to do so.

> [!WARNING]
> Do not use `poetry build` to build the package. Instead, use `poe build` to check before build to ensure that the package is ready for release.

<!-- - [ ] Bump the version in `pyproject.toml` (`poetry version <version>`)
- [ ] Update `CHANGELOG.md` with the new version from `Unreleased`. (`poe changelog`)
- [ ] Stage and commit the changes (`git commit -am "Bump version to <version>"`) -->
- [ ] Update `CHANGELOG.md` if there are any undocummented changes.
- [ ] Commit all changes in working tree.
- [ ] Check and build the package. (`uv run poe build`)
- [ ] Bump, commit and tag the version automatically. (`uv run poe bump` for interactive bump, or `uv run bump-my-version bump patch`, etc. for non-interactive bump)
- [ ] Push the changes to the remote repository. (`git push --follow-tags`)
<!-- - [ ] Create a new tag (`git tag -a <version> -m "Version <version>"`) and push it (`git push --tags`) -->
<!-- - [ ] Publish the package to PyPI (and `uv publish`) -->
<!-- - [ ] Create a new release on GitHub with the release notes from `CHANGELOG.md` -->
