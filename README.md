# tree-problem-set

gfg tree problems for coding interviews!

## Problem Set

Source: [GeeksforGeeks — Tree Coding Problems for Interviews](https://www.geeksforgeeks.org/dsa/top-50-tree-coding-problems-for-interviews/)

### Easy

1. [Height of Binary Tree](https://www.geeksforgeeks.org/dsa/find-the-maximum-depth-or-height-of-a-tree/)
2. [Identical Trees](https://www.geeksforgeeks.org/dsa/write-c-code-to-determine-if-two-trees-are-identical/)
3. [Mirror Trees](https://www.geeksforgeeks.org/dsa/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/)
4. [Symmetric Trees](https://www.geeksforgeeks.org/dsa/symmetric-tree-tree-which-is-mirror-image-of-itself/)
5. [Balanced tree](https://www.geeksforgeeks.org/dsa/how-to-determine-if-a-binary-tree-is-balanced/)
6. [Children Sum Parent](https://www.geeksforgeeks.org/dsa/check-for-children-sum-property-in-a-binary-tree/)
7. [Array to BST](https://www.geeksforgeeks.org/dsa/sorted-array-to-balanced-bst/)
8. [Nodes at given distance](https://www.geeksforgeeks.org/dsa/print-nodes-distance-k-given-node-binary-tree/)
9. [Inorder Successor in BST](https://www.geeksforgeeks.org/dsa/inorder-successor-in-binary-search-tree/)
10. [Kth Largest Element in a BST](https://www.geeksforgeeks.org/dsa/kth-largest-element-bst-using-constant-extra-space/)
11. [Balance a BST](https://www.geeksforgeeks.org/dsa/convert-normal-bst-balanced-bst/)

### Medium

12. [Diameter of Tree](https://www.geeksforgeeks.org/dsa/diameter-of-a-binary-tree/)
13. [Check if Subtree](https://www.geeksforgeeks.org/dsa/check-if-a-binary-tree-is-subtree-of-another-binary-tree/)
14. [Check for BST](https://www.geeksforgeeks.org/dsa/a-program-to-check-if-a-binary-tree-is-bst-or-not/)
15. [Single Valued Subtree](https://www.geeksforgeeks.org/dsa/find-count-of-singly-subtrees/)
16. [Unique BSTs](https://www.geeksforgeeks.org/dsa/number-of-unique-bst-with-a-given-key-dynamic-programming/)
17. [Zigzag Tree Traversal](https://www.geeksforgeeks.org/dsa/zigzag-tree-traversal/)
18. [Vertical Traversal](https://www.geeksforgeeks.org/dsa/vertical-order-traversal-of-binary-tree-using-map/)
19. [Boundary Traversal](https://www.geeksforgeeks.org/dsa/boundary-traversal-of-binary-tree/)
20. [Tree from Preorder and Inorder Traversal](https://www.geeksforgeeks.org/dsa/construct-tree-from-given-inorder-and-preorder-traversal/)
21. [BST from preorder traversal](https://www.geeksforgeeks.org/dsa/construct-bst-from-given-preorder-traversa/)
22. [Minimum distance between two nodes](https://www.geeksforgeeks.org/dsa/find-distance-between-two-nodes-of-a-binary-tree/)
23. [Maximum sum leaf to root path](https://www.geeksforgeeks.org/dsa/find-the-maximum-sum-path-in-a-binary-tree/)
24. [Odd Even Level Difference](https://www.geeksforgeeks.org/dsa/difference-between-sums-of-odd-and-even-levels/)
25. [Lowest Common Ancestor of a Binary Tree](https://www.geeksforgeeks.org/dsa/lowest-common-ancestor-binary-tree-set-1/)
26. [Ancestors in Binary Tree](https://www.geeksforgeeks.org/dsa/print-ancestors-of-a-given-node-in-binary-tree/)
27. [Remove BST keys outside the given range](https://www.geeksforgeeks.org/dsa/remove-bst-keys-outside-the-given-range/)
28. [Pair with given target in BST](https://www.geeksforgeeks.org/dsa/find-a-pair-with-given-sum-in-bst/)
29. [BST to greater sum tree](https://www.geeksforgeeks.org/dsa/transform-bst-sum-tree/)
30. [Maximum sum of non adjacent](https://www.geeksforgeeks.org/dsa/maximum-sum-nodes-binary-tree-no-two-adjacent/)
31. [Largest BST in a Binary Tree](https://www.geeksforgeeks.org/dsa/largest-bst-binary-tree-set-2/)
32. [Extreme nodes in alternate order](https://www.geeksforgeeks.org/dsa/print-extreme-nodes-of-each-level-of-binary-tree-in-alternate-order/)
33. [Connect nodes at same level](https://www.geeksforgeeks.org/dsa/connect-nodes-at-same-level/)

### Hard

34. [Sorted Linked List to BST](https://www.geeksforgeeks.org/dsa/sorted-linked-list-to-balanced-bst/)
35. [Binary Tree to Doubly Linked List](https://www.geeksforgeeks.org/dsa/convert-binary-tree-to-doubly-linked-list-by-keeping-track-of-visited-node/)
36. [Maximum sum path between two leaves](https://www.geeksforgeeks.org/dsa/find-maximum-path-sum-two-leaves-binary-tree/)
37. [K-Sum Paths](https://www.geeksforgeeks.org/dsa/count-all-k-sum-paths-in-a-binary-tree/)
38. [Number of turns in a binary tree](https://www.geeksforgeeks.org/dsa/number-turns-reach-one-node-binary-tree/)
39. [Merge two BST’s](https://www.geeksforgeeks.org/dsa/merge-two-bsts-with-limited-extra-space/)
40. [Fixing two nodes of a BST](https://www.geeksforgeeks.org/dsa/fix-two-swapped-nodes-of-bst/)
41. [Burn Binary Tree](https://www.geeksforgeeks.org/dsa/burn-the-binary-tree-starting-from-the-target-node/)
42. [Clone binary tree with random pointer](https://www.geeksforgeeks.org/dsa/clone-binary-tree-random-pointers/)

## Running tests

```
uv run pytest                                   # everything
nix run .                                       # same, via the flake (optional)
uv run pytest tests/test_01_height_of_binary_tree.py   # one problem
```

`src/tree.py` holds `TreeNode`. `tests/helpers.py` has `build([...])` (level-order list, `None` = missing node) and `to_list(root)` for writing cases.
