# Given a string, find the length of the longest substring in it with no more than K distinct characters
# You can assume K is less than or equal to the length of the given string

# INPUTS/OUTPUTS
#   "araaci", K=2 => 4
#   explanation:
#       the longest substring with no more than '2' distinct characters is 'araa'

#   "araaci", K=1 => 2
#   explanation:
#       the longest substring with no more than '1' distinct characters is 'aa'

#   "cbbebi", K=3 => 5
#   explanation:
#       the longest substring with no more than '3' distinct characters are 'cbbeb' and 'bbebi'

def longest_substring_with_k_distinct(str1, k):
    max_substring = 0
    window_substring_length = 0
