// the distance between a node in a Binary Tree and the tree's root is called the node's depth

// write a function that takes in a binary tree and returns the sum of its nodes' depths.


class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function nodeDepths(node, depth = 0) {
    if (node === null) return 0;

    let res = nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1);

    return depth + res;
}
