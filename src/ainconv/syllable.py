from .conversion.latin import VOWELS, CONSONANTS


def separate(text: str) -> list[str]:
    """Separate a romanized Ainu word into syllables.

    Args:
        text (str): A string that holds the romanized Ainu word.

    Returns:
        str: A list of syllables.
    """
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
