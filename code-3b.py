""" Code to solve aoc-2021 day 3 part b """

# Set input_path
input_path = "input-3.csv"

# Read input file
with open(input_path, 'r') as fp:
    input_list = [v.strip() for v in fp]
print(input_list)

def filter_list(input_list, pos):
    # Initialise lists
    zeros = []
    ones = []
    while len(input_list) > 0:
        #print(f"List: {input_list}")
        value = input_list[0]
        #print(f"Value: {value}")
        if value[pos] == '0':
            input_list.remove(value)
            zeros.append(value)
        else:
            input_list.remove(value)
            ones.append(value)
        #print(f"Zeros: {zeros}")
        #print(f"Ones: {ones}")
    if len(zeros) > len(ones):
        input_list.extend(zeros)
    else:
        input_list.extend(ones)
    return input_list
    

print(filter_list(input_list, 0))

