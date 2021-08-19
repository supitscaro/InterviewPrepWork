# Given an input string of a certain length, design an algorithm that compresses the string

#  consecutive duplicates of characters are replaced with whe character and followed by the number of consecutive duplicates

#  "wwwwaaadexxxxxx" => "w4a3dex6"

def stringCompress(string):
    index = 0
    res = ''

    while index < len(string):
        appearance_counter = 1
        string_length = len(string)

        while ((index < string_length - 1) and string[index] == string[index + 1]):
            appearance_counter += 1
            index += 1

        if appearance_counter == 1:
            res += string[index]
        else:
            res += string[index] + str(appearance_counter)

        index += 1

    print(res)
    return res


string_test = "wwwwaaadexxxxxxywww"
stringCompress(string_test)
