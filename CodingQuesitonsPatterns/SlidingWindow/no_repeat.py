# Given a string, find the length of the longest substring, which has no repeating characters

# INPUTS/OUTPUTS
# "aabccbb" => 3
# explanation:
#   the longest substring without any repeating characters is abc

# "abbbb" => 2
# explanation:
#   the longest substring without any repeating characters is "ab"

# "abccde" => 3
# explanation:
#   longest substrings without any repeating characters are "abc" and "cde"

# THOUGHTS
#   might need a dict to keep track of the characters
#   create a window start variable, a max length variable, and the char freq dict
#   if letter not in char_freq then add it and set it = to 0

def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    char_freq = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_freq:
            print(char_freq)
            print(char_freq[right_char] + 1)
            # we want to get the index of the char that appears the most
            window_start = max(window_start, char_freq[right_char] + 1)

        char_freq[right_char] = window_end


non_repeat_substring("aabccbb")
