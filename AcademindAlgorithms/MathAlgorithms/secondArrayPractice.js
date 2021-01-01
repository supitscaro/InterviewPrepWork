// The algorithm should take an array of numbers as input and return the
// minimum value in the array (i.e. the smallest number)

function minValue(numbers) {
    let num = Infinity; // 1
    for (let i = 0; i < numbers.length; i++) { // 1
        if (numbers[i] < num) { // n
            num = numbers[i]; // n
        }
    }

    return num;
};

// Time Complexity
// O(n)
