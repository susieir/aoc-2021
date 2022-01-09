""" Code to solve aoc-2021 day 7 part b """

def read_outputs(input_path):
    """ 
    Read input path and return outputs
    as a list of lists 
    """
    # Open file
    with open(input_path, 'r') as fp:
        # Initialise list of outputs
        outputs = []
        # Read each entry
        for line in fp.read().split("\n"):
            # Read output as list
            outputs.append(line.split("|")[1].strip().split(" "))
        return outputs

def convert_outputs(outputs):
    """ Convert outputs to number of distinct letters """
    # Initialise list of output numbers
    output_numbers = []
    # Iterate through entries
    for entry in outputs:
        # Initialise list of entry numbers
        entry_numbers = []
        # For each character
        for char in entry:
            entry_numbers.append(len(set(char)))
        output_numbers.append(entry_numbers)
    return output_numbers

# Set number of characters for each digit
digit_1 = 2
digit_4 = 4
digit_7 = 3
digit_8 = 7
unique_digits = [digit_1, digit_4, digit_7, digit_8]

def main(input_path):
    # Read outputs and convert to list of list of distinct numbers
    outputs = read_outputs('input-8.csv')
    output_numbers = convert_outputs(outputs)
    # Count number of appearances of digit_1, digit_4, digit_7 and digit_8
    digit_counts = 0
    # Iterate through entries
    for entry in output_numbers:
        for digit in entry:
            if digit in unique_digits:
                digit_counts += 1
    return digit_counts

print(main('input-8.csv'))
