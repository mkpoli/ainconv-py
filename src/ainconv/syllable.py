from .conversion.latin import VOWELS, CONSONANTS

# from icecream import ic


def separate_word(text: str) -> list[str]:
    syllable_map = {}
    syllable_count = 1

    for i, char in enumerate(text):
        if char in VOWELS:
            if i > 0 and text[i - 1] in CONSONANTS:
                syllable_map[i - 1] = syllable_count
            syllable_map[i] = syllable_count
            syllable_count += 1

    for i in range(len(text)):
        if i not in syllable_map:
            syllable_map[i] = syllable_map.get(i - 1, 0)

    syllables = []
    current_group_id = 1
    head = 0

    for i in range(len(text)):
        if syllable_map.get(i, 0) != current_group_id:
            current_group_id = syllable_map.get(i, 0)
            syllables.append(text[head:i])
            head = i

    syllables.append(text[head:])

    return [
        s.replace("'", "")
        .replace("’", "")
        .replace("yi", "i")
        .replace("wu", "u")
        .replace("=", "")
        for s in syllables
    ]


def is_letter(char: str) -> bool:
    return char.isalpha() or char in "’'="


def separate(text: str) -> list[str]:
    """Separate a romanized Ainu word into syllables.

    Args:
        text (str): A string that holds the romanized Ainu word.

    Returns:
        str: A list of syllables.
    """
    if not text:
        return []

    text = text.lower()

    result: list[str] = []
    current_group: list[str] = []

    last_alpha = is_letter(text[0])

    for char in text:
        # ic(char, last_alpha, current_group, result)

        current_alpha = is_letter(char)
        # ic(current_alpha, last_alpha, current_alpha == last_alpha)

        if current_alpha != last_alpha:
            if current_group:
                joined = "".join(current_group)
                if last_alpha:
                    result += separate_word(joined)
                else:
                    result.append(joined)
                current_group = [char]
            else:
                current_group.append(char)
        else:
            current_group.append(char)

        last_alpha = current_alpha

    if current_group:
        joined = "".join(current_group)
        if last_alpha:
            result += separate_word(joined)
        else:
            result.append(joined)

    result = [r for r in result if r]

    processed = []
    i = 0
    while i < len(result):
        token = result[i]
        if token == " " and i + 1 < len(result) and result[i + 1] == "p":
            processed[-1] += "p"
            i += 2  # skip the "p"
        else:
            processed.append(token)
            i += 1

    result = [t for t in processed if t]

    return result if result[0] else result[1:]
