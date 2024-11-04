<!-- omit in toc -->
# ainconv - Ainu language script converter

[![Version](https://img.shields.io/pypi/v/ainconv)](https://pypi.org/project/ainconv/)
[![Downloads](https://pepy.tech/badge/ainconv)](https://pepy.tech/project/ainconv)
[![Python Versions](https://img.shields.io/pypi/pyversions/ainconv)](https://pypi.org/project/ainconv/)
[![Read the Docs](https://img.shields.io/readthedocs/ainconv-py)](https://ainconv-py.readthedocs.io/)
[![MIT License](https://img.shields.io/pypi/l/ainconv)](./LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/mkpoli/ainconv-py)](https://github.com/mkpoli/ainconv-py/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/mkpoli/ainconv-py)](https://github.com/mkpoli/ainconv-py/issues)
[![test](https://github.com/mkpoli/ainconv-py/actions/workflows/test.yml/badge.svg)](https://github.com/mkpoli/ainconv-py/actions/workflows/test.yml)
[![Discord](https://dcbadge.vercel.app/api/server/pkpAdPHzpP?style=flat)](https://discord.aynu.org/)
[![Aynuitak](https://img.shields.io/badge/lang-ain-red`)](https://wiki.aynu.org/wiki/Aynu_itak)

<!-- omit in toc -->
## Table of Contents

- [Overview](#overview)
  - [Important Note](#important-note)
- [Installation](#installation)
- [Usage](#usage)
  - [Word Conversion](#word-conversion)
  - [Extra Functionality](#extra-functionality)
    - [Conversion Options](#conversion-options)
      - [Katakana](#katakana)
    - [Script Detection](#script-detection)
    - [Syllable Splitting](#syllable-splitting)
- [Support](#support)
- [License](#license)
- [See also](#see-also)

## Overview


> [!IMPORTANT]
> By default, conversions between Katakana to and from any script are inherently lossy. See [Important Note](#important-note) for more details.

This package provides a comprehensive set of functions for converting text between different writing systems of the [Ainu language](https://en.wikipedia.org/wiki/Ainu_language).

Currently, Latin (Romanization), Katakana and Cyrillic scripts are supported. We are also planning to convert between different romanization systems and Katakana variants. Currently only the more adopted version of Latin script and lossy Katakana script are supported.

Sentence conversion is planned to be supported in the future. For now, only well-formed single word is accepted. The converted string are always in lower case.

### Important Note

Conversion between Latin and Cyrillic script are lossless, however, conversion between Katakana and any other scripts are lossy. This means that converting from Katakana to other scripts and then back to Katakana may not give the original string and the result may be ambiguous or even incorrect.

This is because the most widely used Katakana orthography for the Ainu language is intrinsically ambiguous. For example, *tow* and *tu* are both *トゥ*, *iw* and *i.u* are both *イウ*, *ay* and *a.i* are both *アイ*, etc. Some alternative Katakana scripts are proposed to solve this problem, but none of them are widely adopted.

We already added some options (see [Conversion Options](#conversion-options)) for Katakana output and are planning to support others to mitigate this problem. However, since Katakana orthography still contains less information than Latin orthography, you cannot get the original text back from the converted text, distinctions such as `-w`, `-y` and `-n` (with options off), `=` and `-` symbols, letter case, etc. are lost in the conversion. Additionally, Katakana text from elsewhere usually does not contain these distinctions, so converting losslessly from Katakana to other scripts is impossible.

## Installation

Install the package using pip

```bash
pip install ainconv
```

## Usage

> [!NOTE]
> You can also read the full documentation on [Read the Docs](https://ainconv-py.readthedocs.io/).

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

#### Conversion Options

##### Katakana

```python
from ainconv import latn2kana

# Use ィ (-y), ゥ (-w) and ㇴ (-n)
assert latn2kana("kay") == "カイ"
assert latn2kana("kay", use_small_i=True) == "カィ"
assert latn2kana("kew") == "ケウ"
assert latn2kana("kew", use_small_u=True) == "ケゥ"
assert latn2kana("mun") == "ムン"
assert latn2kana("mun", use_small_n=True) == "ムㇴ"

# Use ヰ (wi), ヱ (we) and ヲ (wo) 
assert latn2kana("wiki") == "ウィキ"  # for loanwords only
assert latn2kana("wiki", use_wi=True) == "ヰキ"
assert latn2kana("weni") == "ウェニ"
assert latn2kana("weni", use_we=True) == "ヱニ"
assert latn2kana("wóse") == "ウォセ"
assert latn2kana("wóse", use_wo=True) == "ヲセ"

assert latn2kana("wiwewo") == "ウィウェウォ"
assert latn2kana("wiwewo", use_wi=True, use_we=True, use_wo=True) == "ヰヱヲ"
```


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
