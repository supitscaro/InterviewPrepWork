// Write a function that take in a potentially invalid BST and returns a boolean representing whether the BST is valid.

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function validateBST(node) {
    return isValid(node, -Infinity, Infinity); // left is < node, right > node
};

function isValid(node, min, max) {
    if (node === null) return true;

    if (node.value < min || node.value >= max) {
        return false;
    }
    // node   min   max
    let left = isValid(node.left, min, node.value);
    let right = isValid(node.right, max, node.value);

    return left && right;
}
