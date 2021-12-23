""" Code to solve aoc-2021 day 5 part a """

# Read input
def read_input(input_path):
    """Reads input"""
    # Initialise list of tuples containing coords
    coord_list = []
    # Read file
    with open(input_path, 'r') as fp:
        data = fp.read()
    # Initialise max_x and max_y
    max_x = 0
    max_y = 0
    # Convert coords to list of tuples and append to list if horiz or vert
    for line in data.split("\n"):
        x1 = int(line[0:line.find(",")])
        y1 = int(line[line.find(",")+1:line.find("->")])
        x2 = int(line[line.find("->")+3:line.find(",", line.find(",")+1)])
        y2 = int(line[line.find(",", line.find(",")+1)+1:])
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        coord_list.append([x1, y1, x2, y2])
    return coord_list, max_x, max_y

# Create grid
def create_grid(max_x, max_y):
    """Creates blank 9x9 grid"""
    blank_grid = []
    for i in range(0, max_y+1):
        blank_grid.append([0 for _ in range(0, max_x+1)])
    return blank_grid

def calc_points(x1, y1, x2, y2):
    """Takes list of tuples and calculates all points covered"""
    if x1 == x2:
        return([(x1, i) for i in range(min(y1, y2), max(y1, y2) + 1)])
    elif y1 == y2:
        return([(j, y1) for j in range(min(x1, x2), max(x1, x2) + 1)])
    else:
        if x1 < x2:
            x_s = [x for x in range(x1, x2 + 1)]
        elif x1 > x2:
            x_s = [x for x in range(x1, x2 - 1, -1)]
        if y1 < y2:
            y_s = [y for y in range(y1, y2 + 1)]
        elif y1 > y2:
            y_s = [x for x in range(y1, y2 - 1, -1)]
        return(list(zip(x_s, y_s)))

def increment_point(grid, y, x):
    """Increments grid by given point (x, y)"""
    grid[y][x] += 1
    return grid

def output_gtr_2_crossings(grid):
    """Outputs the number of points with more than 2 lines overlapping"""
    # Initialise counter
    gtr_2_count = 0
    for row in grid:
        gtr_2_count += sum([1 for n in row if n > 1])
    return gtr_2_count

def main(input_path):
    # Read input and create list of coords
    coord_list, max_x, max_y = read_input(input_path)
    # Create blank grid
    grid = create_grid(max_x, max_y)
    # For each pair of coords calculate points covered
    for i in range(len(coord_list)):
        x1, y1, x2, y2 = [coord for coord in coord_list[i]]
        #print(x1, y1, x2, y2)
        points = calc_points(x1, y1, x2, y2)
        #print(points)
        for point in points:
            increment_point(grid, point[1], point[0])
    # Count points where 2+ lines overlap
    score = output_gtr_2_crossings(grid)
    return score

print(main('input-5.csv'))
