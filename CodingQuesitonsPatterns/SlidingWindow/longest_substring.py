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

# NOTES
#   we can use a hashmap to keep track of the frequency of each character we have
#   insert the characters from the beginning of the string until we have K distinct characters in the hashmap
#   the characters in the hashmap constitute our sliding window
#       we have to find the longest such window having no more than K distinct characters
#       we can remember the length of this window as the longest window so far
#   we keep adding one character in the sliding window
#   each step, we will try to shrink the window from the beginning if the count of distinct characters in the hashmap is larger than K
#   we shrink the widow until we no longer have more than K distinct characters in the hashmap
#   while we shrink the window, we decrement the character's frequency going out of the window and remove it from the hashmap if its frequency becomes zero


def longest_substring_with_k_distinct(str1, k):
    max_length = 0
    window_start = 0
    character_frequency = {}

    # Add character to dictionary if it's not there and if it is, increment by 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in character_frequency:
            character_frequency[right_char] = 0
        character_frequency += 1

        # check if our dict has more than K characters
        while len(character_frequency) > k:
            left_char = str1[window_start]
            character_frequency[left_char] -= 1

            if character_frequency[left_char] == 0:
                del character_frequency[left_char]

            window_start += 1  # shrinking the window from the beginning

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
