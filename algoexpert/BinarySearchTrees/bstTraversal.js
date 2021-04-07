// Write three functions that take in a BST and an empty array, traverse the BST, add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, and post-order tree-traversal techniques, respectively.

// O(n) time complexity, O(n) space complexity

// L N R
function inOrderTraverse(tree, array) {
    if (tree !== null) {
        inOrderTraverse(tree.left, array);
        array.push(tree.value);
        inOrderTraverse(tree.right, array);
    }
    return array;
}

// N L R
function preOrderTraverse(tree, array) {
    if (tree !== null) {
        array.push(tree.value);
        preOrderTraverse(tree.left, array);
        preOrderTraverse(tree.right, array);
    }
    return array;
}

// L R N
function postOrderTraverse(tree, array) {
    if (tree !== null) {
        postOrderTraverse(tree.left, array);
        postOrderTraverse(tree.right, array);
        array.push(tree.value);
    }
    return array;
}
