from helpers import build, find, load

connect_same_level = load("33_connect_nodes_same_level").connect_same_level


def _levels_via_next_right(root):
    """Walk each level using next_right, starting from the leftmost node."""
    out = []
    while root:
        row, node = [], root
        while node:
            row.append(node.value)
            node = node.next_right
        out.append(row)
        root = root.left or root.right
    return out


def test_connect_same_level():
    root = build([10, 20, 30, 40, 60])
    connect_same_level(root)
    assert _levels_via_next_right(root) == [[10], [20, 30], [40, 60]]
    assert root.next_right is None
    assert find(root, 30).next_right is None


def test_connect_same_level_across_subtrees():
    root = build([1, 2, 3, 4, None, None, 5, 6, None, None, 7])
    connect_same_level(root)
    assert find(root, 4).next_right is find(root, 5)
    assert find(root, 6).next_right is find(root, 7)
    assert find(root, 7).next_right is None
    connect_same_level(None)
