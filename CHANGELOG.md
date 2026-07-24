# 2.1.0

- Renamed the distribution to `chunspell-next` while keeping `hunspell` as the import package.
- Migrated packaging and development tooling to `pyproject.toml` and uv.
- Added test and wheel coverage for Python 3.13 and 3.14 while retaining wheels for Python 3.8 through 3.12.
- Reworked GitHub Actions for cross-platform testing, tag-based releases, PyPI Trusted Publishing, and GitHub Releases.
- Updated the test suite to use the current API and bundled dictionaries.
- Streamlined the README and moved detailed usage, development, and release documentation into dedicated guides.
- Removed obsolete packaging files, build scripts, and generated-file exclusions.

# 2.0.5

- Forked [`MSeal/cython_hunspell`](https://github.com/MSeal/cython_hunspell) as `chunspell`; see the [full fork comparison](https://github.com/MSeal/cython_hunspell/compare/master...cdhigh:chunspell:master).
- Renamed the distribution from `CyHunspell` to `chunspell`.
- Updated the bundled Hunspell library from 1.7.0 to 1.7.2.
- Removed caching and threaded bulk operations, eliminating the `cacheman` runtime dependency.
- Reduced the bundled dictionaries to an updated `en_US` dictionary while retaining support for custom dictionaries.
- Added automated wheel builds for Linux, Windows, and macOS, plus FreeBSD build support.
- Improved native-library linking and included the Hunspell build helpers in source distributions.

# 2.0.3
- Rebuilt with python 3.10 tested

# 2.0.2
- Removed support for python3.5
- Added support for python3.9

# 2.0.1
- Fixed builds for OSX

# 2.0.0
- Removed support for python 2
- Updated to hunspell 1.7.0
- Added support for `suffix_suggest`
- Added support for `analyze`
- Added support for `add_dic`
- Added support for `remove`
- Added support for `add_with_affix`
- Updated builds to be wheel based
- Moved dictionaries inside hunspell directory structure

# 1.3.3
- Mapped the `add` function to the cython wrapper class.

# 1.3.1 -> 1.3.2
- Fixed dictionary loader to respect locales
- Enabled long file paths to be loaded on windows
- Fixed caching bug which caches results across hunspell instances with different dictionaries.

# 1.3.0
- Fixed build for python 3.7
- Fixed library search issues (> Ubunutu 17)
- Upgraded default hunspell to 1.6.2 for Linux distros

# 1.2.1
- Fixed empty string crash

# 1.2.0
- Fixed detect CPU issue on Linux distros
- Fixed bytes versus unicode conversion for inputs in python2
- Added fix for Python 2.7 on osx
- Added fix for Windows 10 builds

# 1.1.4
- Added Python 3 support

# 1.1.3
- Removed library depdency on cython
- Dropped support for Python 2.6
- Added ability to set concurrency on bulk operations
