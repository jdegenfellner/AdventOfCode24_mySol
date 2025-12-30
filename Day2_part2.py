# read lines from input_Day2.txt file
with open('input_Day2.txt', 'r') as file:
    lines = file.readlines()

#print(lines)

# remove newline characters from each line
lines = [line.strip() for line in lines]

#print(lines)

# split each line into a list of strings
lines = [line.split() for line in lines]

#print(lines)

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

# check if absolute differences between consecutive numbers is between 1 and 3:
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

# function to define safety:
def is_safe(nums):
    if is_strictly_increasing(nums) or is_strictly_decreasing(nums):
        if check_absolute_differences(nums):
            return True
    return False

# Now, the same rules apply as before, except if removing a
# single level from an unsafe report would make it safe, the report instead counts as safe.

# function to leave out the i-th element from the list
def leave_out_element(nums, i):
    return nums[:i] + nums[i+1:]

safe_counter_new = 0
for line in lines:
    if is_safe(line):
        safe_counter_new += 1
    else:
        # try leaving out each element and check if it becomes safe
        for i in range(len(line)):
            modified_line = leave_out_element(line, i)
            print(modified_line)
            if is_safe(modified_line):
                print("modified line:", modified_line)
                safe_counter_new += 1
                break  # no need to check further if we found a safe configuration

print(safe_counter_new)

# wrong: 944; That's not the right answer; your answer is too high.
# correct: 520