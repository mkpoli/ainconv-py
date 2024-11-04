import pytest

from src.ainconv.utils import (
    combine_accents,
    is_vowel,
    is_consonant,
    is_letter,
    split_words,
)


def test_is_vowel():
    assert is_vowel("a") == True
    assert is_vowel("x") == False
    with pytest.raises(ValueError):
        is_vowel("ab")


def test_is_consonant():
    assert is_consonant("b") == True
    assert is_consonant("a") == False
    with pytest.raises(ValueError):
        is_consonant("ab")


def test_is_letter():
    assert is_letter("a") == True
    assert is_letter("あ") == True
    assert is_letter("1") == False
    assert is_letter("ん") == True
    assert is_letter("ハ") == True
    assert is_letter("ぁァ") == True
    assert is_letter("シネㇷ゚") == True


def test_split_words():
    assert split_words("This  is a test") == ["This", "  ", "is", " ", "a", " ", "test"]
    assert split_words("ヒオイオイ") == ["ヒオイオイ"]
    assert split_words("アイヌ イタク") == ["アイヌ", " ", "イタク"]
    assert split_words("シネㇷ゚") == ["シネㇷ゚"]


def test_combine_accents():
    assert combine_accents("á") == "á"
    assert combine_accents("áé") == "áé"
