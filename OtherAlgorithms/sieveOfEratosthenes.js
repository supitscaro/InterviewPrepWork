// A prime number is a natural number greater than 1
// that is not a product of two smaller natural numbers.

// algorithm used to find prime numbers up to any given limit

var findPrimes = function (nums) {
    let count = 0;
    let mark = new Array(n + 1).fill(false);

    for (let i = 2; i < n; i++) {
        if (!mark[i]) {
            for (let j = i * i; j < n; j++) {
                mark[j] = true;
            }
            count++;
        }
    }

    return count;
}
