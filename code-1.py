""" Code to solve the AOC day 1 puzzle """

# Set input path
input = "input-1.csv"

# Set counter to 0
rcount = 0
# Intialise increases counter
increases = 0
# Iterate through input line by line
with open(input, "r") as fp:
    # Iterate through each line
    for line in fp:
        # For the first line store result
        if rcount == 0:
            # Store first value
            prev = int(line)
            print(f"First value is {prev}")
            rcount += 1
        else:
            # Store latest value
            current = int(line)
            print(f"Next value is {current}")
            # Calculate difference
            diff = current - prev
            print(f"Diff is {diff}")
            # If positive difference, increment increases counter
            if diff > 0:
                increases += 1
                print("Increase")
            # Reset prev value
            prev = current
            # Increment row counter
            rcount += 1

print(increases)