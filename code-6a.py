""" Code to solve aoc-2021 day 6 part a """

def initial_state(in_path):
    """Reads initial state into counter dictionary"""
    # Read input csv
    with open(in_path, 'r') as fp:
        data = fp.read()
    # Convert to list of numbers
    num_list = [int(i) for i in data.split(",")]
    # Convert to counter dict
    initial_state_dict = {}
    for num in num_list:
        if num in initial_state_dict.keys():
            initial_state_dict[num] += 1
        else:
            initial_state_dict[num] = 1
    return initial_state_dict


def increment_day(in_dict):
    """
    Takes counter dict with initial state
    converts to new dict with next day's state
    """
    # Initialise dict
    new_state_dict = {}
    # For 0 times
    for key in in_dict.keys():
        #print(key)
        if key == 0:
            if 6 in new_state_dict.keys():
                new_state_dict[6] += in_dict[key]
            else:
                new_state_dict[6] = in_dict[key]
            if 8 in new_state_dict.keys():
                new_state_dict[8] += in_dict[key]
            else:
                new_state_dict[8] = in_dict[key]
        else:
            new_key = key - 1
            if new_key in new_state_dict.keys():
                new_state_dict[new_key] += in_dict[key]
            else:
                new_state_dict[new_key] = in_dict[key]
    return new_state_dict

def n_days(in_dict, days):
    """
    Increments initial state by n days
    """
    # Set active_dict to initial dict
    active_dict = in_dict
    for i in range(days):
        active_dict = increment_day(active_dict)
        #print(f"After {i + 1} days: {active_dict}")
    return active_dict

def main(in_path, days):
    # Create initial state
    in_dict = initial_state(in_path)
    # Increment by 5 days
    final_dict = n_days(in_dict, days)
    # Sum total lantern fish
    fish_count = 0
    for key in final_dict.keys():
        fish_count += final_dict[key]
    return fish_count

print(main('input-6.csv', 256))

"""
# Increment day and output result
day_2 = increment_day(in_dict)
print(f"After 1 day {day_2}")
# Increment day and output result
day_3 = increment_day(day_2)
print(f"After 2 days {day_3}")
"""

