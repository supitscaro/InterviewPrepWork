// Calculate the factorial of a number
// Needs to do one thing: go through all smaller numbers and multiply them
// with each other (and with the input number)

function fact(number) {
    let result = 1;
    for (let i = 2; i <= number; i++) {
        result *= i;
    }

    return result;
}

// Time Complexity
// O(n)
