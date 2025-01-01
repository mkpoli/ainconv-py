import json

from src.ainconv.syllable import separate


def test_separate() -> None:
    for case in cases:
        assert separate(case["latn"]) == case["syllables"]


with open("./tests/cases/test_cases.json", "r") as f:
    cases = json.load(f)
