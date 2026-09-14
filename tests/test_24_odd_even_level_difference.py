import pytest
from helpers import build, load

odd_even_diff = load("24_odd_even_level_difference").odd_even_diff


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([5, 2, 6, 1, 4, None, 8], 10),
        ([1, 2, 3], -4),
        ([1], 1),
        ([], 0),
    ],
)
def test_odd_even_diff(tree, expected):
    assert odd_even_diff(build(tree)) == expected
