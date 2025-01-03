# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.0] - 2025-01-02

### Added

- Added support for removal of lone p in Latin to Cyrillic conversion.
- Added accent support for dipthongs in Latin to Cyrillic conversion.
- Added normalization for "ву" in Cyrillic.
- Ignore lengthened vowel in Latin to Cyrillic conversion.
- Added normalization for "ー" in Latin to Katakana conversion.

### Fixed

- Fixed uppercase dipthong in Latin to Cyrillic and Cyrillic to Latin conversion.

## [0.7.0] - 2025-01-02

### Added

- Added normalization for invalid "yi-" and "wu-" syllable upon syllable separation.
- Added normalization for "йи" in Cyrillic.
- Added equal sign (`=`) removal upon syllable separation.
- Added support for merging "p" with the next token upon syllable separation.
- Added lowercase conversion upon syllable separation.
- Added extended Katakana mappings for long vowels.

### Fixed

- Fixed words with apostrophe are separated into words instead of as a single word.

## [0.6.2] - 2025-01-02

### Fixed

- Fixed syllables with accented vowels cannot be separated correctly.

## [0.6.1] - 2024-11-05

### Fixed

- Fixed missing 'チ' (`chi`) due to overlook.

## [0.6.0] - 2024-11-04

### Added

- Added support for combining diacritics in Latin to Cyrillic conversion.
- Added support for cyrillic accents in Latin to Cyrillic conversion.
- Added robustness test cases.
- Added support for half-width Katakana and Hiragana.

## [0.5.0] - 2024-11-03

### Added

- Added automatic apostrophe insertion in Katakana to Latin conversion.
- Added -y (ey, oy, uy) support for diphthongs in Katakana to Latin conversion.
- Added word level romanization for Katakana to Latin conversion.

## [0.4.0] - 2024-03-09

### Added

- Added conversion between Katakana and Cyrillic scripts.
- Added options for ィ (-y), ゥ (-w) and ㇴ (-n) usage in Latin to Katakana conversion.
- Added support from Python 3.8 and above.
- Added more badges to [README.md](README.md).
- Added [tox](https://tox.readthedocs.io/) for multi-environment testing.

## [0.3.0] - 2024-03-09

### Added

- Added options for ヰ (wi), ヱ (we) and ヲ (wo) usage in Latin to Katakana conversion.
- Added [Poe the Poet](https://github.com/nat-n/poethepoet) guidance in [CONTRIBUTING.md](CONTRIBUTING.md).
- Added check script for potential usage of dev-dependencies before release.
- Added changelog script to automate changelog update.
- Added links to [readthedocs](https://readthedocs.org/) in [README.md](README.md) and [pyproject.toml](pyproject.toml).

### Changed

- Improved publish flow to prevent unchecked push in [CONTRIBUTING.md](CONTRIBUTING.md).

### Fixed

- Fixed non-alphabetic group of syllable gets ignored.
- Fixed extra apostrophe in conversion from Latin.
- Fixed Cyrillic-Latin conversion not preserving case.
- Fixed Latin syllabification cannot handle multiple words.
- Fixed Latin with accented vowels cannot be converted to Kana.
- Fixed Kana variable coda conversion failure due to wrong logic.
- Fixed doc build error due to missing dependencies.
- Fixed git commit message template.

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
