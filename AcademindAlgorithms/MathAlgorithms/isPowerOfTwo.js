// Determine whether an input number is a power of two.
// Divide number and future division results by two, until 1 is reached and
// check if the remainder is always 0

function isPowerOfTwo(number) {
    if (number < 1) return false;
    let dividedNumber = number;

    while (dividedNumber !== 1) {
        if (dividedNumber % 2 !== 0) return false;
        dividedNumber = dividedNumber / 2;
    }

    return true;
}

// Time complexity
// Best Case: O(n)
// Average: O(log n)

// Improved

function isPowerOfTwo(number) {
    if (number < 1) return false;

    return (number & (number - 1)) === 0; // O(1)
}
