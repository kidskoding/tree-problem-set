"""01. Height of Binary Tree (GFG, easy)."""

from tree import TreeNode


def height(root: TreeNode | None) -> int:
    if not root:
        return 0

    return 1 + height(root.le)
