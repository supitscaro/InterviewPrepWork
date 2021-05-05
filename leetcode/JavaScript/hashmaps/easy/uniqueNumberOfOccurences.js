// Given an array of integers arr, write a function that returns
// true if and only if the number of occurrences of each value in
// the array is unique.

// Example 1:
// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
// No two values have the same number of occurrences.

// Example 2:
// Input: arr = [1,2]
// Output: false

// Example 3:
// Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
// Output: true

var uniqueOccurrences = function (arr) {
    let map = {}; // {'1': 3, '2': 2, '3': 1}

    // move array values to object.
    for (let val of arr) {

        // if the value in array is in map then increment value.
        // else add it with a value of 1
        if (map[val]) {
            map[val]++;
        } else {
            map[val] = 1;
        }
    }

    // we create an array of the map object
    let entries = Object.entries(map); // [3, 2, 1]


    return (new Set(entries)).size === entries.length; // Set(3) {3, 2, 1}. size for set is 3 and entries length is 3
};

// if a value in the array had the same occurence, then the Set size
// would not be equal to the Object.entries length
