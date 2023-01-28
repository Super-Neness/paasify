# Introduction

This is a quite complete description of the project developer operations. Obviously, most of those tasks are designed to be run inside a CI/CD

This section introduces how Paasify is developped and which process are in place.

* This page give an overview of the Paasify environment
* The second section explains how to [install Paasify in development mode](/paasify/develop/install/)
* The third section explains how to [modify Paasify source code](/paasify/develop/contribute/)
* The fourth section explains how to [update documentation](/paasify/develop/docs/)
* The last section explains how to [build and release](/paasify/develop/release/)


## Dependencies overview

List of main dependencies:

* Paasify dependencies
    * `Typer`: Command line handling
    * `jsonnet`: Jsonnet parsing
    * `sh`: Easy library to execute shell commands
    * `jsonschema`: handle jsonscheme specs
    * `anyconfig`: load any configs
* Develop dependencies
    * General
        * `poetry`: manage python project and dependencies
        * `commitizen`: ensure commit respect standards
        * `pytest`: test the code is not broken
        * `pylint`: test the code is always first quality
        * `black`: test the code is always perfectly formatted
        * `pre-commit`: prevent you to commit too early
    * Documentation (optional)
        * `mkdocs`: Project documentation website
        * `mike`: manage many version of mkdocs
        * `jupyter`: generate docs from commands
    * Docker (optional)
    * Other
        * `jq`: threat json data
        * `yq`: same as jq but for yaml
        * `task`: `make` alternative

## Workflow

Each commit should ideally contains:

1. code
1. tests
1. documentation
2. commit message

This is the general workflow:

1. Code Development
    * Update the code
    * Update the tests
    * Update the doc
    * Update release
        * Generate release notes
2. Documentation:
    * Generate jsonschema documentation
    * Generate mkdocs:
        * Include other files of the project
        * Import jsonschema documentation
        * Generate python code reference
3. Code Quality:
    * Run autolinter `black`
    * Run linting report `pylint`
    * Run tests:
        * Run unit tests
        * Run code-coverage
        * Run functional tests
        * Run examples tests
4. Delivery:
    * Documentation:
        * Build static documentation
    * Release Pypi:
        * Build package
        * Push package
    * Release Container:
        * Build Docker Build env
        * Build Paasify App Image
        * Build Paasify Documentation Image
        * Push images
5. Contributing:
    * Create a git commit
    * Create a pull request
    * Review of the commit
    * Merge to upstream if accepted

Once you developed or changed things, you need to test
