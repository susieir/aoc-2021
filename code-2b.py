""" Code to solve aoc-2021 day 2 part b """

def main(input_path):
    """aoc-2021 day 2 part b"""
    # Initialise starting position and aim
    horiz = 0
    depth = 0
    aim = 0

    # Read input file
    with open(input_path, 'r') as fp:
        for line in fp:
            direction, unit = line.split()
            if direction == 'forward':
                horiz += int(unit)
                depth += int(unit) * aim
            elif direction == 'up':
                aim -= int(unit)
            elif direction == 'down':
                aim += int(unit)
    return(horiz * depth)

# Set input path
input_path = "input-2.csv"

# Execute function
print(main(input_path))