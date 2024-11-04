import json
from src.ainconv import (
    latn2cyrl,
    cyrl2latn,
    latn2kana,
    kana2latn,
)
import json

with open("./tests/cases/test_cases.json", "r") as f:
    cases = json.load(f)

with open("./tests/cases/robustness.json", "r") as f:
    robustness_cases = json.load(f)


def test_latn2cyrl() -> None:
    for case in cases:
        assert latn2cyrl(case["latn"]) == case["cyrl"]

    for case in robustness_cases:
        if case["from"] == "Latn":
            assert latn2cyrl(case["Latn"]) == case["Cyrl"]


def test_cyrl2latn() -> None:
    for case in cases:
        assert cyrl2latn(case["cyrl"]) == case["latn"]

    for case in robustness_cases:
        if case["from"] == "Cyrl":
            assert cyrl2latn(case["Cyrl"]) == case["Latn"]


def test_latn2kana() -> None:
    for case in cases:
        assert latn2kana(case["latn"]) == case["kana"]

    for case in robustness_cases:
        if case["from"] == "Latn":
            assert latn2kana(case["Latn"]) == case["Kana"]

    # Test variations

    ## -y, -w, -n
    assert latn2kana("kay") == "カイ"
    assert latn2kana("kay", use_small_i=True) == "カィ"
    assert latn2kana("kew") == "ケウ"
    assert latn2kana("kew", use_small_u=True) == "ケゥ"
    assert latn2kana("mun") == "ムン"
    assert latn2kana("mun", use_small_n=True) == "ムㇴ"

    ## wi, we, wo
    assert latn2kana("wiki") == "ウィキ"  # for loanwords only
    assert latn2kana("wiki", use_wi=True) == "ヰキ"
    assert latn2kana("weni") == "ウェニ"
    assert latn2kana("weni", use_we=True) == "ヱニ"
    assert latn2kana("wose") == "ウォセ"
    assert latn2kana("wose", use_wo=True) == "ヲセ"
    assert latn2kana("wósekamuy") == "ウォセカムイ"
    assert latn2kana("wósekamuy", use_wo=True) == "ヲセカムイ"
    assert latn2kana("wiwewo") == "ウィウェウォ"
    assert latn2kana("wiwewo", use_wi=True, use_we=True, use_wo=True) == "ヰヱヲ"


def test_kana2latn() -> None:
    for case in cases:
        assert kana2latn(case["kana"]) == case["latnLossy"]

    for case in robustness_cases:
        if case["from"] == "Kana":
            assert kana2latn(case["Kana"]) == case["Latn"]
