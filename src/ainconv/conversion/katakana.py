import unicodedata
from more_itertools import peekable

from ..utils import is_vowel, split_words


# from icecream import ic

# ic.configureOutput(includeContext=True)

from ..conversion.latin import ACCENTED_VOWELS, CONSONANTS, clean
from ..syllable import separate

HALF_WIDTH_KATAKANA_TABLE = {
    # ア行
    "ｱ": "ァ",
    "ｲ": "ィ",
    "ｳ": "ゥ",
    "ｴ": "ェ",
    "ｵ": "ォ",
    # カ行
    "ｸ": "ㇰ",
    "ｹ": "ヶ",
    # サ行
    "ｼ": "ㇱ",
    "ｽ": "ㇲ",
    # タ行
    "ﾄ": "ㇳ",
    "ﾀ": "ㇴ",
    # ナ行
    "ﾇ": "ㇴ",
    # ハ行
    "ﾊ": "ㇵ",
    "ﾋ": "ㇶ",
    "ﾌ": "ㇷ",
    "ﾍ": "ㇸ",
    "ﾎ": "ㇹ",
    # パ行
    "ﾌﾟ": "ㇷ゚",
    # マ行
    "ﾑ": "ㇺ",
    # ヤ行
    "ﾔ": "ャ",
    "ﾕ": "ュ",
    "ﾖ": "ョ",
    # ラ行
    "ﾗ": "ㇻ",
    "ﾘ": "ㇼ",
    "ﾙ": "ㇽ",
    "ﾚ": "ㇾ",
    "ﾛ": "ㇿ",
    # ワ行
    "ﾜ": "ヮ",
    "ｦ": "𛅦",
    # 撥音
    "ﾝ": "𛅧",
    # There is no half-width version of ヱ (we) and ヰ (wi)
}

HIRAGANA_TO_KATAKANA_TABLE = {
    "あ": "ア",
    "い": "イ",
    "う": "ウ",
    "ゔ": "ヴ",
    "え": "エ",
    "お": "オ",
    "か": "カ",
    "き": "キ",
    "く": "ク",
    "け": "ケ",
    "こ": "コ",
    "が": "ガ",
    "ぎ": "ギ",
    "ぐ": "グ",
    "げ": "ゲ",
    "ご": "ゴ",
    "さ": "サ",
    "し": "シ",
    "す": "ス",
    "せ": "セ",
    "そ": "ソ",
    "ざ": "ザ",
    "じ": "ジ",
    "ず": "ズ",
    "ぜ": "ゼ",
    "ぞ": "ゾ",
    "た": "タ",
    "ち": "チ",
    "つ": "ツ",
    "て": "テ",
    "と": "ト",
    "だ": "ダ",
    "ぢ": "ヂ",
    "づ": "ヅ",
    "で": "デ",
    "ど": "ド",
    "な": "ナ",
    "に": "ニ",
    "ぬ": "ヌ",
    "ね": "ネ",
    "の": "ノ",
    "は": "ハ",
    "ひ": "ヒ",
    "ふ": "フ",
    "へ": "ヘ",
    "ほ": "ホ",
    "ば": "バ",
    "び": "ビ",
    "ぶ": "ブ",
    "べ": "ベ",
    "ぼ": "ボ",
    "ぱ": "パ",
    "ぴ": "ピ",
    "ぷ": "プ",
    "ぺ": "ペ",
    "ぽ": "ポ",
    "ま": "マ",
    "み": "ミ",
    "む": "ム",
    "め": "メ",
    "も": "モ",
    "や": "ヤ",
    "ゆ": "ユ",
    "よ": "ヨ",
    "ら": "ラ",
    "り": "リ",
    "る": "ル",
    "れ": "レ",
    "ろ": "ロ",
    "わ": "ワ",
    "ゐ": "ヰ",
    "ゑ": "ヱ",
    "を": "ヲ",
    "ん": "ン",
    "っ": "ッ",
    "ゃ": "ャ",
    "ゅ": "ュ",
    "ょ": "ョ",
    "ぁ": "ァ",
    "ぃ": "ィ",
    "ぅ": "ゥ",
    "ぇ": "ェ",
    "ぉ": "ォ",
    "ゎ": "ヮ",
    "𛅐": "𛅤",
    "𛅑": "𛅥",
    "𛅒": "𛅦",
}


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
    "チ": "ci",
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
    "𛅧": "n",
    "ー": "̂",
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
    "エイ": "ey",
    "オイ": "oy",
    "ウイ": "uy",
}

