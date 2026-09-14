import pytest
from helpers import build, load

max_leaf_to_root_sum = load("23_max_sum_leaf_to_root").max_leaf_to_root_sum


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3], 4),
        ([10, -2, 7, 8, -4], 17),
        ([-5, -3, -10], -8),
        ([-5], -5),
    ],
)
def test_max_leaf_to_root_sum(tree, expected):
    assert max_leaf_to_root_sum(build(tree)) == expected
