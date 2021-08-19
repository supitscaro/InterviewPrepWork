# given a string s, return the longest palindromic substring in s

# NOTES
#   "babad"
#   we could use the sliding window technique
#

class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        start = 0
        end = 0

        for idx in range(len(s)):
            # check against same character
            length_one = self.expandFromMiddle(s, idx, idx)
            length_two = self.expandFromMiddle(s, idx, idx + 1)
            res = max(length_one, length_two)

            if res > end - start:
                start = idx - ((res - 1) // 2)
                end = idx + (res // 2)

    def expandFromMiddle(s, left, right):
        if s == None or left > right:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left + 1
