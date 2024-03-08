# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added options for ヰ (wi), ヱ (we) and ヲ (wo) usage in Latin to Katakana conversion.
- Added [Poe the Poet](https://github.com/nat-n/poethepoet) guidance in [CONTRIBUTING.md](CONTRIBUTING.md).
- Added check script for potential usage of dev-dependencies before release.
- Added links to [readthedocs](https://readthedocs.org/) in [README.md](README.md) and [pyproject.toml](pyproject.toml).

### Fixed

- Fixed Latn with accented vowels cannot be converted to Kana.
- Fixed Kana variable coda conversion failure due to wrong logic.
- Fixed doc build error due to missing dependencies.

### Removed

- Removed Python version badge from [README.md](README.md).

## [0.2.0] - 2024-03-09

### Added

- Added [CHANGELOG.md](CHANGELOG.md) file (current file).
- Added PyPI version badge from [Shields.io](https://shields.io/).
- Added Support section to [README.md](README.md).
- Added Discord badge and links to [README.md](README.md).
- Added [CONTRIBUTING.md](CONTRIBUTING.md) file for contribution guidelines.
- Added MIT License to [LICENSE](LICENSE) file.
- Added [Sphinx](https://www.sphinx-doc.org/) documentation.
- Added [readthedocs](https://readthedocs.org/) integration.
- Added links to badges in [README.md](README.md).

### Fixed

- Fixed unexpected stdout output by removing `print` statements.

## [0.1.1] - 2024-03-08

### Fixed

- Fixed error due to invalid `tool.poetry.scripts` settings, using poe instead.

## [0.1.0] - 2024-03-03

### Added

- Added conversion between Katakana, Cyrillic and Latin scripts.
