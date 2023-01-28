#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# flake8: noqa

# Usual way to call this script: ./gen_apidoc.py src/

# import os
# from pprint import pprint
import os
from distutils.dir_util import copy_tree
import logging

import sh
import click

log = logging.getLogger("mkdocs")
if __name__ == "__main__":
    log = logging.getLogger("gen_apidoc")


#
# Constants
# =============================================

PATH = "./src"
BUILD_DIR_SCHEMA = f"{PATH}/jsonschemas"
BUILD_DIR_DOC = f"{PATH}/refs/config"
BUILD_DIR_RAW = f"{PATH}/refs/raw"
BUILD_DIR_SCHEMA = BUILD_DIR_RAW
ENV = os.environ.copy()
ENV.update(
    {
        "COLUMNS": "82",
    }
)

cli_usage = """
Generate all artifacts for mkdocs after the building. This
script can be both called manually or via the mkdocs-simple-hooks
plugin.

Example:
```
./gen_apidoc.py src/
```

Config definition in `mkdocs.yml`:
```
plugins:
  - mkdocs-simple-hooks:
      hooks:
        #on_post_build: "docs.hooks:copy_logos"
        on_files: "docs.hooks:install_files"
```

The same command is called each time mkdocs is built.

Note: If you edit this script and generate new files, don't forget
      to update .gitignore as well.
"""

#
# Helpers
# =============================================


def get_paasify_pkg_dir():
    """Return the dir where the actual paasify source code lives"""

    # pylint: disable=import-outside-toplevel
    import paasify as _

    return os.path.dirname(_.__file__)


#
# mkdoc API
# =============================================


def copy_logos(*args, **kwargs):
    "Insert logo into the site"

    log.info("Copy logos into project root")
    copy_tree("../logo/", "src/logo")

    # print ("COPY", "../README.md", "src/README.md", os.getcwd())
    # shutil.copy("../README.md", "src/TOTO.md")
    # shutil.copy("../logo/paasify_brand.svg", "paasify_brand.svg")


def gen_cli_usage(*args, **kwargs):
    "Generate cli usage"
    log.info("Generate paasify help output")
    log.info(f"cmd: paasify help")
    sh.paasify("help", _env=ENV, _out=f"{BUILD_DIR_RAW}/cli_usage.txt")


def install_jupyter(*args, **kwargs):
    "Install jupyter bash kernel module"
    log.info("Installing jupyter bash kernel")
    log.info(f"cmd: python -m bash_kernel.install")
    sh.python("-m", "bash_kernel.install")

    # At least, I tried ... lol
    # import bash_kernel
    # bash_kernel.install


def gen_internal_collection(*args, **kwargs):
    "Generate internal collection doc"


    col_path = os.path.join(get_paasify_pkg_dir(), "assets", "collections", "paasify")
    log.info(f"Generate internal collection: {col_path}")
    sh.paasify(
            "document_collection",
            col_path,
            "--out",
            "src/plugins_apidoc",
        )

    return


def gen_schemas(*args, **kwargs):
    "Generate jsonschema"
    log.info("Generate jsonschemas")

    sh.paasify(
            "document_conf",
            "--out",
            "src/paasify_apidoc",
        )

    return

    # for target in SCHEMA_TARGETS:
    #     log.info(
    #         f"Generate schema for {target}: {BUILD_DIR_SCHEMA}/paasify_{target}_schema.*"
    #     )
    #     log.info(f"cmd: paasify schema --format json {target}")
    #     sh.paasify(
    #         "schema",
    #         "--format",
    #         "json",
    #         target,
    #         _out=f"{BUILD_DIR_SCHEMA}/paasify_{target}_schema.json",
    #     )
    #     sh.paasify(
    #         "schema",
    #         "--format",
    #         "yaml",
    #         target,
    #         _out=f"{BUILD_DIR_SCHEMA}/paasify_{target}_schema.yml",
    #     )


# def gen_doc_schemas(*args, **kwargs):
#     "Generate jsonschema"
#     log.info("Generate schema-doc")

#     for target in SCHEMA_TARGETS:
#         for out in ["md", "html"]:
#             log.info(f"Generate schema-doc '{out}' for {target}: in {BUILD_DIR_DOC}")
#             log.info(
#                 f"cmd: generate-schema-doc --config-file doc_schema_{out}.yml {BUILD_DIR_SCHEMA}/paasify_{target}_schema.json {BUILD_DIR_DOC}"
#             )
#             sh.generate_schema_doc(
#                 "--config-file",
#                 f"doc_schema_{out}.yml",
#                 f"{BUILD_DIR_SCHEMA}/paasify_{target}_schema.json",
#                 f"{BUILD_DIR_DOC}",
#             )


# IF set to t

from_env = os.environ.get("FAST")
STATE=False
if from_env == 't':
    STATE=True

# Main hook
def on_files_hook(*args, **kwargs):
    "Pre hook to install everything"
    global STATE

    if STATE:
        log.info("Skip generate scripts, only run at startup!")
        return

    copy_logos()
    gen_cli_usage()
    install_jupyter()
    gen_schemas()
    #gen_doc_schemas()
    gen_internal_collection()
    STATE = True

    log.info("Pre-hooks are all done :)")


#
# Cli
# =============================================

@click.command(help=cli_usage)
@click.argument("path", type=click.Path(exists=True))
def hello(path):
    """
    Hello world!
    """

    if not path:
        raise

    PATH = path
    BUILD_DIR_SCHEMA = f"{PATH}/jsonschemas"
    BUILD_DIR_DOC = f"{PATH}/refs/config"
    BUILD_DIR_RAW = f"{PATH}/refs/raw"
    BUILD_DIR_SCHEMA = BUILD_DIR_RAW

    log = logging.basicConfig(level=logging.INFO)

    click.echo("This script will copy assets into mkdocs dir")
    on_files_hook()
    click.echo("Done!")


if __name__ == "__main__":
    hello()
