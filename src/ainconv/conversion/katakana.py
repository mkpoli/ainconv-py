from more_itertools import peekable

from ..conversion.latin import CONSONANTS
from ..syllable import separate

KANA_2_LATN = {
    "ア": "a",
    "イ": "i",
    "ウ": "u",
    "エ": "e",
    "オ": "o",
    "カ": "ka",
    "キ": "ki",
    "ク": "ku",
    "ケ": "ke",
    "コ": "ko",
    "サ": "sa",
    "シ": "si",
    "ス": "su",
    "セ": "se",
    "ソ": "so",
    "タ": "ta",
    "テ": "te",
    "ト": "to",
    "ナ": "na",
    "ニ": "ni",
    "ヌ": "nu",
    "ネ": "ne",
    "ノ": "no",
    "ハ": "ha",
    "ヒ": "hi",
    "フ": "hu",
    "ヘ": "he",
    "ホ": "ho",
    "パ": "pa",
    "ピ": "pi",
    "プ": "pu",
    "ペ": "pe",
    "ポ": "po",
    "マ": "ma",
    "ミ": "mi",
    "ム": "mu",
    "メ": "me",
    "モ": "mo",
    "ヤ": "ya",
    "ユ": "yu",
    "ヨ": "yo",
    "ラ": "ra",
    "リ": "ri",
    "ル": "ru",
    "レ": "re",
    "ロ": "ro",
    "ワ": "wa",
    "ヲ": "wo",
    "ン": "n",
    "ッ": "t",
    "ㇳ": "t",
    "ゥ": "w",
    "ㇰ": "k",
    "ㇵ": "x",
    "ㇶ": "x",
    "ㇷ": "x",
    "ㇸ": "x",
    "ㇹ": "x",
    "ァ": "a",
    "ェ": "e",
    "ォ": "o",
    "ㇻ": "r",
    "ㇼ": "r",
    "ㇽ": "r",
    "ㇾ": "r",
    "ㇿ": "r",
    "ィ": "y",
    "ㇷ": "h",
    "ㇱ": "s",
    "ㇺ": "m",
    "ㇴ": "n",
}

KANA_2_LATN_DIAGRAPH = {
    "イェ": "ye",
    "ウェ": "we",
    "ウィ": "wi",
    "ウォ": "wo",
    "トゥ": "tu",
    "ㇷ゚": "p",
    "ト゚": "tu",
    "チャ": "ca",
    "チュ": "cu",
    "チェ": "ce",
    "チョ": "co",
}


def kana2latn(kana: str) -> str:
    """Converts Katakana script to Latin script."""
    result = []
    chars = peekable(kana)

    for current_char in chars:
        latn = None
        next_char = chars.peek() if chars else None

        # print(current_char, next_char)

        if (
            current_char
            and next_char
            and current_char + next_char in KANA_2_LATN_DIAGRAPH
        ):
            # print(f"diagraph: {current_char + next_char = }")
            next(chars)
            latn = KANA_2_LATN_DIAGRAPH.get(current_char + next_char)
        else:
            latn = KANA_2_LATN.get(current_char)

        # print(f"{latn = }")
        result.append(latn if latn is not None else current_char)

    return "".join(result)


def latn2kana(text: str) -> str:
    """Converts Latin script to Katakana script."""
    syllables = separate(text)

    result = ""

    for i, syllable in enumerate(syllables):
        next_syllable = syllables[i + 1] if i + 1 < len(syllables) else None
        if len(syllable) == 0:
            continue

        last_char = syllable[-1]

        if last_char in CONSONANTS:
            (remains, coda) = syllable[:-1], last_char
        else:
            (remains, coda) = syllable, ""

        converted_remains = {
            "a": "ア",
            "i": "イ",
            "u": "ウ",
            "e": "エ",
            "o": "オ",
            "'a": "ア",
            "'i": "イ",
            "'u": "ウ",
            "'e": "エ",
            "'o": "オ",
            "’a": "ア",
            "’i": "イ",
            "’u": "ウ",
            "’e": "エ",
            "’o": "オ",
            "ka": "カ",
            "ki": "キ",
            "ku": "ク",
            "ke": "ケ",
            "ko": "コ",
            "sa": "サ",
            "si": "シ",
            "su": "ス",
            "se": "セ",
            "so": "ソ",
            "ta": "タ",
            "tu": "ト゚",
            "te": "テ",
            "to": "ト",
            "ca": "チャ",
            "ci": "チ",
            "cu": "チュ",
            "ce": "チェ",
            "co": "チョ",
            "na": "ナ",
            "ni": "ニ",
            "nu": "ヌ",
            "ne": "ネ",
            "no": "ノ",
            "ha": "ハ",
            "hi": "ヒ",
            "hu": "フ",
            "he": "ヘ",
            "ho": "ホ",
            "pa": "パ",
            "pi": "ピ",
            "pu": "プ",
            "pe": "ペ",
            "po": "ポ",
            "ma": "マ",
            "mi": "ミ",
            "mu": "ム",
            "me": "メ",
            "mo": "モ",
            "ya": "ヤ",
            "yi": "イ",
            "yu": "ユ",
            "ye": "イェ",
            "yo": "ヨ",
            "ra": "ラ",
            "ri": "リ",
            "ru": "ル",
            "re": "レ",
            "ro": "ロ",
            "wa": "ワ",
            "wi": "ヰ",
            "we": "ヱ",
            "wo": "ヲ",
            "nn": "ン",
            "tt": "ッ",
        }.get(remains)

        result += converted_remains or ""

        # print(f"{coda = } {next_syllable = }")

        next_char = next_syllable[0] if next_syllable else None

        converted_coda = {
            "w": "ゥ",
            "y": "ィ",
            "m": "ㇺ",
            "n": "ㇴ",
            "s": "ㇱ",
            "p": "ㇷ゚",
            "t": "ッ",
            "T": "ㇳ",
            "k": "ㇰ",
            "r": {
                "a": "ㇻ",
                "i": "ㇼ",
                "u": "ㇽ",
                "e": "ㇾ",
                "o": "ㇿ",
            }.get(next_char or "", "ㇽ"),
            "h": {
                "a": "ㇵ",
                "i": "ㇶ",
                "u": "ㇷ",
                "e": "ㇸ",
                "o": "ㇹ",
            }.get(next_char or "", "ㇷ"),
        }.get(coda, coda)

        result += converted_coda

    return (
        result.replace("ィ", "イ")
        .replace("ゥ", "ウ")
        .replace("ㇴ", "ン")
        .replace("ヱ", "ウェ")
        .replace("ヰ", "ウィ")
    )
