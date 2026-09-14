import pytest
from helpers import build, load

zigzag = load("17_zigzag_traversal").zigzag


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7]),
        ([7, 9, 7, 8, 8, 6, None, 10, 9], [7, 7, 9, 8, 8, 6, 9, 10]),
        ([1], [1]),
        ([], []),
    ],
)
def test_zigzag(tree, expected):
    assert zigzag(build(tree)) == expected
