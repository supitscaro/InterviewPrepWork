// Write a function that takes in a BST and a target integer value and returns the closest value to that target value contained in the BST.

// you can assume that there will only be one closest value

function findClosestValueInBst(tree, target) {
    return helper(tree, target, tree.value);
}

function helper(tree, target, closest) {
    if (tree === null) return closest;
    // if target val is farther from closest than it is to tree.value then we update closest to = tree.value;
    if (Math.abs(target - closest) > Math.abs(target - tree.value)) {
        closest = tree.value;
    }
    if (target > tree.value) {
        return helper(tree.left, target, closest);
    } else if (target < tree.value) {
        return helper(tree.right, target, closest);
    } else {
        return closest;
    }
}
