// write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum

// a branch sum is the sum of all the values in a binary tree branch

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function branchSums(root) {
    let sum = []; // will contain the sum of each branch as [a, b, c]

    calculator(root, 0, sum);

    return sum;
};

function calculator(node, currentSum, sums) {
    if (node === null) return 0;
    let newSum = currentSum + node.value;

    if (!node.left && !node.right) {
        sums.push(newSum);
    }

    calculator(node.left, newSum, sums);
    calculator(node.right, newSum, sums);
}
