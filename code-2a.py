""" Code to solve aoc-2021 day 2 part 1 """

def main(input_path):
    """aoc-2021 day 2 part a"""
    # Initialise starting position
    horiz = 0
    depth = 0

    # Read input file
    with open(input_path, 'r') as fp:
        for line in fp:
            direction, unit = line.split()
            if direction == 'forward':
                horiz += int(unit)
            elif direction == 'up':
                depth -= int(unit)
            elif direction == 'down':
                depth += int(unit)
    return(horiz * depth)

# Set input path
input_path = "input-2.csv"

# Execute function
print(main(input_path))