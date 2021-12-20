""" Code to solve aoc-2021 day 4 part b """

def format_board(board):
    """ Takes a board in str format returns in list of lists format """
    # Initialise empty board
    board_formatted = []
    # Split into rows
    rows = [x for x in board.split("\n")]
    for row in rows:
        board_formatted.append([int(n) for n in row.split() if n.isdigit()])
    return board_formatted

def read_numbers(input_path):
    """ Loads input file and returns list of numbers """
    # Open and read file
    with open(input_path, 'r') as fp:
        data = fp.read()
        # Store first section of data as numbers
        numbers = data.split("\n")[0]
        # Return numbers as integers in list form 
        return [int(n) for n in numbers.split(",")]

def read_boards(input_path):
    """ Takes input file, reads and formats boards into nested list of lists """
    # Read file and store data
    with open(input_path, 'r') as fp:
        data = fp.read()
    # Initialise list of boards
    board_list = []
    # Count number of double line breaks
    board_range = data.count("\n\n")
    # Iterate through all boards
    for i in range(board_range + 1):
        # Skip first section of data (numbers)
        if i == 0:
            i += 1
            next
        # Capture bingo board, foramt and append to board list
        else:
            board = data.split("\n\n")[i]
            board_list.append(format_board(board))
            i += 1
    return board_list

def initialise_bingo_counter(input_path):
    """ Creates bingo counter with empty row/col scores """
    # Count number of boards
    board_count = len(read_boards(input_path))
    # Initialise bingo_counter_list
    bingo_counter = []
    # Create the same number of dictionary keys, each with a list of 10 0's as values
    for i in range(board_count):
        bingo_counter.append([5 for n in range(10)])
    return bingo_counter

def calculate_score(number_list, win_n, win_board):
    """ 
    Takes the list of numbers, winning number and winning board
    and returns the final score
    calculated as winning number multiplied by
    sum of unmarked numbers on winning board
    """    
    # Find list of called numbers
    marked_numbers = number_list[:number_list.index(win_n)+1]
    # Calculate sum of unmarked numbers
    unmarked_sum = 0
    for list in win_board:
        unmarked_sum += sum([item for item in list if item not in marked_numbers])
    return unmarked_sum * win_n

def main(input_path):
    """ Plays game - part b variant """
    # Create number list and board list
    num_list = read_numbers(input_path)
    board_list = read_boards(input_path)

    # Initialise bingo counter
    bingo_counter = initialise_bingo_counter(input_path)

    # Set bingo status
    bingo = True
    # Iterate backwards through num list
    for n in num_list[::-1]:
        # Iterate through boards
        for j in range(len(board_list)):
            for i in range(5):
                # Iterate through rows
                if n in board_list[j][i]:
                    bingo_counter[j][i] -= 1
                # Iterate through columns
                col = [x[i] for x in board_list[j]]
                if n in col:
                    bingo_counter[j][i + 5] -= 1
            if max(bingo_counter[j]) < 5:
                bingo = False
                final_score = calculate_score(num_list, n, board_list[j])
                break
        if bingo == False:
            break
    return final_score

print(main('input-4.csv'))