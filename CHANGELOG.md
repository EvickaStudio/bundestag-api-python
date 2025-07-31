# Changelog

## 0.1.0-alpha.1 (2025-07-31)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/EvickaStudio/bundestag-api-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* clean up environment call outs ([d3ab06b](https://github.com/EvickaStudio/bundestag-api-python/commit/d3ab06bd27aab5b6bfad9de3c23a67007a98e169))
* **client:** add follow_redirects request option ([8e00daa](https://github.com/EvickaStudio/bundestag-api-python/commit/8e00daa6499ad1a1abe75fcbff63f334486ad2e9))
* **client:** add support for aiohttp ([090fca6](https://github.com/EvickaStudio/bundestag-api-python/commit/090fca6eeee4e1332873ace2b0919305f895e2f7))
* **client:** support file upload requests ([011729d](https://github.com/EvickaStudio/bundestag-api-python/commit/011729d8c16d5ad49d730d546fdc177995fbc3ff))


### Bug Fixes

* **ci:** correct conditional ([6df4c8e](https://github.com/EvickaStudio/bundestag-api-python/commit/6df4c8eca8a95e796897e75fab20a0b08a8ad1b7))
* **ci:** release-doctor — report correct token name ([5ea89c6](https://github.com/EvickaStudio/bundestag-api-python/commit/5ea89c6ef1e6038fad75fe5026972b1d78a469c2))
* **client:** correctly parse binary response | stream ([c2520dd](https://github.com/EvickaStudio/bundestag-api-python/commit/c2520ddb7ca4e14549253c37e628eef882adc0c6))
* **client:** don't send Content-Type header on GET requests ([a3256f1](https://github.com/EvickaStudio/bundestag-api-python/commit/a3256f14a4a5b14ab0ea4216ae2626c62e59d64c))
* **parsing:** correctly handle nested discriminated unions ([6e8c0b3](https://github.com/EvickaStudio/bundestag-api-python/commit/6e8c0b3620d06de465d168afac736df476c4a8ba))
* **parsing:** ignore empty metadata ([3641cfc](https://github.com/EvickaStudio/bundestag-api-python/commit/3641cfce3651f27968765956908551e8a3555169))
* **parsing:** parse extra field types ([3c251a1](https://github.com/EvickaStudio/bundestag-api-python/commit/3c251a1562d7702c745b2fbc0f63ccf2a3c55daf))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([12ea00e](https://github.com/EvickaStudio/bundestag-api-python/commit/12ea00e35238acddd3b0aa9540d688d08a242bc4))


### Chores

* change publish docs url ([a51829c](https://github.com/EvickaStudio/bundestag-api-python/commit/a51829c756cff100dfa3f6d46557fb257aec4da8))
* **ci:** change upload type ([ad69e0e](https://github.com/EvickaStudio/bundestag-api-python/commit/ad69e0eae61ef0947473cf16e658a809948d85a0))
* **ci:** enable for pull requests ([a2d3354](https://github.com/EvickaStudio/bundestag-api-python/commit/a2d33541e7de9ec83bf4023631cc2544f1909992))
* **ci:** only run for pushes and fork pull requests ([e56a1cc](https://github.com/EvickaStudio/bundestag-api-python/commit/e56a1cc7de09c931e1f59b47882f1006c70bd4d6))
* **docs:** remove unnecessary param examples ([48b0d54](https://github.com/EvickaStudio/bundestag-api-python/commit/48b0d549322ac8485ff0ae92b0e2614082b26a37))
* **internal:** bump pinned h11 dep ([c4f3f26](https://github.com/EvickaStudio/bundestag-api-python/commit/c4f3f26d0a2f776bb3d3c9aae9972d500d3f6886))
* **internal:** codegen related update ([ac88670](https://github.com/EvickaStudio/bundestag-api-python/commit/ac88670ecbccf815920d98284c3fb9fc5bb06195))
* **internal:** update conftest.py ([99b4f93](https://github.com/EvickaStudio/bundestag-api-python/commit/99b4f93ce87866dfea0bf59e5fcf39b495c7420f))
* **package:** mark python 3.13 as supported ([95cbbc2](https://github.com/EvickaStudio/bundestag-api-python/commit/95cbbc2402c2750dbeeaf6c063aa4620238a9792))
* **project:** add settings file for vscode ([e643a5e](https://github.com/EvickaStudio/bundestag-api-python/commit/e643a5ecc9bf2f4e1b5c5229843c0b6cff7c090b))
* **readme:** fix version rendering on pypi ([947b4f4](https://github.com/EvickaStudio/bundestag-api-python/commit/947b4f495e35fb4a409863bfa121c92d22ffc335))
* **readme:** update badges ([07558e3](https://github.com/EvickaStudio/bundestag-api-python/commit/07558e385dddb5b061a3315694ed84f36e5ce35e))
* **tests:** add tests for httpx client instantiation & proxies ([7414177](https://github.com/EvickaStudio/bundestag-api-python/commit/74141773a4ad77c44c8ac73a886c427e2ddbb168))
* **tests:** run tests in parallel ([c8bf6ca](https://github.com/EvickaStudio/bundestag-api-python/commit/c8bf6cabec0d137c284fa649d64ad84c9f0c2d2c))
* **tests:** skip some failing tests on the latest python versions ([a33ab7c](https://github.com/EvickaStudio/bundestag-api-python/commit/a33ab7c8f0239c9752a0b08d16652896f1041457))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([0e4c1cf](https://github.com/EvickaStudio/bundestag-api-python/commit/0e4c1cf7d0e3a27440a66a2cf6cff1d7266f58ee))

## 0.0.1-alpha.1 (2025-06-02)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/EvickaStudio/bundestag-api-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* update SDK settings ([9da8004](https://github.com/EvickaStudio/bundestag-api-python/commit/9da800420e91bc9bbbaead8ed26e370b509fb4f6))
