import pytest
from helpers import build, load

to_dll = load("35_binary_tree_to_dll").to_dll


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 12, 15, 25, 30, 36], [25, 12, 30, 10, 36, 15]),
        ([1, None, 2], [1, 2]),
        ([1], [1]),
    ],
)
def test_to_dll(tree, expected):
    head = to_dll(build(tree))
    assert head.left is None
    forward, node = [], head
    while node.right:
        forward.append(node.value)
        node = node.right
    forward.append(node.value)
    assert forward == expected
    backward = []
    while node:
        backward.append(node.value)
        node = node.left
    assert backward == expected[::-1]


def test_to_dll_empty():
    assert to_dll(None) is None
