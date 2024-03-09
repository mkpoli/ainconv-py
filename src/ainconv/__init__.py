from .conversion.cyrillic import latn2cyrl, cyrl2latn
from .conversion.katakana import latn2kana, kana2latn
from .syllable import separate
from .detection import detect, Script


def cyrl2kana(cyrl: str, **kwargs) -> str:
    """Converts Cyrillic script to Katakana script.

    See Also:
        `latn2kana` for `kwargs`.
    """
    return latn2kana(cyrl2latn(cyrl), **kwargs)


def kana2cyrl(kana: str) -> str:
    """Converts Katakana script to Cyrillic script."""
    return latn2cyrl(kana2latn(kana))


__all__ = [
    "latn2kana",
    "kana2latn",
    "latn2cyrl",
    "cyrl2latn",
    "kana2cyrl",
    "cyrl2kana",
    "separate",
    "detect",
    "Script",
]
