// Given an array of integers nums.

// A pair (i,j) is called good if nums[i] == nums[j] and i < j.

// Return the number of good pairs.

// Example 1:

// Input: nums = [1,2,3,1,1,3]
// Output: 4
// Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
// Example 2:

// Input: nums = [1,1,1,1]
// Output: 6
// Explanation: Each pair in the array are good.
// Example 3:

// Input: nums = [1,2,3]
// Output: 0

var numIdenticalPairs = function (nums) {
    let goodPairs = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        let firstNum = nums[i];

        for (let j = i + 1; j < nums.length; j++) {
            let secondNum = nums[j];

            if (firstNum == secondNum && i < j) {
                goodPairs++;
            }
        }
    }

    return goodPairs;
}
