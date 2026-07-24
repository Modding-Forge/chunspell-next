# Releasing

## Track changes

Update `CHANGELOG.md` with all significant release changes and update the version in `hunspell/_version.py`.

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

Pushing a `v*` tag starts the release workflow. It runs the tests, builds platform wheels and the source distribution, and publishes all artifacts to PyPI and a GitHub Release.

PyPI Trusted Publishing must be configured once for this repository with `.github/workflows/release.yml` as the workflow and `pypi` as the GitHub environment. No PyPI username or password secret is required.

## Tag the release

Create and push a tag matching the version in `hunspell/_version.py`:

```shell
git tag v<version>
git push origin v<version>
```
