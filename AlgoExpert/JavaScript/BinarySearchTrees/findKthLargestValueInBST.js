// write a function that takes in a BST and a positive integer k and returns the kth largest integer contained in the BST

// you can assume that there will only be integer values in the BST and that k is less than or equal to the number of nodes in the tree

// possibly need to do DFS

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function findKthLargestValue(tree, k) {
    let sorted = [];

    inOrderTraverse(tree, sorted);

    return sorted[sorted.length - k];
};

// if we do in order traversal, we can create an array that will store the nodes in ascending order, allowing us to then find the kth largest number by doing sorted.length - k
function inOrderTraverse(node, sorted) {
    if (node === null) return;

    inOrderTraverse(node.left, sorted);
    sorted.push(node.value);
    inOrderTraverse(node.right, sorted);
};