NON_COMBINING_MODIFIERS = {
    "゜": "\u309A",  # U+309A COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK "◌゚"
    "゛": "\u3099",  # U+3099 COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK "◌゙"
}


def kana2latn(kana: str) -> str:
    """Converts Katakana script to Latin script."""

    def convert_word(word: str):
        for char in NON_COMBINING_MODIFIERS:
            word = word.replace(char, NON_COMBINING_MODIFIERS[char])
        word = unicodedata.normalize("NFC", word)
        print(word)
        for char in word:
            if char in HIRAGANA_TO_KATAKANA_TABLE:
                word = word.replace(char, HIRAGANA_TO_KATAKANA_TABLE[char])
        for char in HALF_WIDTH_KATAKANA_TABLE:
            word = word.replace(char, HALF_WIDTH_KATAKANA_TABLE[char])

        result = []
        chars = peekable(word)

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

        joined = "’".join(result)

        result = []
        for i, char in enumerate(joined):
            print(i, char)
            if char == "’":
                if i > 0 and is_vowel(joined[i - 1]):
                    # If the previous character is not a consonant, remove the apostrophe\
                    continue
                if i < len(joined) - 1 and not is_vowel(joined[i + 1]):
                    # If the next character is not a vowel, remove the apostrophe
                    continue
            result.append(char)

        print(f"{result = }")
        joined = "".join(result)
        joined = unicodedata.normalize("NFC", joined)
        print(f"{joined = }")
        return joined

    return "".join(convert_word(word) for word in split_words(kana))


