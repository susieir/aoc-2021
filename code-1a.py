""" Code to solve the AOC day 1 puzzle - part 1"""


def main(input):
    """ Takes input numbers and returns number of
    positive increments"""
    # Initialise counters
    rcount = 0
    increases = 0
    # Iterate through input line by line
    with open(input, "r") as fp:
        for line in fp:
            # For the first line store result
            if rcount == 0:
                # Store first value
                prev = int(line)
                rcount += 1
            # For all other lines calculate increment and reset prev value
            else:
                # Store latest value
                current = int(line)
                # Calculate difference
                diff = current - prev
                # If positive difference, increment increases counter
                if diff > 0:
                    increases += 1
                # Reset prev value
                prev = current
                # Increment row counter
                rcount += 1
    return increases

# Set input path
input = "input-1.csv"

print(main(input))