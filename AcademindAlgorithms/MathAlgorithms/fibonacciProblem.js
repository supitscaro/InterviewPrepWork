// Return the nth element of the Fibonacci sequence.

function fib(n) {
    let nums = [1, 1]; // 1

    for (let i = 2; i < n + 1; i++) { // 1
        nums.push(nums[i - 2] + nums[i - 1]); // n - 1
    }

    return numbers[n]; // 1
}

// Time Complexity
// T = 1 + 1 + 1 + n - 1
// O(n)
