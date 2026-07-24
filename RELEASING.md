# Releasing

## Track changes

Update `CHANGELOG.md` with all significant release changes and update the
version in `hunspell/_version.py`.

## Rebuild the generated extension source

Create the development environment and regenerate the checked-in C++ source:

```shell
uv sync --group dev
uv run cython -3 --cplus hunspell/hunspell.pyx
uv run pytest tests
```

Commit the regenerated `hunspell/hunspell.cpp` when it changed.

## Build distributions

Build the source distribution and a wheel through the PEP 517 backend:

```shell
uv build
```

The platform wheel workflow can also be started manually in GitHub Actions.
It stores all wheels and the source distribution as workflow artifacts.

## Tag the release

Create and push a tag matching the version in `hunspell/_version.py`:

```shell
git tag v<version>
git push origin v<version>
```
