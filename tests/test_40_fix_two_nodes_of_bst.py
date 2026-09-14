import pytest
from helpers import build, load, to_list

fix_bst = load("40_fix_two_nodes_of_bst").fix_bst


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 5, 8, 2, 20], [10, 5, 20, 2, 8]),
        ([1, 3, None, None, 2], [3, 1, None, None, 2]),  # adjacent in inorder
        ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
        ([20, 8, 22, 4, 12, None, None, None, None, 14, 10], [20, 8, 22, 4, 12, None, None, None, None, 10, 14]),
    ],
)
def test_fix_bst(tree, expected):
    root = build(tree)
    fix_bst(root)
    assert to_list(root) == expected
