import input
import re

rules = input.lines(7)

# build a dict of sets of parents and children
allowed_parents = {}
child_bags = {}
for rule in rules:
    (parent, children) = rule.rstrip('.').split(' bags contain ')
    child_bags[parent] = []

    if children == 'no other bags':
        continue
    
    children = children.split(', ')
    for child in [re.match(r"(\d*) (.*) bags?", x) for x in children]:
        if child.group(2) not in allowed_parents:
            allowed_parents[child.group(2)] = set()
        allowed_parents[child.group(2)].add(parent)

        child_bags[parent].append((int(child.group(1)), child.group(2)))

can_contain_mine = set()
def pop_can_contain(colour):
    for x in allowed_parents.get(colour, set()):
        can_contain_mine.add(x)
        pop_can_contain(x)

pop_can_contain('shiny gold')
print(len(can_contain_mine))


def total_bags(colour):
    return sum([num * (1 + total_bags(new_colour)) for (num, new_colour) in child_bags[colour]])

print(total_bags('shiny gold'))
