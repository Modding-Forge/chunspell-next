# chunspell-next

**chunspell-next** is a fast Python interface to [Hunspell](https://hunspell.github.io/), implemented as a native Cython/C++ extension.
This project a fork of [cdhigh/chunspell](https://github.com/cdhigh/chunspell), which is itself a fork of [MSeal/cython_hunspell](https://github.com/MSeal/cython_hunspell). This fork supports current Python versions, provides updated wheels, and uses a modern `uv`-based development and release workflow.

## Installation

```shell
uv add chunspell-next
```

or

```shell
pip install chunspell-next
```

The distribution is named `chunspell-next`; the Python import remains `hunspell`.

## Usage

```python
from hunspell import Hunspell

spellchecker = Hunspell()

spellchecker.spell("correct")     # True
spellchecker.spell("incorect")    # False
spellchecker.suggest("incorect")  # ("incorrect", "correction", ...)
```

The wheel includes the `en_US` dictionary. Custom Hunspell dictionaries can be loaded from another directory.

See the [usage and development guide](docs/guide.md) for dictionaries, the full API, Windows path handling, development setup, and build commands.

## Releases

Tagged releases provide wheels for Linux, macOS, and Windows as well as a source distribution.

See [CHANGELOG.md](CHANGELOG.md) for the project history.

## License

The Python wrapper is licensed under the [MIT License](LICENSE). Bundled Hunspell components use the terms documented in [HUNSPELL_LICENSE_LESSER](HUNSPELL_LICENSE_LESSER).

## About Modding Forge

**chunspell-next** is maintained for the Python tooling powering [Modding Forge](https://moddingforge.com), a community dedicated to Skyrim modding.
