from more_itertools import peekable

from ..utils import combine_accents

LATN_2_CYRL = {
    "a": "а",
    "á": "а́",
    "i": "и",
    "í": "и́",
    "u": "у",
    "ú": "у́",
    "e": "э",
    "é": "э́",
    "o": "о",
    "ó": "о́",
    "k": "к",
    "s": "с",
    "t": "т",
    "c": "ц",
    "h": "х",
    "m": "м",
    "n": "н",
    "p": "п",
    "r": "р",
    "w": "в",
    "y": "й",
    "'": "ъ",
    "’": "",
}

LATN_2_CYRL_Y = {
    "u": "ю",
    "a": "я",
    "o": "ё",
    "e": "е",
}

LATN_2_CYRL_Y_WITH_Y = {f"y{k}": v for k, v in LATN_2_CYRL_Y.items()}

CYRL_2_LATN_Y = {
    "у": "y’u",
    "а": "y’a",
    "о": "y’o",
    "э": "y’e",
}


def latn2cyrl(text: str) -> str:
    """Converts Latin script to Cyrillic script."""
    result = []
    chars = peekable(text)

    for current_char in chars:
        current_lower = current_char.lower()
        cyrl = None
        next_char = chars.peek() if chars else None
        next_lower = next_char.lower() if next_char else None

        if current_lower == "y" and next_lower in LATN_2_CYRL_Y:
            next(chars)
            cyrl = LATN_2_CYRL_Y.get(next_lower)
            if cyrl:
                if current_char.isupper():
                    cyrl = cyrl.upper()
        else:
            cyrl = LATN_2_CYRL.get(current_lower)

        cyrl = cyrl or current_char
        cyrl = cyrl.upper() if current_char.isupper() else cyrl

        result.append(cyrl)

    return "".join(result).replace("’", "")


def cyrl2latn(text: str) -> str:
    """Converts Cyrillic script to Latin script."""
    result = []
    chars = peekable(text)

    for current_char in chars:
        current_lower = current_char.lower()
        latn = None
        next_char = chars.peek() if chars else None
        next_lower = next_char.lower() if next_char else None

        # print(f"f{current_lower = } {next_lower = }")

        if current_lower == "й" and next_lower in CYRL_2_LATN_Y:
            # print("й with vowel")
            next(chars)
            latn = CYRL_2_LATN_Y.get(next_lower)
        else:
            # print(LATN_2_CYRL | LATN_2_CYRL_Y)

            latn = next(
                (
                    latn
                    for latn, cyrl in (LATN_2_CYRL | LATN_2_CYRL_Y_WITH_Y).items()
                    if cyrl == current_lower
                ),
                None,
            )

        latn = latn or current_char
        latn = latn.upper() if current_char.isupper() else latn

        result.append(latn if latn is not None else current_char)

    return combine_accents("".join(result))
