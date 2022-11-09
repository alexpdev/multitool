import atexit
import os
import shutil
import string
import sys
from os.path import abspath, dirname, join

import pytest

from multitool import execute
from multitool.__main__ import main
from multitool.runner import Remover
from tests.conf import a, b, c


@pytest.mark.parametrize("val", a)
def test_ord(val):
    """
    Test ord function.
    """
    key, val = val
    sys.argv = ["mtool", "ord", key]
    assert execute() == str(val)


@pytest.mark.parametrize("val", b)
def test_utf(val):
    """
    Test utf function.
    """
    key, val = val
    sys.argv = ["mtool", "utf", str(key)]
    assert execute()


@pytest.mark.parametrize("val", c)
def test_bin(val):
    """
    Test bin function.
    """
    key, val = val
    sys.argv = ["mtool", "bin", str(key)]
    assert execute() == val[2:]


ROOT = join(dirname(abspath(__file__)), "TESTDIR")


@pytest.fixture
def tempdir():
    """
    Temporary test fixture for unit tests.
    """
    root = ROOT
    filler = string.printable + string.whitespace
    if os.path.exists(root):
        shutil.rmtree(root)  # pragma: nocover
    os.mkdir(root)
    sub1 = join(root, "subdir1")
    sub2 = join(root, "subdir2")
    sub3 = join(root, "subdir3")
    sub4 = join(sub2, "subdir1")
    for path in [sub1, sub2, sub3, sub4]:
        os.mkdir(path)
    for i, ext in enumerate([".dat", ".mp4", ".exe"]):
        filename = "file" + str(i) + ext
        with open(join(sub1, filename), "wt", encoding="utf-8") as file_1:
            if ext != ".mp4":
                file_1.write(filler * 10)
    for i, ext in enumerate([".py", ".zip", ".sh"] * 2):
        filename = "file" + str(i) + ext
        with open(join(sub2, filename), "wt", encoding="utf-8") as file_1:
            if ext != ".py":
                file_1.write(filler * 10)
    yield root
    shutil.rmtree(root)


def test_cli_standard(tempdir):
    """
    Test the cli in standard mode.
    """
    sys.argv = ["multitool", "empty", tempdir]
    execute()
    assert not os.path.exists(join(tempdir, "subdir1", "file1.mp4"))
    assert not os.path.exists(join(tempdir, "subdir2", "file0.py"))


def test_cli_standard_with_exclusions(tempdir):
    """
    Test the cli in standard mode with extension exclusions.
    """
    sys.argv = ["multitool", "empty", "--exclude-ext", ".py", tempdir]
    execute()
    exts = [
        os.path.splitext(i)[1] for i in os.listdir(join(tempdir, "subdir2"))
    ]
    assert ".py" in exts


def test_cli_standard_name_exclusions(tempdir):
    """
    Test the cli in standard mode with name exclusions.
    """
    names = ["file1.mp4", "file0.py", "file3.py"]
    sys.argv = ["multitool", "empty", "--exclude-names"] + names + [tempdir]
    execute()
    print(os.listdir(join(tempdir, "subdir1")))
    path = join(tempdir, "subdir1", names[0])
    assert os.path.exists(path)


def test_cli_dirs(tempdir):
    """
    Test the cli in directory mode.
    """
    sys.argv = ["multitool", "empty", "-d", tempdir]
    execute()
    assert not os.path.exists(join(tempdir, "subdir3"))
    assert not os.path.exists(join(tempdir, "subdir2", "subdir1"))


def test_cli_dirs_names_exclusions(tempdir):
    """
    Test the cli in directory mode with name exclusions.
    """
    args = [
        "empty",
        "-d",
        "--exclude-names",
        "subdir1",
        "subdir3",
        tempdir,
    ]
    execute(args)
    assert os.path.exists(join(tempdir, "subdir3"))
    assert os.path.exists(join(tempdir, "subdir2", "subdir1"))


def test_help_message():
    """
    Test generating the help message by default when no args.
    """
    try:
        sys.argv = []
        execute()
    except SystemExit:
        assert True


def test_main_module(tempdir):
    """Test main module."""
    sys.argv = [
        "multitool",
        "empty",
        "-d",
        tempdir,
        "--exclude-name",
        "subdir3",
    ]
    main()
    assert os.path.exists(join(tempdir, "subdir3"))


def test_remover(tempdir):
    """Test remover class."""

    class Namespace:
        """Emulates argparse.namespace"""

        path = [tempdir]
        folders = True
        ex_ext = []
        ex_names = []

    Remover(Namespace)
    assert not os.path.exists(join(tempdir, "subdir3"))
    assert not os.path.exists(join(tempdir, "subdir2", "subdir1"))


@atexit.register
def teardown():
    """
    Teardown any temporary files or directories for testing.
    """
    if os.path.exists(ROOT):
        shutil.rmtree(ROOT)  # pragma: nocover
