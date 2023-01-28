#!/usr/bin/env pytest
# -*- coding: utf-8 -*-

# MUST READ: https://www.psaggu.com/learning-python/2020/08/10/pfd-pytest-for-devops.html

import os
import time
from pprint import pprint
import logging

import pytest

import yaml
from typer.testing import CliRunner

from paasify.cli import cli_app
from paasify.app import PaasifyApp
import paasify.errors as error

from paasify.common import get_paasify_pkg_dir

log = logging.getLogger()

# Test cli
# ------------------------
cwd = os.path.realpath(os.path.dirname(get_paasify_pkg_dir()))
# cwd is expected to be the paasify root project directory
runner = CliRunner()


# Projects to test
EX_DIR = cwd + "/tests/examples/"

PRJ_MINIMAL = cwd + "/tests/examples/minimal"
PRJ_REAL_TESTS = cwd + "/tests/examples/real_tests"
PRJ_UNIT_SOURCES = cwd + "/tests/examples/unit_sources"
PRJ_UNIT_STACK_IDENTS = cwd + "/tests/examples/unit_stacks_idents"
PRJ_UNIT_STACK_DUP_FAIL = cwd + "/tests/examples/unit_stacks_idents_dup_fail"
PRJ_VAR_MERGE = cwd + "/tests/examples/var_merge"
PRJ_NONE = cwd



# Test things that should fail
#######################################

def test_cli_info_without_project():
    opts = ["-vvvvv", "--config", cwd + "/tests/examples", "info"]
    result = runner.invoke(cli_app, opts)

    out = result.stdout_bytes.decode("utf-8")
    assert result.exit_code != 0


def test_cli_fail_on_outside_project():
    prj_dir = cwd + "/tests/examples/real_tests"
    opts = ["info"]
    result = runner.invoke(cli_app, opts)
    # out = result.stdout_bytes.decode("utf-8")
    pprint (result.__dict__)
    assert result.exit_code != 0 # error.ProjectNotFound.rc



# Test basic commands
#######################################

show_commands = ["explain", "info", "logs", "ls", "ps", "src-ls", "vars"]
cmd_always = ["document_conf", "help"]
cmd_always = ["help"]

@pytest.mark.parametrize('cmd', show_commands)
def test_cli_cmd_inside(cmd):
    opts = ["-c", PRJ_REAL_TESTS, cmd]
    #print ("TESTING", opts)
    #log.error("TESTING: {opts}")
    #time.sleep(1)
    result = runner.invoke(cli_app, opts)


@pytest.mark.parametrize('cmd', show_commands)
def test_cli_cmd_fail_outside(cmd):
    opts = ["-c", PRJ_NONE, cmd]
    result = runner.invoke(cli_app, opts)
    assert result.exit_code != 0

@pytest.mark.parametrize('cmd', cmd_always)
def test_cli_cmd_never_fail(cmd):
    opts = ["-c", PRJ_NONE, cmd]
    result = runner.invoke(cli_app, opts)
    assert result.exit_code == 0


# Test project commands
#######################################


prj = ["real_tests"]

@pytest.mark.parametrize('prj', prj)
def test_cli_cmd_inside_basics(prj):
    base = ["-c", os.path.join(EX_DIR, prj)]

    cmds = ["build", "up", "logs", "ps", "down", "recreate", "apply", "down"]
    for cmd in cmds:
        #time.sleep(1)
        #print ("YOLOO", base + [cmd])
        result = runner.invoke(cli_app, base + [cmd])
        assert result.exit_code == 0
