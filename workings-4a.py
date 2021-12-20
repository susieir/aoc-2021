# Set input path
input_path = "input-4.csv"

def format_board(board):
    """
    Takes a board in str format
    returns in list of lists format
    """
    # Initialise empty board
    board_formatted = []
    # Split into rows
    rows = [x for x in board.split("\n")]
    for row in rows:
        board_formatted.append([n for n in row.split() if n.isdigit()])
    return board_formatted


def store_boards(input_path):
    """
    Takes input file and reads boards, 
    formats board into list of lists
    returns nested list of lists of boards
    """
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

