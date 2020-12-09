import input

numbers = [int(x) for x in input.lines(9)]

preamble_size = 25
i = preamble_size

while i < len(numbers):
    target = numbers[i]
    for first in range(i - preamble_size, i):
        for second in range(first + 1, i):
            if numbers[first] + numbers[second] == target:
                break
        else:
            continue
        break
    else:
        print(target)
        break
    i += 1

# Part 2
# Use sliding window
start = 0
end = 1
total = numbers[start] + numbers[end]
while start < len(numbers) - 1:
    if total == target:
        print(max(numbers[start:end+1]) + min(numbers[start:end+1]))
        break
    elif total < target:
        end += 1
        total += numbers[end]
    elif total > target:
        total -= numbers[start]
        start += 1
    