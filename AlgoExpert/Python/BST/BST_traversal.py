# write three functions that take in a BST and an empty array,
# traverse the BST, add its nodes' values to the input array,
# and return that array

# the three functions should traverse the BST using in-order,
# pre-order, post-order


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
    return array
