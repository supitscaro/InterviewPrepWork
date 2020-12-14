// Given an integer n, return any array containing n
// unique integers such that they add up to 0.

// Example 1:

// Input: n = 5
// Output: [-7,-1,1,3,4]
// Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
// Example 2:

// Input: n = 3
// Output: [-1,0,1]
// Example 3:

// Input: n = 1
// Output: [0]

var sumZero = function (n) { // given n = 5
    let result = []; // after loop, we get [1, 2, 3, 4]
    let num = 0;

    for (let i = 1; i < n; i++) { // we start looping at 1
        result.push(i); // we go i = 1, i = 2, i = 3, i = 4
        num += i; // num at end of loop will now equal to 10
    }

    result.push(-num); // to cancel it out, we push a negative 10

    return result; // we get integers that add up to 0
}
