# write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum

# a branch sum is the sum of all values in a BT branch.

# NOTES
# we need to go down each branch and add the values for each node
# there are three types of traversals
# we can focus on in-order traversal

# PSEUDOCODE
# create a sums variable containing an empty list


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    pass
