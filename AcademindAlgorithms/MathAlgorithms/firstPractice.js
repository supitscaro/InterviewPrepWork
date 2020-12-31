// Write an algorithm that takes an array of numbers as input and calculates
// the sum of those numbers.

// Define the Time Complexity of that algorithm and determine what the lowest
// possibe time complexity is for this problem

function sumNumbers(numbers) {
    let result = 0; // 1

    for (let i = 0; i < numbers.length; i++) { // 1
        result += numbers[i]; // n
    }

    return result; // 1
}

// Time Complexity ???
// 3 + n so O(n)

function sumNumbers(numbers) {
    return numbers.reduce((sum, curNum) => sum + curNum, 0);
}

// Time Complexity
// also gives us O(n) linear time complexity
