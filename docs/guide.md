# chunspell-next guide

## API

Create a spellchecker using the bundled `en_US` dictionary:

```python
from hunspell import Hunspell

spellchecker = Hunspell()
```

Check spelling and request suggestions:

```python
spellchecker.spell("correct")      # True
spellchecker.spell("incorect")     # False
spellchecker.suggest("incorect")   # ("incorrect", "correction", ...)
spellchecker.suffix_suggest("do")  # ("doing", "doth", ...)
```

Stem words and retrieve morphological analysis:

```python
spellchecker.stem("testers")        # ("tester", "test")
spellchecker.analyze("permanently") # (" st:permanent fl:Y",)
```

Add or remove words at runtime:

```python
spellchecker.add("customword")
spellchecker.remove("customword")
```

## Dictionaries

The wheel includes the `en_US` dictionary:

```python
spellchecker = Hunspell("en_US")
```

Load another Hunspell-compatible dictionary from a directory containing its matching `.aff` and `.dic` files:

```python
spellchecker = Hunspell(
    "de_DE",
    hunspell_data_dir="/path/to/dictionaries",
)
```

Load an additional `.dic` file at runtime:

```python
spellchecker.add_dic("/path/to/custom.dic")
```

The `HUNSPELL_DATA` environment variable can provide the default dictionary directory.

## Windows dictionary paths

Dictionary paths containing characters outside the system path encoding or very long paths may require UTF-8 path handling:

```python
spellchecker = Hunspell(
    "de_DE",
    hunspell_data_dir="C:/path/to/dictionaries",
    system_encoding="UTF-8",
)
```

Alternatively, set `HUNSPELL_PATH_ENCODING=UTF-8`.

## Development

Create the development environment and run the tests:

```shell
uv sync --group dev
uv run pytest tests
```

Build a wheel and source distribution:

```shell
uv build
```

After changing `hunspell/hunspell.pyx`, regenerate the checked-in C++ source:

```shell
uv run cython -3 --cplus hunspell/hunspell.pyx
```

Release preparation and tagging are documented in [RELEASING.md](../RELEASING.md).
