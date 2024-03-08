<!-- omit in toc -->
# ainconv - Ainu language script converter

![Version](https://img.shields.io/pypi/v/ainconv)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ainconv)
![GitHub issues](https://img.shields.io/github/issues/mkpoli/ainconv-py)
![GitHub](https://img.shields.io/github/license/mkpoli/ainconv-py)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.aynu.org/)

<!-- omit in toc -->
## Table of Contents

- [Overview](#overview)
  - [Important Note](#important-note)
- [Installation](#installation)
- [Usage](#usage)
  - [Word Conversion](#word-conversion)
  - [Extra Functionality](#extra-functionality)
    - [Script Detection](#script-detection)
    - [Syllable Splitting](#syllable-splitting)
- [Support](#support)
- [License](#license)
- [See also](#see-also)

## Overview

This package provides a comprehensive set of functions for converting text between different writing systems of the [Ainu language](https://en.wikipedia.org/wiki/Ainu_language).

Currently, Latin (Romanization), Katakana and Cyrillic scripts are supported. We are also planning to convert between different romanization systems and Katakana variants. Currently only the more adopted version of Latin script and lossy Katakana script are supported.

Sentence conversion is planned to be supported in the future. For now, only well-formed single word is accepted. The converted string are always in lower case.

### Important Note

Conversion between Latin and Cyrillic script are lossless, however, conversion between Katakana and other scripts are lossy. This means that converting from Katakana to other scripts and then back to Katakana may not give the original string and the result may be ambiguous or even incorrect.

This is because the Katakana script used broadly for the Ainu language is intrinsically ambiguous. For example, it does not distinguish between *tow* and *tu* (both *トゥ*), *iw* and *i.u* (both *イウ*), *ay* and *a.i* (both *アイ*), etc. Some alternative Katakana scripts are proposed to solve this problem, but none of them are widely adopted. We are planning to support some of these alternative scripts in the future.

## Installation

Install the package using pip

```bash
pip install ainconv
```

## Usage

### Word Conversion

```python
from ainconv import (
    kana2latn,
    latn2kana,
    cyrl2latn,
    latn2cyrl,
    kana2cyrl,
    cyrl2kana,
    # ...
)

print(kana2latn("イランカラㇷ゚テ")) # "irankarapte"
print(latn2kana("irankarapte")) # "イランカラㇷ゚テ"
print(cyrl2latn("иранкараптэ")) # "irankarapte"
print(latn2cyrl("irankarapte")) # "иранкараптэ"
print(cyrl2kana("иранкараптэ")) # "イランカラㇷ゚テ"
print(kana2cyrl("イランカラㇷ゚テ")) # "иранкараптэ"
```

### Extra Functionality

#### Script Detection

Detect the script of a given string.

```python
from ainconv import detect

print(detect("aynu")) # "Latn"
print(detect("アイヌ")) # "Kana"
print(detect("айну")) # "Cyrl"
```

#### Syllable Splitting

```python
from ainconv import separate

print(separate("eyaykosiramsuypa")) # ["e", "yay", "ko", "si", "ram", "suy", "pa"]
```

## Support

If you have a question or have found a bug or any other issue, feel free to [open an issue](https://github.com/mkpoli/ainconv-py/issues/new) to let me know. For instructions on how to contribute, see [CONTRIBUTING.md](https://github.com/mkpoli/ainconv-py/blob/master/CONTRIBUTING.md).

You can also [join our Discord](https://discord.aynu.org/) for discussion. We have many projects going on about Ainu, so you may find something interesting there as well.

## License

[MIT License](LICENSE) (c) 2024 mkpoli

## See also

* [ainconv - npm](https://www.npmjs.com/package/ainconv): The JavaScript version of this package
* [ainconv - crates.io](https://crates.io/crates/ainconv): The Rust version of this package
* [Module:ain-kana-conv - ウィクショナリー日本語版](https://ja.wiktionary.org/wiki/%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB:ain-kana-conv): The original Lua Scribunto module in the Japanese Wiktionary
