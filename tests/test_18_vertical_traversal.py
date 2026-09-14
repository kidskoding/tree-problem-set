import pytest
from helpers import build, load

vertical_order = load("18_vertical_traversal").vertical_order


@pytest.mark.parametrize(
    "tree, expected",
    [
        (
            [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9],
            [[4], [2], [1, 5, 6], [3, 8], [7], [9]],
        ),
        ([1, 2, 3, None, 4, 5], [[2], [1, 4, 5], [3]]),  # same column+level: level order
        ([1], [[1]]),
        ([], []),
    ],
)
def test_vertical_order(tree, expected):
    assert vertical_order(build(tree)) == expected
