from src.ainconv import (
    latn2cyrl,
    cyrl2latn,
    latn2kana,
    kana2latn,
)

TEST_CASES = [
    ("", [], "", "", "", ""),
    ("aynu", ["ay", "nu"], "アイヌ", "айну", "애누", "ainu"),
    ("itak", ["i", "tak"], "イタㇰ", "итак", "이닥", "itak"),
    (
        "aynuitak",
        ["ay", "nu", "i", "tak"],
        "アイヌイタㇰ",
        "айнуитак",
        "애누이닥",
        "ainuitak",
    ),
    ("sinep", ["si", "nep"], "シネㇷ゚", "синэп", "시넙", "sinep"),
    ("ruunpe", ["ru", "un", "pe"], "ルウンペ", "руунпэ", "루운버", "ruunpe"),
    ("wenkur", ["we", "n", "kur"], "ウェンクㇽ", "вэнкур", "펀굴", "wenkur"),
    ("pekanke", ["pe", "kan", "ke"], "ペカンケ", "пэканкэ", "버간거", "pekanke"),
    (
        "eramuskare",
        ["e", "ra", "mus", "ka", "re"],
        "エラムㇱカレ",
        "эрамускарэ",
        "어라뭇가러",
        "eramuskare",
    ),
    ("hioy’oy", ["hi", "oy", "oy"], "ヒオイオイ", "хиойой", "히외외", "hioioi"),
    (
        "irankarapte",
        ["i", "ran", "ka", "rap", "te"],
        "イランカラㇷ゚テ",
        "иранкараптэ",
        "이란가랍더",
        "irankarapte",
    ),
    (
        "iyairaykere",
        ["i", "ya", "yi", "ray", "ke", "re"],
        "イヤイライケレ",
        "ияирайкэрэ",
        "이야이래거러",
        "iyairaikere",
    ),
    ("yayrayke", ["yay", "ray", "ke"], "ヤイライケ", "яйрайкэ", "얘래거", "yairaike"),
    (
        "keyaykosiramsuypa",
        ["ke", "yay", "ko", "si", "ram", "suy", "pa"],
        "ケヤイコシラㇺスイパ",
        "кэяйкосирамсуйпа",
        "거얘고시람쉬바",
        "keyaikosiramsuipa",
    ),
]


def test_latn2cyrl() -> None:
    for latn, _, _, cyrl, _, _ in TEST_CASES:
        assert latn2cyrl(latn) == cyrl


def test_cyrl2latn() -> None:
    for latn, _, _, cyrl, _, _ in TEST_CASES:
        assert cyrl2latn(cyrl) == latn


def test_latn2kana() -> None:
    for latn, _, kana, _, _, _ in TEST_CASES:
        assert latn2kana(latn) == kana


def test_kana2latn() -> None:
    for _, _, kana, _, _, latn_lossy in TEST_CASES:
        assert kana2latn(kana) == latn_lossy