def latn2kana(
    text: str,
    use_wi: bool = False,
    use_we: bool = False,
    use_wo: bool = False,
    use_small_i: bool = False,
    use_small_u: bool = False,
    use_small_n: bool = False,
) -> str:
    """Converts Latin script to Katakana script.

    Args:
        text (str): The Latin script to be converted.
        use_wi (bool): Whether to use "ヰ" (wi) instead of "ウィ" (wi), e.g. "wiki" -> "ヰキ" instead of "ウィキ".
        use_we (bool): Whether to use "ヱ" (we) instead of "ウェ" (we), e.g. "weni" -> "ヱニ" instead of "ウェニ".
        use_wo (bool): Whether to use "ヲ" (wo) instead of "ウォ" (wo). e.g. "wóse" -> "ヲセ" instead of "ウォセ".
        use_small_i (bool): Whether to use "ィ" (y) instead of "イ" for -y, e.g. "kay" -> "カィ" instead of "カイ".
        use_small_u (bool): Whether to use "ゥ" (w) instead of "ウ" for -w, e.g. "kew" -> "ケゥ" instead of "ケウ".
        use_small_n (bool): Whether to use "ン" (n) instead of "ㇴ" for -n, e.g. "mun" -> "ムン" instead of "ムㇴ".

    Returns:
        str: The converted Katakana script.
    """
    syllables = separate(text)
    # ic(syllables)

    result = ""

    for syllable in syllables:
        syllable = clean(syllable.lower())

        if not any(char.isalpha() for char in syllable):
            result += syllable
            continue

        for accented, vowel in ACCENTED_VOWELS.items():
            syllable = syllable.replace(accented, vowel)

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
            "â": "アー",
            "î": "イー",
            "û": "ウー",
            "ê": "エー",
            "ô": "オー",
            "ka": "カ",
            "ki": "キ",
            "ku": "ク",
            "ke": "ケ",
            "ko": "コ",
            "kâ": "カー",
            "kî": "キー",
            "kû": "クー",
            "kê": "ケー",
            "kô": "コー",
            "sa": "サ",
            "si": "シ",
            "su": "ス",
            "se": "セ",
            "so": "ソ",
            "sâ": "サー",
            "sî": "シー",
            "sû": "スー",
            "sê": "セー",
            "sô": "ソー",
            "ta": "タ",
            "tu": "ト゚",
            "te": "テ",
            "to": "ト",
            "tâ": "ター",
            "tû": "ト゚ー",
            "tê": "テー",
            "tô": "トー",
            "ca": "チャ",
            "ci": "チ",
            "cu": "チュ",
            "ce": "チェ",
            "co": "チョ",
            "câ": "チャー",
            "cî": "チィー",
            "cû": "チュー",
            "cê": "チェー",
            "cô": "チョー",
            "na": "ナ",
            "ni": "ニ",
            "nu": "ヌ",
            "ne": "ネ",
            "no": "ノ",
            "nâ": "ナー",
            "nî": "ニー",
            "nû": "ヌー",
            "nê": "ネー",
            "nô": "ノー",
            "ha": "ハ",
            "hi": "ヒ",
            "hu": "フ",
            "he": "ヘ",
            "ho": "ホ",
            "hâ": "ハー",
            "hî": "ヒー",
            "hû": "フー",
            "hê": "ヘー",
            "hô": "ホー",
            "pa": "パ",
            "pi": "ピ",
            "pu": "プ",
            "pe": "ペ",
            "po": "ポ",
            "pâ": "パー",
            "pî": "ピー",
            "pû": "プー",
            "pê": "ペー",
            "pô": "ポー",
            "ma": "マ",
            "mi": "ミ",
            "mu": "ム",
            "me": "メ",
            "mo": "モ",
            "mâ": "マー",
            "mî": "ミー",
            "mû": "ムー",
            "mê": "メー",
            "mô": "モー",
            "ya": "ヤ",
            "yi": "イ",
            "yu": "ユ",
            "ye": "イェ",
            "yo": "ヨ",
            "yâ": "ヤー",
            "yî": "イー",
            "yû": "ユー",
            "yê": "イェー",
            "yô": "ヨー",
            "ra": "ラ",
            "ri": "リ",
            "ru": "ル",
            "re": "レ",
            "ro": "ロ",
            "râ": "ラー",
            "rî": "リー",
            "rû": "ルー",
            "rê": "レー",
            "rô": "ロー",
            "wa": "ワ",
            "wi": "ヰ",
            "we": "ヱ",
            "wo": "ヲ",
            "wâ": "ワー",
            "wî": "ヰー",
            "wê": "ヱー",
            "wô": "ヲー",
            "nn": "ン",
            "tt": "ッ",
        }.get(remains)
        # ic(converted_remains)

        result += converted_remains or ""

        nucleus = remains[-1] if remains else None

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
            }.get(nucleus or "", "ㇽ"),
            "h": {
                "a": "ㇵ",
                "i": "ㇶ",
                "u": "ㇷ",
                "e": "ㇸ",
                "o": "ㇹ",
            }.get(nucleus or "", "ㇷ"),
            "x": {
                "a": "ㇵ",
                "i": "ㇶ",
                "u": "ㇷ",
                "e": "ㇸ",
                "o": "ㇹ",
            }.get(nucleus or "", "ㇷ"),
        }.get(coda, coda)

        result += converted_coda

        # ic(result)

    if not use_small_i:
        result = result.replace("ィ", "イ")
    if not use_small_u:
        result = result.replace("ゥ", "ウ")
    if not use_small_n:
        result = result.replace("ㇴ", "ン")

    # Replace wi, we, wo
    if not use_wi:
        result = result.replace("ヰ", "ウィ")
    if not use_we:
        result = result.replace("ヱ", "ウェ")
    if not use_wo:
        result = result.replace("ヲ", "ウォ")

    # ic(result)

    return result.replace("’", "")
