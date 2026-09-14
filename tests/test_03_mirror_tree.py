from helpers import build, load, to_list

mirror = load("03_mirror_tree").mirror


def test_mirror():
    root = build([1, 2, 3, 4, 5])
    mirror(root)
    assert to_list(root) == [1, 3, 2, None, None, 5, 4]


def test_mirror_twice_restores():
    root = build([1, 2, None, 3, 4])
    mirror(root)
    mirror(root)
    assert to_list(root) == [1, 2, None, 3, 4]
    mirror(None)
