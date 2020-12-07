import input

groups = input.get(6).split('\n\n')

# Get the uniques. Easiest way is to use a set
print(sum([len(set(list(x.replace('\n', '')))) for x in groups]))

def compare(lists):
    return lists[0].intersection(*lists)

print(sum([len(compare([set(list(y)) for y in x.splitlines()])) for x in groups]))