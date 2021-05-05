// Given an array A of strings made only from lowercase letters,
// return a list of all characters that show up in all strings
// within the list (including duplicates).  For example, if a
// character occurs 3 times in all strings but not 4 times, you
// need to include that character three times in the final answer.

// You may return the answer in any order.

// Example 1:
// Input: ["bella","label","roller"]
// Output: ["e","l","l"]

// Example 2:
// Input: ["cool","lock","cook"]
// Output: ["c","o"]

var commonChars = function (array) {
    let common = array[0].split('').filter(char => { // we split the word into an array
        for (let i = 0; i < array.length; i++) { // we iterate through the original array
            if (!array[i].includes(char)) return false; // if in array[i] (each word), DOESN'T contain the char return false
            else {
                array[i] = array[i].replace(char, ''); // IF it does contain the character, replace it with an empty string
            }
        }
        return true; // once out of the loop, we return true which adds it into the new common array
    });

    return common; // return true
};
