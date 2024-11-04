def is_vowel(char: str):
    if len(char) != 1:
        raise ValueError("is_vowel expects a single character")
    return char in "aiueoáíúéóāīūēōAIUEOÁÍÚÉÓĀĪŪĒŌ"


def is_consonant(char: str):
    if len(char) != 1:
        raise ValueError("is_consonant expects a single character")
    return char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"


def is_letter(s: str):
    return all(c.isalpha() or c in "\u309A" for c in s)


def split_words(s):
    if not s:
        return []
    result = []
    current = s[0]
    current_is_letter = is_letter(s[0])
    for c in s[1:]:
        if is_letter(c) == current_is_letter:
            current += c
        else:
            result.append(current)
            current = c
            current_is_letter = is_letter(c)
    result.append(current)
    return result


ACCENTS_COMBINATIONS = {
    "á": "á",
    "é": "é",
    "ó": "ó",
    "ú": "ú",
    "í": "í",
}


def combine_accents(s: str):
    for k, v in ACCENTS_COMBINATIONS.items():
        s = s.replace(k, v)
    return s
