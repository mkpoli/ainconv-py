from more_itertools import peekable

from ..utils import combine_accents

LATN_2_CYRL = {
    "a": "а",
    "á": "а́",
    "â": "а",
    "i": "и",
    "í": "и́",
    "î": "и",
    "u": "у",
    "ú": "у́",
    "û": "у",
    "e": "э",
    "é": "э́",
    "o": "о",
    "ó": "о́",
    "ô": "о",
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
    "ú": "ю́",
    "a": "я",
    "á": "я́",
    "o": "ё",
    "ó": "ё́",
    "e": "е",
    "é": "е́",
}

LATN_2_CYRL_Y_WITH_Y = {f"y{k}": v for k, v in LATN_2_CYRL_Y.items()}

CYRL_2_LATN_Y = {
    "у": "y’u",
    "а": "y’a",
    "о": "y’o",
    "э": "y’e",
}

CYRL_2_LATN_Y_ACCENTED = {
    "ю": "yu",
    "ю́": "yú",
    "я": "ya",
    "я́": "yá",
    "ё": "yo",
    "ё́": "yó",
    "е": "ye",
    "е́": "yé",
}


def latn2cyrl(text: str) -> str:
    """Converts Latin script to Cyrillic script."""
    merged_chunks = []
    for chunk in text.split(" "):
        if chunk.lower() == "p" and merged_chunks:
            merged_chunks[-1] += chunk
        else:
            merged_chunks.append(chunk)
    text = " ".join(merged_chunks)

    result = []
    chars = peekable(text)
    while True:
        try:
            current_char = next(chars)
        except StopIteration:
            break

        current_lower = current_char.lower()

        # Peek at next char
        try:
            next_char = chars.peek()
            next_lower = next_char.lower()
        except StopIteration:
            next_char = None
            next_lower = None

        if current_lower == "y" and next_lower in LATN_2_CYRL_Y:
            _ = next(chars)
            cyrl = LATN_2_CYRL_Y[next_lower]
            if current_char.isupper():
                cyrl = combine_accents(cyrl.upper())
        else:
            cyrl = LATN_2_CYRL.get(current_lower, current_char)
            if current_char.isupper() and cyrl != current_char:
                cyrl = combine_accents(cyrl.upper())

        result.append(cyrl)

    text_cyrl = "".join(result)
    text_cyrl = text_cyrl.replace("’", "").replace("йи", "и").replace("ву", "у")
    return text_cyrl


def cyrl2latn(text: str) -> str:
    """Converts Cyrillic script to Latin script."""
    result = []
    chars = peekable(text)

    while True:
        try:
            current_char = next(chars)
        except StopIteration:
            break

        current_lower = current_char.lower()
        latn = None

        # Peek next char
        try:
            next_char = chars.peek()
            next_lower = next_char.lower()
        except StopIteration:
            next_char = None
            next_lower = None

        if current_lower in CYRL_2_LATN_Y_ACCENTED:
            latn = CYRL_2_LATN_Y_ACCENTED[current_lower]
        elif current_lower == "й" and next_lower in CYRL_2_LATN_Y:
            next(chars)
            latn = CYRL_2_LATN_Y.get(next_lower)
        else:
            latn = next(
                (
                    latn
                    for latn, cyrl in (LATN_2_CYRL | LATN_2_CYRL_Y_WITH_Y).items()
                    if cyrl == current_lower
                ),
                None,
            )

        if current_char.isupper():
            if latn and len(latn) > 1:
                latn = latn[0].upper() + latn[1:]
            else:
                latn = latn.upper() if latn else current_char

        result.append(latn if latn is not None else current_char)

    return combine_accents("".join(result)).replace("yi", "i").replace("wu", "u")
