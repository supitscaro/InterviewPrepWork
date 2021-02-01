// Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
// some elements appear twice and others appear once.

// Find all the elements that appear twice in this array.

// Could you do it without extra space and in O(n) runtime?

// Example:
// Input:
// [4,3,2,7,8,2,3,1]

// Output:
// [2,3]


var findDuplicates = function (nums) {
    let counter = {};

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];

        if (counter[num]) {
            counter[num]++;
        } else {
            counter[num] = 1;
        }
    }

    let res = [];

    for (let key in counter) {
        let amount = counter[key];

        if (amount >= 2) {
            res.push(key)
        }
    }

    return res;
}
