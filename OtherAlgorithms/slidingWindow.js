// The problem will involve a data structure that is ordered
// and iterable like an array or a string

// You are looking for some subrange in that array/string,
// like a longest, shortest or target value.

// There is an apparent naive or brute force solution that runs
// in O(N²), O(2^N) or some other large time complexity.

// strings, arrays, linked lists

var slidingWindow = function (s) {
    if (s == null || s.length === 0) return 0;

    let seen = new Set();
    let longest = 0;
    let j = 0;

    for (let i = 0; i < s.length; i++) {
        while (seen.has(s[i])) {
            seen.delete(s[j]);
            j++;
        }

        seen.add(s[i]);
        longest = Math.max(longest, i - j + 1);
    }

    return longest;

}
