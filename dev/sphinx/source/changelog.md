# lucit-licensing-python Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

[Discussions about lucit-licensing-python releases!](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/discussions/categories/releases)

[How to upgrade to the latest version!](https://lucit-licensing-python.docs.lucit.tech/readme.html#installation-and-upgrade)

## 1.8.2.dev (development stage/unreleased/unstable)

## 1.8.2
`lucit-licensing-python` can now also be installed on all architectures on which there are no precompiled packages from 
LUCIT. PIP now automatically recognises whether there is a suitable precompiled package and if not, the source is 
automatically compiled on the target system during the installation process with Cython. Even if you don't have to do 
anything special, please note that this process takes some time!

## 1.8.1
### Fixed
- Typing of `manager.__init__()` parameters

## 1.8.0
- Building conda packages and distribute them via https://anaconda.org/lucit

## 1.7.0
### Changed
- Removed calls `sys.exit()` calls in `manager.py`
- Using `try-except`-blocks in `cli.py`

## 1.6.0
### Changed
- Exceptions are now forwarded to the parent class and be raised there to be catchable in spite of threads and asyncio.

## 1.5.4
### Fixed
- Raising `NoValidatedLucitLicense` moved to main thread 

## 1.5.3
### Fixed
- Using `sys.exit()` for cli and exception `NoValidatedLucitLicense` for non cli calls.

## 1.5.2
### Changed
- Handling of unexpected license result in `manager.run()`.

## 1.5.1
### Changed 
- Using `dict.get()` instead of `try` in `manager.run()`.

## 1.5.0
## Added
- Logging the used license profile with debug level `INFO`.
- `pyproject.toml` now ready for poetry
- Support for `with`-context
### Fixed
- Raising exceptions in specific situations

## 1.4.1
### Changed
- Text and Link if no license provided.

## 1.4.0
### Added
- Parameter `license_ini` and `license_profile` to `LucitLicensingManager()`
- Parameter `--licenseini` and `--licenseprofile` to CLI
- Load license from file by default if no license provided via parameter.

## 1.3.0
### Added
- `--info` and `--reset` parameter to `lucitlicmgr`

## 1.2.0
### Added
- Commandline Interface `lucitlicmgr`

## 1.1.9
- RELEASE!!! :)
