# we're given two arrays containing the height of each student based on their color shirt
# we need to arrange the students so the student behind someone is taller than the person
# in front of them
# caveat: each row must have the students of the same shirt color
# we need to return if this is possible

# INPUTS/OUTPUTS
# red_shirt_heights = [5, 8, 1, 3, 4], blue_shirt_heights = [6, 9, 2, 4, 5] => True

# NOTES
# sort in desc order so you can grab the tallest kid by doing arr[0]
# choose the tallest kid from the two arrays and set that to one of the colors in our shirt_front_row, so they can be placed in the front
# iterate through one of the arrays by doing range(len(arr)) - doesnt matter which of the arrays cause both have the same length
# create variables for both shirt colors using the idx in the loop
# if our shirt_front_row is red, return false if the red shirt height is greater than the blue shirt
# do the same if shirt_front_row is blue


def classPhotos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    front_shirt_color = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'

    for idx in range(len(red_shirt_heights)):
        red_shirt = red_shirt_heights[idx]
        blue_shirt = blue_shirt_heights[idx]

        if front_shirt_color == 'RED':
            if red_shirt > blue_shirt:
                return False
        else:
            if blue_shirt > red_shirt:
                return False

    return True

    # red_shirt_heights.sort(reverse=True)
    # blue_shirt_heights.sort(reverse=True)

    # first_row_color = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'

    # for idx in range(len(red_shirt_heights)):
    #     red_shirt_height = red_shirt_heights[idx]
    #     blue_shirt_height = blue_shirt_heights[idx]

    #     if first_row_color == 'RED':
    #         if red_shirt_height >= blue_shirt_height:
    #             return False
    #     else:
    #         if blue_shirt_height >= red_shirt_height:
    #             return False

    # return True
