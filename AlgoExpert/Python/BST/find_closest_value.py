# write a function that takes in a BST and a target integer value and returns the closest value to that target value contained in the BST

# you can assume there will only be one closest value

# INPUTS/OUTPUTS
"""
tree =        10
            /    \
           5     15
         /  \   /  \
        2    5 13  22
       /         \
      1           14

target = 12
"""

# output => 13


def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, tree.value)


def findClosestValueHelper(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return current_node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
