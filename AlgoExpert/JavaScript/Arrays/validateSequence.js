// Given two non-empty arrays of integers, write a function that determines
// whether the second array is a subsequence of the first one.

// A subsequence of an array is a set of numbers that aren't necessarily
// adjacent in the array but that are in the same order as they appear
// in the array.

function isValidSubsequence(array, sequence) {
    let seqIdx = 0;

    for (let value of array) {
        if (seqIdx === sequence.length) {
            break;
        }
        if (sequence[seqIdx] === value) {
            seqIdx++;
        }
    }

    return seqIdx === sequence.length;
};
