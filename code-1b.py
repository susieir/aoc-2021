""" Code to solve the AOC day 1 puzzle - part 2 """


def main(input_path):
    """ Takes input numbers and returns number of
    positive increments"""
    # Initialise counters
    rcount = 0
    increases = 0
    # Initialise lists
    prev_list = []
    current_list = []
    # Iterate through input line by line
    with open(input_path, "r") as fp:
        for line in fp:
            # For the first three rows, append the latest value to the list
            if rcount <= 2:
                prev_list.append(int(line))
                rcount += 1
            else:
                # Copy the current list to the previous list
                current_list = prev_list.copy()
                # Drop the first value and add the latest
                current_list.pop(0)
                current_list.append(int(line))
                # Calculate difference
                current_sum = sum(current_list)
                prev_sum = sum(prev_list)
                diff = current_sum - prev_sum
                #print(f"Current {current_sum}, previous {prev_sum}")
                # If difference is positive increment increases counter
                if diff > 0:
                    increases += 1
                # Reset current list to previous list
                prev_list = current_list.copy()
    return increases


# Set input path
input_path = "input-1.csv"

print(main(input_path))