# we're given two arrays containing the height of each student based on their color shirt
# we need to arrange the students so the student behind someone is taller than the person
# in front of them
# caveat: each row must have the students of the same shirt color
# we need to return if this is possible

def classPhotos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    first_row_color = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'

    for idx in range(len(red_shirt_heights)):
        red_shirt_height = red_shirt_heights[idx]
        blue_shirt_height = blue_shirt_heights[idx]

        if first_row_color == 'RED':
            if red_shirt_height >= blue_shirt_height:
                return False
        else:
            if blue_shirt_height >= red_shirt_height:
                return False

    return True
