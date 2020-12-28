// Write a function that takes in a non-empty string and that returns
// a boolean representing whether the string is a palindrome.

// A palindrome is defined as a string thats written the same forward
// and backward. Note that single-character strings are palindromes

function isPalindrome(string) {
    let left = 0;
    let right = string.length - 1;

    while (left < right) {
        if (string[left] !== string[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};

// QUESTIONS TO CONSIDER
// why do return false instead of making if statement true
