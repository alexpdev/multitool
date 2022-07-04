import sys
import pytest

from tests.conf import a, b, c
from multitool import execute




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
