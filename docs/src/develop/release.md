# Build and distribute

TODO

### Bump version

Bumping versions workflow:
```
poetry version prepatch  # Idempotent
poetry version prerelease
poetry version patch
poetry version minor
poetry version major
```

If you made a mistake, you can revert the version number:
```
# Reset version
poetry version <expected version>

# Reset to default git version
git checkout paasify.version.py
poetry version $(python -m paasify.version)
```

Yeah, cool, you modified the code, you can rerun the whole test suite described in [Code Development Worklow](#Code-Development-Worklow).

### Build

TODO

Build python package:
```
task build
```


### Release

TODO

## CI/CD

Every CI/CD commands must be able to be launched via `task`. No github actions or whatever vendor specific tasks, everything the CI/CD can do the developer should be able to do so.

However, there are some github configurations and workflow defined into the `.github` project in the project dir.


## Push upstream

WIP

But in your own repo, in your branch. From there, open a pull request on github to have your changes incorporated into the project. And thanks to you for your contribution <3
