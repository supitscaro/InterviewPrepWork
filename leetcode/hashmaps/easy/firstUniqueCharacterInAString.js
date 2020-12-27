// Given a string, find the first non-repeating
// character in it and return its index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode"
// return 2.

var firstUniqueChar = function (s) {
    for (let i = 0; i < s.length; i++) {
        let letter = s[i];

        if (s.indexOf(letter) === s.lastIndexOf(letter)) { // returns the last index at which an element can be found
            return i;
        }
    }

    return -1;
};

// if the index of the letter is equal to the index of the last location the
// letter appears at then we return the index
