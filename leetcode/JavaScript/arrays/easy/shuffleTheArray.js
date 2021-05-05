// Given the array nums consisting of 2n elements in the
// form [x1,x2,...,xn,y1,y2,...,yn].

// Return the array in the form [x1,y1,x2,y2,...,xn,yn].



// Example 1:

// Input: nums = [2,5,1,3,4,7], n = 3
// Output: [2,3,5,4,1,7]
// Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
// Example 2:

// Input: nums = [1,2,3,4,4,3,2,1], n = 4
// Output: [1,4,2,3,3,2,4,1]
// Example 3:

// Input: nums = [1,1,2,2], n = 2
// Output: [1,2,1,2]

var shuffle = function (nums, n) {
    let numsTwo = [];
    let finalArray = [];

    for (let i = n; i < nums.length; i++) { // we start looping at the index n
        numsTwo.push(nums[i]); // we push the number from index n into numsTwo
    } // at the end we will get an array of all Y numbers

    for (let i = 0; i < n; i++) { // we loop for how long n is, so if its 5, loop 5 times
        finalArray.push(nums[i]) // we push the first X1
        finalArray.push(numsTwo[i]); // we push the first Y1 from numsTwo
    }

    return finalArray;
}

// Logic here is to split the arrays by looping until we reach "n".
// By doing this, we can separate our nums array into X and Y
// Then we can do a second loop
