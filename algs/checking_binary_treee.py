# The task was taken from
# https://www.youtube.com/watch?v=i_Q0v_Ct5lY
#

from binarytree import tree
from binarytree import Node


def check_tree(root_node, min_v=float('-inf'), max_v=float('inf')):
    if root_node is None:
        return True

    value = root_node.value

    if not min_v < value < max_v:
        return False

    """"""
    if root_node.left and root_node.left.value > value:
        return False
    if root_node.right and root_node.right.value < value:
        return False

    return check_tree(root_node.left, min_v=min_v, max_v=value) \
           and check_tree(root_node.right, min_v=value, max_v=max_v)


# create random binary tree
non_sorted_tree = tree(height=3, is_perfect=False)
print(non_sorted_tree)

result = check_tree(non_sorted_tree)
print('Non sorted tree:', result)

# Build the new tree from the example in the video:
sorted_tree = Node(50)
sorted_tree.left = Node(10)
sorted_tree.right = Node(80)
sorted_tree.left.left = Node(5)
sorted_tree.left.right = Node(30)
sorted_tree.left.right.left = Node(20)
sorted_tree.left.right.left = Node(40)
sorted_tree.right.left = Node(70)
sorted_tree.right.right = Node(90)
sorted_tree.right.right.left = Node(85)

print(sorted_tree)

# Check it
result = check_tree(sorted_tree)
print('Example tree:', result)


# Create little correct binary search tree:
small_tree = Node(100)
small_tree.left = Node(50)
small_tree.right = Node(110)
small_tree.left.left = Node(1)
small_tree.left.right = Node(55)
print(small_tree)

# Check it
result = check_tree(small_tree)
print('Correct example tree:', result)
