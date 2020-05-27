def is_mutant(rows):
    """This function allows you tue determine if a DNA array belongs to a mutant or a human.

    Args:
        rows (string[]): The DNA rows of strings.

    Returns:
        bool: The return value. True when DNA belongs to a mutant, false when not.
    """

    for x in range(len(rows)):
        for y in range(len(rows[x])):

            # to the right / horizontal
            if count_by_direction(rows, rows[x][y], x, y, +1, 0, 0) > 3:
                return True

            # to the bottom / vertical
            if count_by_direction(rows, rows[x][y], x, y, 0, +1, 0) > 3:
                return True

            # to the bottom right / diagonal
            if count_by_direction(rows, rows[x][y], x, y, +1, +1, 0) > 3:
                return True

            # to the bottom left / diagonal
            if count_by_direction(rows, rows[x][y], x, y, -1, +1, 0) > 3:
                return True

    return False


def count_by_direction(rows, letter, current_x, current_y, direction_x, direction_y, count):
    """This function allow us to to recursively move into the 2 dimensional matrix
    and search for continuous chars

    Args:
        rows (string[]): The DNA rows of strings.
        letter (char): The current analyzed char
        current_x (int): The current X position in the 2 dimensions matrix
        current_y (int): The current Y position in the 2 dimensions matrix
        direction_x (int): The desired movement on X axis
        direction_y (int): The desired movement on Y axis
        count (int): The current count observed during the recursive process

    Returns:
        bool: The return value. The new observed count after procesing
    """

    x = current_x + direction_x
    y = current_y + direction_y

    try:
        if letter == rows[x][y]:

            count += 1

            # If we didn't reach minimum of 4, we will still search, avoid loosing time
            if count < 4:
                count += count_by_direction(rows, letter, x, y, direction_x, direction_y, count)

            return count
        else:
            return 0
    except IndexError:
        return 0
