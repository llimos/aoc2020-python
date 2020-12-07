import input

numbers = [int(x) for x in input.lines(1)]

for index, num1 in enumerate(numbers):
    for num2 in numbers[index:]:
        if num1 + num2 == 2020:
            print(num1 * num2)
            break
    else:
        continue
    break

for index1, num1 in enumerate(numbers):
    for index2, num2 in enumerate(numbers[index1:]):
        if num1 + num2 < 2020:
            for num3 in numbers[index1+index2:]:
                if num1 + num2 + num3 == 2020:
                    print(num1 * num2 * num3)
                    break
            else:
                continue
            break
    else:
        continue
    break