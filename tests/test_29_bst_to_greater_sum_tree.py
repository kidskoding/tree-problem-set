from helpers import build, load, to_list

to_greater_sum_tree = load("29_bst_to_greater_sum_tree").to_greater_sum_tree


def test_to_greater_sum_tree():
    root = build([11, 2, 29, 1, 7, 15, 40, None, None, None, None, None, None, 35])
    to_greater_sum_tree(root)
    assert to_list(root) == [119, 137, 75, 139, 130, 104, 0, None, None, None, None, None, None, 40]


def test_to_greater_sum_tree_small():
    root = build([2, 1, 3])
    to_greater_sum_tree(root)
    assert to_list(root) == [3, 5, 0]
    to_greater_sum_tree(None)
