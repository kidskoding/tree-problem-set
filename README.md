# tree-problem-set

gfg tree problems for coding interviews!

## Problem Set

Source: [GeeksforGeeks — Tree Coding Problems for Interviews](https://www.geeksforgeeks.org/dsa/top-50-tree-coding-problems-for-interviews/)

### Easy

1. [Height of Binary Tree](src/01_height_of_binary_tree.py) — `tests/test_01_height_of_binary_tree.py`
2. [Identical Trees](src/02_identical_trees.py) — `tests/test_02_identical_trees.py`
3. [Mirror Tree](src/03_mirror_tree.py) — `tests/test_03_mirror_tree.py`
4. [Symmetric Tree](src/04_symmetric_tree.py) — `tests/test_04_symmetric_tree.py`
5. [Balanced Tree](src/05_balanced_tree.py) — `tests/test_05_balanced_tree.py`
6. [Children Sum Parent](src/06_children_sum_parent.py) — `tests/test_06_children_sum_parent.py`
7. [Array to BST](src/07_array_to_bst.py) — `tests/test_07_array_to_bst.py`
8. [Nodes at Given Distance](src/08_nodes_at_given_distance.py) — `tests/test_08_nodes_at_given_distance.py`
9. [Inorder Successor in BST](src/09_inorder_successor_in_bst.py) — `tests/test_09_inorder_successor_in_bst.py`
10. [Kth Largest Element in a BST](src/10_kth_largest_in_bst.py) — `tests/test_10_kth_largest_in_bst.py`
11. [Balance a BST](src/11_balance_a_bst.py) — `tests/test_11_balance_a_bst.py`

### Medium

12. [Diameter of Tree](src/12_diameter_of_tree.py) — `tests/test_12_diameter_of_tree.py`
13. [Check if Subtree](src/13_check_if_subtree.py) — `tests/test_13_check_if_subtree.py`
14. [Check for BST](src/14_check_for_bst.py) — `tests/test_14_check_for_bst.py`
15. [Single Valued Subtree](src/15_single_valued_subtree.py) — `tests/test_15_single_valued_subtree.py`
16. [Unique BSTs](src/16_unique_bsts.py) — `tests/test_16_unique_bsts.py`
17. [Zigzag Tree Traversal](src/17_zigzag_traversal.py) — `tests/test_17_zigzag_traversal.py`
18. [Vertical Traversal](src/18_vertical_traversal.py) — `tests/test_18_vertical_traversal.py`
19. [Boundary Traversal](src/19_boundary_traversal.py) — `tests/test_19_boundary_traversal.py`
20. [Tree from Preorder and Inorder Traversal](src/20_tree_from_preorder_inorder.py) — `tests/test_20_tree_from_preorder_inorder.py`
21. [BST from Preorder Traversal](src/21_bst_from_preorder.py) — `tests/test_21_bst_from_preorder.py`
22. [Minimum Distance Between Two Nodes](src/22_min_distance_between_nodes.py) — `tests/test_22_min_distance_between_nodes.py`
23. [Maximum Sum Leaf to Root Path](src/23_max_sum_leaf_to_root.py) — `tests/test_23_max_sum_leaf_to_root.py`
24. [Odd Even Level Difference](src/24_odd_even_level_difference.py) — `tests/test_24_odd_even_level_difference.py`
25. [Lowest Common Ancestor of a Binary Tree](src/25_lowest_common_ancestor.py) — `tests/test_25_lowest_common_ancestor.py`
26. [Ancestors in Binary Tree](src/26_ancestors_in_binary_tree.py) — `tests/test_26_ancestors_in_binary_tree.py`
27. [Remove BST Keys Outside the Given Range](src/27_remove_bst_keys_outside_range.py) — `tests/test_27_remove_bst_keys_outside_range.py`
28. [Pair with Given Target in BST](src/28_pair_with_target_in_bst.py) — `tests/test_28_pair_with_target_in_bst.py`
29. [BST to Greater Sum Tree](src/29_bst_to_greater_sum_tree.py) — `tests/test_29_bst_to_greater_sum_tree.py`
30. [Maximum Sum of Non-Adjacent Nodes](src/30_max_sum_non_adjacent.py) — `tests/test_30_max_sum_non_adjacent.py`
31. [Largest BST in a Binary Tree](src/31_largest_bst_in_binary_tree.py) — `tests/test_31_largest_bst_in_binary_tree.py`
32. [Extreme Nodes in Alternate Order](src/32_extreme_nodes_alternate.py) — `tests/test_32_extreme_nodes_alternate.py`
33. [Connect Nodes at Same Level](src/33_connect_nodes_same_level.py) — `tests/test_33_connect_nodes_same_level.py`

### Hard

34. [Sorted Linked List to BST](src/34_sorted_list_to_bst.py) — `tests/test_34_sorted_list_to_bst.py`
35. [Binary Tree to Doubly Linked List](src/35_binary_tree_to_dll.py) — `tests/test_35_binary_tree_to_dll.py`
36. [Maximum Sum Path Between Two Leaves](src/36_max_sum_path_between_leaves.py) — `tests/test_36_max_sum_path_between_leaves.py`
37. [K-Sum Paths](src/37_k_sum_paths.py) — `tests/test_37_k_sum_paths.py`
38. [Number of Turns in a Binary Tree](src/38_number_of_turns.py) — `tests/test_38_number_of_turns.py`
39. [Merge Two BSTs](src/39_merge_two_bsts.py) — `tests/test_39_merge_two_bsts.py`
40. [Fixing Two Nodes of a BST](src/40_fix_two_nodes_of_bst.py) — `tests/test_40_fix_two_nodes_of_bst.py`
41. [Burn Binary Tree](src/41_burn_binary_tree.py) — `tests/test_41_burn_binary_tree.py`
42. [Clone Binary Tree with Random Pointer](src/42_clone_tree_with_random_pointer.py) — `tests/test_42_clone_tree_with_random_pointer.py`

## Running tests

```
uv run pytest                                   # everything
nix run .                                       # same, via the flake (optional)
uv run pytest tests/test_01_height_of_binary_tree.py   # one problem
```

`src/tree.py` holds `TreeNode` / `ListNode`. `tests/helpers.py` has `build([...])` (level-order list, `None` = missing node) and `to_list(root)` for writing cases.
