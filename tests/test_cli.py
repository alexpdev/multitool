import pytest
from multitool import execute


@pytest.fixture
def contains():
    args = ["multitool", "--count", "50", "--in"]
    return args


@pytest.mark.parametrize("text", ["tem", "ous", "fall", "odio"])
def test_execute(contains, text):
    contains.append(text)
    assert execute(contains)
