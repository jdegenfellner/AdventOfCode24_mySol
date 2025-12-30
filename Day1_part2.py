# This time, you'll need to figure out exactly how often each number
# from the left list appears in the right list. Calculate a total similarity
# score by adding up each number in the left list after multiplying it by the
# number of times that number appears in the right list.

# read input_Day1.txt file
with open('input_Day1.txt', 'r') as file:
    lines = file.readlines()

# remove line breaks '\n' from each line
lines = [line.strip() for line in lines]
print(lines)

list1 = []
list2 = []
for line in lines:
    list1.append(line.split()[0])
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()

# function to find how often the current element of list1 appears in list2
def count_occurrences(element, lst):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

similarity_score = 0
for number in list1:
    occurrences = count_occurrences(int(number), list2)
    similarity_score += int(number) * occurrences

print("The total similarity score is: ", similarity_score)