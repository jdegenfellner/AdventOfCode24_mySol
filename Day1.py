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

distances = []
for i in range(len(list1)):
    distances.append( abs(int(list1[i]) - int(list2[i])) )

print("The sum of distances is: ", sum(distances))