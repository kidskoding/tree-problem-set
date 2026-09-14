from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class TreeNode:
    value: Any
    left: TreeNode | None = None
    right: TreeNode | None = None
    next_right: TreeNode | None = None  # problem 33
    random: TreeNode | None = None  # problem 42
