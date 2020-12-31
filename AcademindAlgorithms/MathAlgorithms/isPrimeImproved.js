// 5 is a Prime: divisible by itself and 1
// 9 is NOT a Prime: divisible by itself, by 1, and 3

// every number that's not a prime has a product that consists of two factors,
// a and b that are both neither 1 nor the number itself.

// Example: 9 = 3 * 3

// at least one factor is smaller or equal to the square root of the number
// sqrt(9) => 9 = 3 * 3 => Both factors are equal to the square root

function isPrime(number) {
    for (let i = 2; i < Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }

    return true;
}

//Time Complexity
// Improved: O(sqrt(n))
