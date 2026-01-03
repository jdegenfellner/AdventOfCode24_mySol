# The notation X|Y means that if both page number X and page number Y are to be produced
# as part of an update, page number X must be printed at some point before page number Y.

# read input_Day5_test.txt
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# read
read_input("input_Day5_test.txt")

# print
def print_output(output):
    for line in output:
        print(line)

print_output(read_input("input_Day5_test.txt"))

# read in rules from input_Day5_test.txt
# form Number | Number
def read_rules(file_path):
    rules = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 2:
                rules.append((int(parts[0].strip()), int(parts[1].strip())))
    return rules


rules = read_rules("input_Day5.txt")
print("rules:")
print(rules)

# read updates from input_Day5_test.txt
# these are given after the first blank line and are comma separated:
def read_updates(file_path):
    list_of_updates = []
    updates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        blank_line_found = False
        for line in lines:
            if line.strip() == "":
                blank_line_found = True
                continue
            if blank_line_found:
                updates = [int(x.strip()) for x in line.strip().split(',')]
                #print(updates)
                list_of_updates.append(updates)
    return list_of_updates

updates = read_updates("input_Day5.txt")
print("updates:")
print(updates)

# function to check if two numbers of a rule are in an update
def check_rule_in_update(rule, update):
    return rule[0] in update and rule[1] in update

# function to check if a rule is satisfied in an update
def is_rule_satisfied(rule, update):
    if check_rule_in_update(rule, update):
        index_first = update.index(rule[0])
        index_second = update.index(rule[1])
        return index_first < index_second
    return True

# function to check if all rules are satisfied in an update
def are_all_rules_satisfied(rules, update):
    for rule in rules:
        if not is_rule_satisfied(rule, update):
            return False
    return True

# find all updates that satisfy all relevant rules
def find_satisfying_updates(rules, updates):
    satisfying_updates = []
    for update in updates:
        if are_all_rules_satisfied(rules, update):
            satisfying_updates.append(update)
    return satisfying_updates

satisfying_updates = find_satisfying_updates(rules, updates)
print("satisfying_updates:")
print(satisfying_updates)

# sum the middle elements of all satisfying updates
def sum_middle_elements(satisfying_updates):
    total_sum = 0
    for update in satisfying_updates:
        if len(update) % 2 == 1:
            middle_index = len(update) // 2
            total_sum += update[middle_index]
    return total_sum

total_sum = sum_middle_elements(satisfying_updates)
print("total_sum of middle elements:")
print(total_sum)

# take only updates not satisfying all rules
def find_non_satisfying_updates(rules, updates):
    non_satisfying_updates = []
    for update in updates:
        if not are_all_rules_satisfied(rules, update):
            non_satisfying_updates.append(update)
    return non_satisfying_updates

non_satisfying_updates = find_non_satisfying_updates(rules, updates)
print("non_satisfying_updates:")
print(non_satisfying_updates)

# function to take and update and switch two elements
def switch_elements(update, index1, index2):
    update[index1], update[index2] = update[index2], update[index1]
    return update

# function to find out which rules are violated in an update
def find_violated_rules(rules, update):
    violated_rules = []
    for rule in rules:
        if not is_rule_satisfied(rule, update):
            violated_rules.append(rule)
    return violated_rules

# now we need to fix all violated rules in the updates.
# for this update the violated rules and exchange the two elements in the update
# until all rules are satisfied
def fix_updates(rules, non_satisfying_updates):
    fixed_updates = []
    for update in non_satisfying_updates:
        violated_rules = find_violated_rules(rules, update)
        while violated_rules:
            for rule in violated_rules:
                index_first = update.index(rule[0])
                index_second = update.index(rule[1])
                if index_first > index_second:
                    update = switch_elements(update, index_first, index_second)
            violated_rules = find_violated_rules(rules, update)
        fixed_updates.append(update)
    return fixed_updates

fixed_updates = fix_updates(rules, non_satisfying_updates)
print("fixed_updates:")
print(fixed_updates)

# sum the middle elements of all fixed updates
total_sum_fixed = sum_middle_elements(fixed_updates)
print("total_sum of middle elements of fixed updates:")
print(total_sum_fixed)