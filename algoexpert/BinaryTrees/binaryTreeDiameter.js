// Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.

// A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes. The length of a path is the number of edges between the path's first node and its last node.

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function binaryTreeDiameter(tree) {
    let di = 0;

    function dfs(node) {
        if (node === null) return 0;

        let left = dfs(node.left);
        let right = dfs(node.right);

        di = Math.max(di, left + right);

        return Math.max(left, right) + 1;
    }

    dfs(tree);

    return di;
}
