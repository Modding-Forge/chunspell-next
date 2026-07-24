from pathlib import Path
from shutil import copyfile

import pytest

from hunspell import Hunspell, HunspellFilePathError


DICT_DIR = Path(__file__).parent.parent / "hunspell" / "dictionaries"


@pytest.fixture
def hunspell():
    return Hunspell("en_US", hunspell_data_dir=str(DICT_DIR))


def test_create_with_bundled_dictionary():
    hunspell = Hunspell()

    assert hunspell.lang == "en_US"
    assert hunspell.spell("test")


def test_missing_dictionary_raises_path_error():
    with pytest.raises(HunspellFilePathError, match="not_available"):
        Hunspell("not_available", hunspell_data_dir=str(DICT_DIR))


def test_unicode_dictionary_path(tmp_path):
    dictionary_dir = tmp_path / "wörterbücher"
    dictionary_dir.mkdir()
    copyfile(DICT_DIR / "en_US.aff", dictionary_dir / "en_US.aff")
    copyfile(DICT_DIR / "en_US.dic", dictionary_dir / "en_US.dic")

    hunspell = Hunspell(
        "en_US",
        hunspell_data_dir=str(dictionary_dir),
        system_encoding="UTF-8",
    )

    assert hunspell.spell("test")


def test_add_dictionary(hunspell, tmp_path):
    dictionary = tmp_path / "custom.dic"
    dictionary.write_text("1\ncodexuniqueword\n", encoding="utf-8")

    assert not hunspell.spell("codexuniqueword")
    assert hunspell.add_dic(str(dictionary)) == 0
    assert hunspell.spell("codexuniqueword")


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("test", True),
        ("correct", True),
        ("incorect", False),
        ("café", True),
        ("uncafé", False),
        ("", True),
    ],
)
def test_spell(hunspell, word, expected):
    assert hunspell.spell(word) is expected


def test_spell_rejects_bytes(hunspell):
    with pytest.raises(TypeError):
        hunspell.spell(b"test")


def test_suggest(hunspell):
    suggestions = hunspell.suggest("incorect")

    assert isinstance(suggestions, tuple)
    assert suggestions[0] == "incorrect"
    assert "correction" in suggestions


def test_suggest_unicode(hunspell):
    assert "café" in hunspell.suggest("cefé")


def test_suggest_empty(hunspell):
    assert hunspell.suggest("") == ()


def test_suffix_suggest(hunspell):
    assert hunspell.suffix_suggest("do") == (
        "doing",
        "doth",
        "doer",
        "doings",
        "doers",
        "doest",
    )


def test_suffix_suggest_unicode(hunspell):
    assert set(hunspell.suffix_suggest("café")) == {"cafés", "café's"}


def test_suffix_suggest_empty(hunspell):
    assert hunspell.suffix_suggest("") == ()


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("dog", ("dog",)),
        ("testers", ("tester", "test")),
        ("saves", ("save",)),
        ("permanently", ("permanent",)),
    ],
)
def test_stem(hunspell, word, expected):
    assert hunspell.stem(word) == expected


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("dog", (" st:dog",)),
        ("permanently", (" st:permanent fl:Y",)),
    ],
)
def test_analyze(hunspell, word, expected):
    assert hunspell.analyze(word) == expected


def test_add(hunspell):
    word = "outofvocabularyword"

    assert not hunspell.spell(word)
    assert hunspell.add(word) == 0
    assert hunspell.spell(word)
    assert word in hunspell.suggest(word + "d")


def test_add_with_affix(hunspell):
    word = "outofvocabularyword"

    assert not hunspell.spell(word)
    assert hunspell.add_with_affix(word, "example") == 0
    assert hunspell.spell(word)
    assert word in hunspell.suggest(word + "d")


def test_remove(hunspell):
    assert hunspell.spell("dog")
    assert hunspell.remove("dog") == 0
    assert not hunspell.spell("dog")


@pytest.mark.parametrize(
    ("action", "word"),
    [
        ("spell", "test"),
        ("suggest", "incorect"),
        ("stem", "testers"),
        ("analyze", "permanently"),
        ("suffix_suggest", "do"),
    ],
)
def test_action_dispatch(hunspell, action, word):
    expected = getattr(hunspell, action)(word)

    assert hunspell.action(action, word) == expected


def test_action_add_and_remove(hunspell):
    word = "actionword"

    assert hunspell.action("add", word) == 0
    assert hunspell.spell(word)
    assert hunspell.action("remove", word) == 0
    assert not hunspell.spell(word)


def test_action_rejects_unknown_action(hunspell):
    with pytest.raises(ValueError, match="Unexpected action"):
        hunspell.action("unknown", "test")
