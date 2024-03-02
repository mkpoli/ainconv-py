from src.ainconv.syllable import separate


def test_separate() -> None:
    separated = separate("eyaykosiramsuypa")
    assert separated == ["e", "yay", "ko", "si", "ram", "suy", "pa"]
    print(separated)
