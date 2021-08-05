# Given a string, find the length of the longest substring, which has no repeating characters

# INPUTS/OUTPUTS
# "aabccbb" => 3
#   explanation:
#       the longest substring without any repeating characters is "abc"

# "abbbb" => 2
#   explanation:
#       the longest substring without any repeating characters is "ab"

# "abccde" => 3
#   explanation:
#       longest substrings without any repeating characters are "abc" & "cde"

def non_repeat_substring(str):
    char_frequency = {}
    max_length = 0
    window_start = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            window_start = max(window_start, char_frequency[right_char] + 1)
        char_frequency[right_char] = window_end

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
