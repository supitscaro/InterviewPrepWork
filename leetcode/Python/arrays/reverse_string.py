# Write a function that reverses a string. The input string is given as an array of characters s.

# INPUTS/OUPUTS
# s = ['h', 'e', 'l', 'l', 'o'] => ['o', 'l', 'l', 'e', 'h']

def reverseString(s):
    start_pointer = 0
    end_pointer = len(s) - 1

    while start_pointer < end_pointer:
        s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer]
        start_pointer += 1
        end_pointer -= 1
