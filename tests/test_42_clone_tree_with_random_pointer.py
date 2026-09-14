from helpers import build, load, to_list

clone_random = load("42_clone_tree_with_random_pointer").clone_random


def _nodes(root):
    return [] if root is None else [root] + _nodes(root.left) + _nodes(root.right)


def test_clone_random():
    root = build([1, 2, 3, 4, 5, None, 6])
    n = {node.value: node for node in _nodes(root)}
    n[1].random = n[5]
    n[2].random = n[2]
    n[4].random = n[1]
    n[6].random = n[3]

    clone = clone_random(root)

    assert to_list(clone) == to_list(root)
    originals, copies = _nodes(root), _nodes(clone)
    assert not set(map(id, originals)) & set(map(id, copies))
    mapping = dict(zip(originals, copies))
    for orig, copy in zip(originals, copies):
        assert copy.value == orig.value
        assert copy.random is (mapping[orig.random] if orig.random else None)


def test_clone_random_empty():
    assert clone_random(None) is None
