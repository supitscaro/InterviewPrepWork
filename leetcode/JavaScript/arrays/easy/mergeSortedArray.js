// Given two sorted integer arrays nums1 and nums2,
// merge nums2 into nums1 as one sorted array.

// Note:

// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is equal to m + n) to
// hold additional elements from nums2.

// Example:
// Input:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// Output: [1,2,2,3,5,6]

var merge = function (nums1, m, nums2, n) {
    let count = 0;

    for (let i = 0; i < nums1.length; i++) {
        let numsOneNum = nums1[i];

        if (numsOneNum === 0) {
            count++;

            if (count === n) {
                nums1.splice(nums1.length - n);
            }
        }
    }

    nums1.push(...nums2);
    nums1.sort((a, b) => a - b);

    return nums1;
}
