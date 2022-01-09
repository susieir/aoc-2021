""" Code to solve aoc-2021 day 7 part b """

def read_input(input_path):
    """ Reads input to list of integers """
    with open(input_path, 'r') as fp:
        data = fp.read()
    return [int(i) for i in data.split(",")]

def calc_minmax(number_list):
    """ Outputs minimum and maximum possible position """
    return (min(number_list), max(number_list))

def calc_fuel_req(target_pos, current_pos):
    """
    Calculates the fuel required to reposition
    from current_pos to target_pos
    """
    delta = abs(target_pos - current_pos)
    fuel_req = (delta * (delta + 1) / 2)
    return fuel_req

def main(input_path):
    # Read input to create number list
    number_list = read_input(input_path)
    # Return min and max possible position
    min_pos, max_pos = calc_minmax(number_list)
    # Initialise list of fuel counts
    fuel_count_list = []
    # Set target position
    for pos in range(min_pos, max_pos + 1):
        # Initialise fuel count
        fuel_count = 0
        for n in number_list:
            fuel_count += calc_fuel_req(pos, n)
        fuel_count_list.append(fuel_count)

    return int(min(fuel_count_list))

print(main('input-7.csv'))