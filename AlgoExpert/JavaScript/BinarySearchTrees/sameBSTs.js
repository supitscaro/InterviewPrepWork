// An array of integers is said to represent the BST obtained by inserting each integer in the array, from left to right, into the BST.

// Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST. Note that you're not allowed to construct any BSTs in your code.

function sameBSTs(arrayOne, arrayTwo) {
    if (arrayOne.length !== arrayTwo.length) return false;

    if (arrayOne.length === 0 && arrayTwo.length === 0) return true;

    if (arrayOne[0] !== arrayTwo[0]) return false;

    let leftOne = getSmaller(arrayOne);
    let leftTwo = getSmaller(arrayTwo);

    let rightOne = getBiggerOrEqual(arrayOne);
    let rightTwo = getBiggerOrEqual(arrayTwo);

    return sameBSTs(leftOne, leftTwo) && sameBSTs(rightOne, rightTwo);
};

function getSmaller(array) {
    let smaller = [];

    for (let i = 1; i < array.length; i++) {
        if (array[i] < array[0]) {
            smaller.push(array[i]);
        };
    };

    return smaller;
};

function getBiggerOrEqual(array) {
    let biggerOrEqual = [];

    for (let i = 1; i < array.length; i++) {
        if (array[i] >= array[0]) {
            biggerOrEqual.push(array[i]);
        };
    };

    return biggerOrEqual;
};
