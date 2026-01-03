# Looking for the instructions, you flip over the word search to find that this
# isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed
# to find two MAS in the shape of an X. One way to achieve that is like this:
#
# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram.
# Within the X, each MAS can be written forwards or backwards.

# read input_Day4_test.txt for testing
with open("input_Day4.txt") as f:
    grid = [line.strip() for line in f.readlines()]

#print(grid)

# print
for line in grid:
    print(line)

# This time, the center of attention is the "A" in the middle.
# we have the following cases to check:

# 1)
# M.S
# .A.
# M.S

# 2)
# M.M
# .A.
# S.S

# 3)
# S.M
# .A.
# S.M

# 4)
# S.S
# .A.
# M.M

# The Ms and Ss cannot be in the diagonal,
# this would read MAM and SAS instead of MAS.

# Also, we only search within a border of 1 around the grid,
# otherwise we get and index error.
XMAS_counter = 0
for line_index in range(1, len(grid)-1):
    for row_index in range(1, len(grid[line_index])-1):
        char = grid[line_index][row_index]

        # Search for "A" in center position:
        if char == "A":
            # Case 1
            if (grid[line_index - 1][row_index - 1] == "M" and
                grid[line_index - 1][row_index + 1] == "S" and
                grid[line_index + 1][row_index - 1] == "M" and
                grid[line_index + 1][row_index + 1] == "S"):
                #print(f"Found XMAS at ({line_index}, {row_index}) case 1")
                XMAS_counter += 1
            # Case 2
            if (grid[line_index - 1][row_index - 1] == "M" and
                grid[line_index - 1][row_index + 1] == "M" and
                grid[line_index + 1][row_index - 1] == "S" and
                grid[line_index + 1][row_index + 1] == "S"):
                #print(f"Found XMAS at ({line_index}, {row_index}) case 2")
                XMAS_counter += 1
            # Case 3
            if (grid[line_index - 1][row_index - 1] == "S" and
                grid[line_index - 1][row_index + 1] == "M" and
                grid[line_index + 1][row_index - 1] == "S" and
                grid[line_index + 1][row_index + 1] == "M"):
                #print(f"Found XMAS at ({line_index}, {row_index}) case 3")
                XMAS_counter += 1
            # Case 4
            if (grid[line_index - 1][row_index - 1] == "S" and
                grid[line_index - 1][row_index + 1] == "S" and
                grid[line_index + 1][row_index - 1] == "M" and
                grid[line_index + 1][row_index + 1] == "M"):
                #print(f"Found XMAS at ({line_index}, {row_index}) case 4")
                XMAS_counter += 1

print(f"Total XMAS found: {XMAS_counter}")