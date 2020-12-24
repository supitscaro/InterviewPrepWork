// Count the number of prime numbers less than a non-negative number, n.

// Example 1:
// Input: n = 10
// Output: 4
// Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

// Example 2:
// Input: n = 0
// Output: 0

// Example 3:
// Input: n = 1
// Output: 0

var countPrimes = function (n) {

}

function isPrime(num) {
    let sqrt = Math.floor(Math.sqrt(num));
    for (let i = 2; i < sqrt; i++) {
        if (num % i === 0) {
            return false;
        }
    }

    return true;
}
