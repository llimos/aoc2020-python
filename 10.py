import input

adaptors = input.ints(10)
adaptors.sort()
adaptors.insert(0, 0)
adaptors.append(adaptors[-1] + 3)

ones = 0
threes = 0
i = 1
while i < len(adaptors):
    if adaptors[i] - adaptors[i - 1] == 3:
        threes += 1
    elif adaptors[i] - adaptors[i - 1] == 1:
        ones += 1
    i += 1

print(ones * threes)

# Part 2
# Work backwards from the end and count how many ways there are to get to the end for each one
combos = {
    len(adaptors)-1: 1 # One way to get to the endpoint from the endpoint
}
i = len(adaptors) - 2
while i >= 0:
    # Find all subsequent adaptors <= 3 away
    localCombos = 0
    # Check the next 3 for being <=3 away
    for n in range(i + 1, min(i + 4, len(adaptors))):
        if adaptors[n] <= adaptors[i] + 3:
            # For each one, look up in 'combos' the number of combos till the end
            localCombos += combos[n]
    # Add them together, and save in 'combos'
    combos[i] = localCombos

    i -= 1

print(combos[0])
