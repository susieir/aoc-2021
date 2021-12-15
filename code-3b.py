""" Code to solve aoc-2021 day 3 part b """

# Read input file
def create_input_list(input_path):
    with open(input_path, 'r') as fp:
        input_list = [v.strip() for v in fp]
    return input_list

def find_rating(input_path, rating_type):
    """ 
    Looks for most/least popular bit based on rating type and retains for each position
    Returns decimal of selected binary character
    """
    # Set keep values '0' (least common) or '1' (most common) based on rating_type 
    if rating_type == 'oxygen':
        keep_val = '0'
    elif rating_type == 'co2':
        keep_val = '1'
    # Create input list
    short_list = create_input_list(input_path)
    # Iterate through positions
    for i in range(len(short_list[0])):
        while len(short_list) > 1:
            # Check for least common bit in given position and retain
            if sum([1 if v[i] == '1' else 0 for v in short_list]) >= len(short_list)/2:
                short_list = [v for v in short_list if v[i] == keep_val]
            else:
                short_list = [v for v in short_list if v[i] != keep_val]
            i += 1
        else:
            # Return decimal of selected binary value
            return int(short_list[0], 2)

def main(input_path):
    """ Finds oxygen and co2 scrubber ratings and returns product """
    return find_rating(input_path, 'oxygen') * find_rating(input_path, 'co2')

# Set input_path
input_path = "input-3.csv"

# Execute function
print(main(input_path))
