# the distance between a node in a Binary Tree and the tree's root is called the node's depth

# write a function that takes in a Binary Tree and returns the sum of its nodes' depths

# NOTES
# we need a counter variable to keep track of the sum
# we can do an in-order traversal and solve the problem recursively

# PSEUDOCODE
# if root is not None:
# return sum + function(root.left, depth + 1) + function(root.right, depth + 1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, sum=0):
    if root is None:
        return 0
    return sum + nodeDepths(root.left, sum + 1) + nodeDepths(root.right, sum + 1)
