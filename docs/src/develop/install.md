# Install

This is a quite complete description of the project developer operations. Obviously, most of those tasks are designed to be run inside a CI/CD


## Install from git

Everything starts with:
```
$ git clone --recurse-submodules git@barbu-it.com:paasify/paasify.git
$ cd paasify
```

If you forgot the `--recurse-submodules`, you can do from inside the git repo:
```
$ git submodule update --init --recursive
```

The you will have to setup a python virtual environment, and install project dependencies


### Build tools

Recommended tools:

* [Poetry](https://python-poetry.org/): Modern Python project management
* [Task](https://taskfile.dev/): MakeFile replacement, useful to run tests, qa or to release.
* [direnv](https://direnv.net/): Allow to enable virtualenv and load environment cars in your shell
* [virtualenv](https://docs.python.org/3/tutorial/venv.html): Manage python virtual env

Troubleshooting:

* [jq](https://stedolan.github.io/jq/): Process JSON files
* [yq](https://mikefarah.gitbook.io/yq/): Process YAML files

!!! info: To see more, check the developper page

### Create virtual environment


#### With direnv

You already have a working direnv? Then review `.envrc` and enable it:

```
$ cd paasify
$ cat .envrc
$ direnv allow
```

#### Manually

You need to create the virtualenv:

```
$ python3 -m .venv
```

Then, each time you get into the project, you will have to source the virtualenv:

```
$ . .venv/bin/activate
```

### Install project build dependencies

Build dependencies are the following:

#### Install task

We install everything inside the virtualenv as the `$PATH` is already set.:

```
$ sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ${VIRTUAL_ENV}/bin
```

#### Install dependencies with task

Once task is installed, it will take care of the rest to do:

```
$ task bootstrap
```

After few minutes, it will have done:

* Install or upgrade poetry
* Install project dependencies and dev dependencies. See here for more informations.

You have now a fully working environment, but `paasify` is not available yet.

!!!  info: you may
     You may need to run this command again if you added or modified project dependencies


### Install paasify

Install paasify itself:

```
task setup
```

!!!  info: you may
     You may need to run this command again if you modified paasify script entry-points. Basically this one only run `poetry install --only-root`.
