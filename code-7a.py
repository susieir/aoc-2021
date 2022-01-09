""" Code to solve aoc-2021 day 7 part a """

def read_input(input_path):
    """ Reads input to list of integers """
    with open(input_path, 'r') as fp:
        data = fp.read()
    return [int(i) for i in data.split(",")]

def median_value(num_list):
    """ Finds median value in list of numbers """
    ordered_list = list(sorted(num_list))
    if len(ordered_list) % 2 == 1:
        middle_val = int((len(ordered_list) / 2) - 0.5)
        median = ordered_list[middle_val]
    elif len(ordered_list) % 2 == 0:
        middle_val = int((len(ordered_list) / 2))
        median = ordered_list[middle_val]
    return median

def calc_dist_from_med(num_list, median):
    """ Calculates sum of distances from median """
    # Initialise distance counter
    dist_count = 0
    # Iterate through num list
    for i in num_list:
        dist_count += abs(median - i)
    return dist_count

# Read input to create number list
number_list = read_input('input-7.csv')
# Find median value
median = median_value(number_list)
# Calculate total fuel used
print(calc_dist_from_med(number_list, median))