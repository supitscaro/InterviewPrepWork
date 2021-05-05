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
    let count = 0;
    let mark = new Array(n + 1).fill(false); // creates an array filled with false of n + 1 values

    for (let i = 2; i < n; i++) {
        if (!mark[i]) { // if there's no mark[i] then do next loop
            for (let j = i * i; j < n; j++) { // for each num of i * i, we set mark[j] to true
                mark[j] = true;
            }
            count++;
        }
    }

    return count;
}
