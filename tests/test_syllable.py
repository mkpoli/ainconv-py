from src.ainconv.syllable import separate

SEPARATION_TEST_CASES = {
    "eyaykosiramsuypa": ["e", "yay", "ko", "si", "ram", "suy", "pa"],
    "irankarapte": ["i", "ran", "ka", "rap", "te"],
    "aynu itak": ["ay", "nu", " ", "i", "tak"],
    "wósekamuy": ["wó", "se", "ka", "muy"],
    "sineno  yayerampewtekkare": [
        "si",
        "ne",
        "no",
        "  ",
        "ya",
        "ye",
        "ram",
        "pew",
        "tek",
        "ka",
        "re",
    ],
}


def test_separate() -> None:
    for text, syllables in SEPARATION_TEST_CASES.items():
        assert separate(text) == syllables
