""" Code to solve aoc-2021 day 3 part a """

def main(input_path):
    """Function to solve day 3 part a"""
    # Read report into list
    with open(input_path, 'r') as fp:
        report_list = [v.strip() for v in fp]

    # Set value length
    v_len = len(report_list[0])

    # Initialise binary strings
    gamma_bin = ""
    epsilon_bin = ""

    # Iterate each position of list
    for i in range(v_len):
        # Initialise counter
        zeros = 0
        ones = 0
        # For each value in list count bits in position i
        for value in report_list:
            if int(value[i]) == 0:
                zeros += 1
            elif int(value[i]) == 1:
                ones += 1
        if zeros > ones:
            gamma_bin += '0'
            epsilon_bin += '1'
        elif ones > zeros:
            gamma_bin += '1'
            epsilon_bin += '0'

    # Convert binary to decimal and multiply
    gamma_int = int(gamma_bin, 2)
    epsilon_int = int(epsilon_bin,2)
    return gamma_int * epsilon_int

# Set input path
input_path = "input-3.csv"

# Execute function
print(main(input_path))
