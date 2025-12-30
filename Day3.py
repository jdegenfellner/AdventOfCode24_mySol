# read input_Day3_test.txt file
with open('input_Day3.txt', 'r') as file:
    lines = file.readlines()
# print the lines
for line in lines:
    print(line.strip())

# now we need to parse line by line for a specific pattern:
# "mul(" , then a number, then a comma, then another number, then a closing parenthesis
import re # regular expressions
pattern = r'mul\((\d+),\s*(\d+)\)'
product_list = []
for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])
        product = num1 * num2
        product_list.append(product)
        print(f"Found multiplication: {num1} * {num2} = {product}")

# sum all the products
total_sum = sum(product_list)
print(f"The total sum of all products is: {total_sum}")

# correct: 174960292