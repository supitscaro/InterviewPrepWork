# write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum

# a branch sum is the sum of all values in a BT branch.

# NOTES
# we need to go down each branch and add the values for each node
# there are three types of traversals
# we can focus on in-order traversal

# PSEUDOCODE
# create a sums variable containing an empty list
# create a helper function

# helper function:
# should take the root, starting sum = 0, and sums
# current_sum = starting sum + node.value
# solve this recursively so,
# if root is None:
# return
# if node.left is None and node.right is None:
# sums.append(node)

# helper function(node.left, current_sum, sums)
# helper function(node.right, current_sum, sums)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []

    return branchSumsHelper(root, 0, sums)


def branchSumsHelper(node, starting_sum, sums):
    if node is not None:
        return

    current_sum = starting_sum + node.value

    if node.left is None and node.right is None:
        sums.append(current_sum)
        return

    branchSumsHelper(node.left, current_sum, sums)
    branchSumsHelper(node.right, current_sum, sums)
