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

    return [s.replace("'", "") for s in syllables]


def separate(text: str) -> list[str]:
    """Separate a romanized Ainu word into syllables.

    Args:
        text (str): A string that holds the romanized Ainu word.

    Returns:
        str: A list of syllables.
    """
    if not text:
        return []

    result: list[str] = []
    current_group: list[str] = []

    last_alpha = text[0].isalpha()

    for char in text:
        # ic(char, last_alpha, current_group, result)

        current_alpha = char.isalpha()
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

    return result if result[0] else result[1:]
