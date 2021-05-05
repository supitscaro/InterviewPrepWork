// In an alien language, surprisingly they also use english lowercase
// letters, but possibly in a different order. The order of the alphabet
// is some permutation of lowercase letters.

// Given a sequence of words written in the alien language, and the order
// of the alphabet, return true if and only if the given words are sorted
// lexicographicaly in this alien language.

// Example 1:
// Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
// Output: true
// Explanation: As 'h' comes before 'l' in this language, then the sequence
// is sorted.

// Example 2:
// Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
// Output: false
// Explanation: As 'd' comes after 'l' in this language, then words[0] >
// words[1], hence the sequence is unsorted.

// Example 3:
// Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
// Output: false
// Explanation: The first three characters "app" match, and the second
// string is shorter (in size.) According to lexicographical rules
// "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank
// character which is less than any other character (More info).

var isAlienSorted = function (words, order) {
    for (let i = 1; i < words.length; i++) {
        let firstWord = words[i - 1];
        let secondWord = words[i];
        let maxLen = Math.max(firstWord, secondWord);

        for (let j = 0; j < maxLen; j++) {
            let indexOne = order.indexOf(firstWord[j]);
            let indexTwo = order.indexOf(secondWord[j]);

            if (indexOne > indexTwo) return false;
            else if (indexOne < indexTwo) {
                j = maxLen;
            }
        }
    }

    return true;
}
