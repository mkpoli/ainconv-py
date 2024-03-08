from more_itertools import peekable

LATN_2_CYRL = {
    "a": "а",
    "i": "и",
    "u": "у",
    "e": "э",
    "o": "о",
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

        result.append(cyrl if cyrl is not None else current_char)

    return "".join(result)


def cyrl2latn(text: str) -> str:
    """Converts Cyrillic script to Latin script."""
    result = []
    chars = peekable(text)

    for current_char in chars:
        current_lower = current_char.lower()
        cyrl = None
        next_char = chars.peek() if chars else None
        next_lower = next_char.lower() if next_char else None

        # print(f"f{current_lower = } {next_lower = }")

        if current_lower == "й" and next_lower in CYRL_2_LATN_Y:
            # print("й with vowel")
            next(chars)
            cyrl = CYRL_2_LATN_Y.get(next_lower)
        else:
            # print(LATN_2_CYRL | LATN_2_CYRL_Y)

            cyrl = next(
                (
                    latn
                    for latn, cyrl in (LATN_2_CYRL | LATN_2_CYRL_Y_WITH_Y).items()
                    if cyrl == current_lower
                ),
                None,
            )

        result.append(cyrl if cyrl is not None else current_char)

    return "".join(result)
