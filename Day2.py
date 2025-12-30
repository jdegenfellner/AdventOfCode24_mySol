# read lines from input_Day2.txt file
with open('input_Day2.txt', 'r') as file:
    lines = file.readlines()

print(lines)

# remove newline characters from each line
lines = [line.strip() for line in lines]

print(lines)

# split each line into a list of strings
lines = [line.split() for line in lines]

print(lines)

# convert each string in the list to an integer
lines = [[int(num) for num in line] for line in lines]
print(lines)

# function to check if numbers are strictly increasing
def is_strictly_increasing(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

# strictly decreasing
def is_strictly_decreasing(nums):
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            return False
    return True

# check if absolute differences between consequtive numbers is between 1 and 3:
def check_absolute_differences(nums):
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

counter = 0
for line in lines:
    if is_strictly_increasing(line) or is_strictly_decreasing(line):
        if check_absolute_differences(line):
            counter += 1
print(counter)