from src.ainconv.detection import detect, Script


def test_detect() -> None:
    assert detect("アイヌ") == Script.Kana
    assert detect("айну") == Script.Cyrl
    assert detect("aynu") == Script.Latn
    assert detect("アイヌайну") == Script.Mixed
    assert detect("愛努") == Script.Unknown
