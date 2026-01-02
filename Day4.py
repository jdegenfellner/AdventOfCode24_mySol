# She only has to find one word: XMAS.
#
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping
# other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS -
# you need to find all of them.

# seems rather straigtforward:
# we just look for all the "X"s, which are potential starting points
# then we look in all 8 directions for the rest of the letters
# if we find a match, we increment our counter

# read input_Day4_test.txt for testing
with open("input_Day4.txt") as f:
    grid = [line.strip() for line in f.readlines()]

#print(grid)

# print
#for line in grid:
#    print(line)

XMAS_counter = 0
for line_index in range(len(grid)):
    for row_index in range(len(grid[line_index])):
        char = grid[line_index][row_index]

        # Search for "X" in right direction:
        if char == "X":
            # 1.look right
            if row_index + 3 < len(grid[line_index]):
                if (grid[line_index][row_index + 1] == "M" and
                    grid[line_index][row_index + 2] == "A" and
                    grid[line_index][row_index + 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going right")
                    XMAS_counter += 1
            # 2.look left
            if row_index - 3 >= 0:
                if (grid[line_index][row_index - 1] == "M" and
                    grid[line_index][row_index - 2] == "A" and
                    grid[line_index][row_index - 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going left")
                    XMAS_counter += 1
            # 3.look down
            if line_index + 3 < len(grid):
                if (grid[line_index + 1][row_index] == "M" and
                    grid[line_index + 2][row_index] == "A" and
                    grid[line_index + 3][row_index] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going down")
                    XMAS_counter += 1
            # 4.look up
            if line_index - 3 >= 0:
                if (grid[line_index - 1][row_index] == "M" and
                    grid[line_index - 2][row_index] == "A" and
                    grid[line_index - 3][row_index] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going up")
                    XMAS_counter += 1
            # 5.look down-right
            if line_index + 3 < len(grid) and row_index + 3 < len(grid[line_index]):
                if (grid[line_index + 1][row_index + 1] == "M" and
                    grid[line_index + 2][row_index + 2] == "A" and
                    grid[line_index + 3][row_index + 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going down-right")
                    XMAS_counter += 1
            # 6.look down-left
            if line_index + 3 < len(grid) and row_index - 3 >= 0:
                if (grid[line_index + 1][row_index - 1] == "M" and
                    grid[line_index + 2][row_index - 2] == "A" and
                    grid[line_index + 3][row_index - 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going down-left")
                    XMAS_counter += 1
            # 7.look up-right
            if line_index - 3 >= 0 and row_index + 3 < len(grid[line_index]):
                if (grid[line_index - 1][row_index + 1] == "M" and
                    grid[line_index - 2][row_index + 2] == "A" and
                    grid[line_index - 3][row_index + 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going up-right")
                    XMAS_counter += 1
            # 8.look up-left
            if line_index - 3 >= 0 and row_index - 3 >= 0:
                if (grid[line_index - 1][row_index - 1] == "M" and
                    grid[line_index - 2][row_index - 2] == "A" and
                    grid[line_index - 3][row_index - 3] == "S"):
                    #print(f"Found XMAS at ({line_index}, {row_index}) going up-left")
                    XMAS_counter += 1

print(f"Total XMAS found: {XMAS_counter}")



