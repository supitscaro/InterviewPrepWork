// Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function invertBinaryTree(tree) {
    if (tree === null) return root;

    function dfs(node) {
        [node.left, node.right] = [node.right, node.left];
        if (node.left) dfs(node.left);
        if (node.right) dfs(node.right);
    }

    dfs(tree);
    return tree;
}
