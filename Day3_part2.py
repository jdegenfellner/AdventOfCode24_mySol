import re # regular expressions

# read input_Day3_test.txt file
#with open('input_Day3_test_part2.txt', 'r') as file:
with open('input_Day3.txt', 'r') as file:
    lines = file.readlines()
# print the lines
for line in lines:
    print(line)

mult_pattern = r'mul\((\d+),\s*(\d+)\)'
pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"

# we need to look in sequence for do()/don't() and mult,
# as soon as a don't comes along, add_mult=False,
# as soon as a do comes along, add_mult=True

# function to find all dos and donts in a string; return TRUE if last is do, FALSE if last is don't
def last_do_or_dont(string, current_add_mult = True):
    do_spans = [m.span() for m in re.finditer(pattern_do, string)]
    dont_spans = [m.span() for m in re.finditer(pattern_dont, string)]
    # max begin position of do and don't
    last_do_pos = do_spans[-1][0] if do_spans else -1
    last_dont_pos = dont_spans[-1][0] if dont_spans else -1
    if last_do_pos > last_dont_pos:
        return True
    elif last_dont_pos > last_do_pos:
        return False
    else:
        return current_add_mult

multiplications_to_do = []
add_mult = True # true at the start
for line in lines:

    # find all mult, do, don't in the line
    pattern_mult = re.findall(mult_pattern, line)
    pattern_dos = re.findall(pattern_do, line)
    pattern_dont_s = re.findall(pattern_dont, line)

    # same with span.
    spanmults = [m.span() for m in re.finditer(mult_pattern, line)]
    spandos = [m.span() for m in re.finditer(pattern_do, line)]
    spandonts = [m.span() for m in re.finditer(pattern_dont, line)]

    #print(pattern_mult)
    #print(spanmults)
    #print(spandos)
    #print(spandonts)

    # go though all mults in the line and check if add_mult is true at that point
    for mult_span in spanmults:
        # check if any do or don't comes before this mult
        substring = line[:mult_span[0]]
        add_mult = last_do_or_dont(substring, add_mult)
        print(f"At mult {line[mult_span[0]:mult_span[1]]}, add_mult is {add_mult}")
        if add_mult:
            # extract the numbers from the mult
            mult_match = re.search(mult_pattern, line[mult_span[0]:mult_span[1]])
            if mult_match:
                num1 = int(mult_match.group(1))
                num2 = int(mult_match.group(2))
                multiplications_to_do.append((num1, num2))
                #print(f"Added multiplication: {num1} * {num2}")

print("Multiplications to do:", multiplications_to_do)
# calculate the result of all multiplications
result = 0
for num1, num2 in multiplications_to_do:
    result += num1 * num2
print("Final result:", result)











