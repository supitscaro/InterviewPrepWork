// Algorithm needs to do one thing: try dividing the number by all smaller
// numbers and return true if it's only divisible by itself and 1

function isPrime(number) {
    for (let i = 2; i < number; i++) { // 1
        if (number % i === 0) { // n
            return false; // we have a remainder, so it's not a Prime
            // runs at most 1
        }
    }

    return true; // if there's no remainder then it's a Prime
    // 1
}

// Time Complexity
// Best case: number = 1 OR number = 2 => O(1)
// Worst case: number = 1,000,000 => O(n)
