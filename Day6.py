# read input_Day6_test.txt
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data

lines = read_input('input_Day6.txt')
#print(lines)

# create a grid/array
def create_grid(data):
    grid = []
    for line in data.split('\n'):
        grid.append([x for x in line])
    return grid

grid = create_grid(lines)
#for row in grid:
#    print(row)

# find "^" in the grid
def find_start(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "^":
                return (i, j)
    return None

start_pos = find_start(grid)
print("Start position:", start_pos)

# - If there is something directly in front of you, turn right 90 degrees.
# - Otherwise, take a step forward.

# function to check if position is out of bounds
def is_out_of_bounds(grid, position):
    if position[0] < 0 or position[0] >= len(grid):
        return True
    if position[1] < 0 or position[1] >= len(grid[0]):
        return True
    return False

# function obstacle detection and direction change:
def detect_obstacle_and_change_direction(grid, current_position, current_direction):
    if current_direction == "up" and not is_out_of_bounds(grid, (current_position[0]-1, current_position[1])):
        if grid[ current_position[0]-1 ][ current_position[1] ] == "#":
            current_direction = "right"
    elif current_direction == "right" and not is_out_of_bounds(grid, (current_position[0], current_position[1]+1)):
        if grid[ current_position[0] ][ current_position[1]+1 ] == "#":
            current_direction = "down"
    elif current_direction == "down" and not is_out_of_bounds(grid, (current_position[0]+1, current_position[1])):
        if grid[ current_position[0]+1 ][ current_position[1] ] == "#":
            current_direction = "left"
    elif current_direction == "left" and not is_out_of_bounds(grid, (current_position[0], current_position[1]-1)):
        if grid[ current_position[0] ][ current_position[1]-1 ] == "#":
            current_direction = "up"
    return current_direction

# move in the grid according to the rules
def move_in_grid(grid, start_pos):
    current_position = start_pos
    current_direction = "up"
    escaped = False
    list_visited_positions = []
    list_visited_positions.append(start_pos)

    while not escaped:
        #print("current_position; begin while:", current_position)
        current_direction = detect_obstacle_and_change_direction(grid, current_position, current_direction)

        # move forward in the current direction
        if current_direction == "up":
            if is_out_of_bounds(grid, (current_position[0]-1, current_position[1])):
                escaped = True
                #print("escaped moving up from", current_position)
                break
            else:
                current_position = (current_position[0]-1, current_position[1]) # not out of bounds, move up
                #print("moved up to", current_position)
        elif current_direction == "right":
            if is_out_of_bounds(grid, (current_position[0], current_position[1]+1)):
                escaped = True
                break
            else:
                current_position = (current_position[0], current_position[1]+1)
        elif current_direction == "down":
            if is_out_of_bounds(grid, (current_position[0]+1, current_position[1])):
                escaped = True
                break
            else:
                current_position = (current_position[0]+1, current_position[1])
        elif current_direction == "left":
            if is_out_of_bounds(grid, (current_position[0], current_position[1]-1)):
                escaped = True
                break
            else:
                current_position = (current_position[0], current_position[1]-1)
        list_visited_positions.append(current_position)
        print("list_visited_positions", list_visited_positions)
    return list_visited_positions

visited_positions = move_in_grid(grid, start_pos)
#print("Visited positions:", visited_positions)
print("Number of unique visited positions:", len(set(visited_positions)))

# mark all visited positions in the grid with "X":
#def mark_visited_positions(grid, visited_positions):
#    for pos in visited_positions:
#        grid[pos[0]][pos[1]] = "X"
#    return grid
#marked_grid = mark_visited_positions(grid, visited_positions)
#for row in marked_grid:
#    print(row)
