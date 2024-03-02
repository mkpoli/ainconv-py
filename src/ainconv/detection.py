from enum import Enum


def is_cyrillic(char: str) -> bool:
    return "\u0400" <= char <= "\u04FF"


def is_katakana(char: str) -> bool:
    return "\u30A1" <= char <= "\u31FF"


class Script(Enum):
    """An enumeration of the possible script types for the Ainu language."""

    """The Katakana script."""
    Kana = "Kana"

    """The Cyrillic script."""
    Cyrl = "Cyrl"

    """The Latin script."""
    Latn = "Latn"

    """A mixed script."""
    Mixed = "Mixed"

    """An unknown script."""
    Unknown = "Unknown"


def detect(text: str) -> Script:
    """Detects the script type of a given Ainu language string.

    This function categorizes the script into one of several types based on the characters present in the string.

    It supports Latin, Cyrillic, Katakana scripts, and can also identify mixed or unknown scripts.

    Args:
        text (str): The text string to be analyzed for script type.

    Returns:
        Script: The detected script type:
            Kana for Katakana
            Cyrl for Cyrillic
            Latn for Latin
            Mixed if multiple scripts are detected
            Unknown if no script is detected
    """
    has_latin = any(c.isalpha() and c.isascii() for c in text)
    has_cyrillic = any(c.isalpha() and is_cyrillic(c) for c in text)
    has_kana = any(c.isalpha() and is_katakana(c) for c in text)

    if [has_latin, has_cyrillic, has_kana].count(True) > 1:
        return Script.Mixed
    elif has_kana:
        return Script.Kana
    elif has_cyrillic:
        return Script.Cyrl
    elif has_latin:
        return Script.Latn
    else:
        return Script.Unknown
