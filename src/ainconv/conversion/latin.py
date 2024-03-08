VOWELS = "aeiou"
CONSONANTS = "ptckmnshwry’"

from unicodedata import normalize

ACCENTED_VOWELS = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
}


def clean(text: str) -> str:
    """Clean up Latin script.

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """

    return (
        normalize("NFKC", text)
        .replace("-", "")
        .replace("=", "")
        .replace(".", "")
        .replace(",", "")
    )
