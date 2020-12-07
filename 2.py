import input
import re

lines = input.lines(2)

def isValid1(line):
    (policy, password) = line.split(': ')
    (counts, letter) = policy.split(' ')
    (num1, num2) = [int(x) for x in counts.split('-')]
    matches = re.findall(letter, password)
    return len(matches) >= num1 and len(matches) <= num2

def isValid2(line):
    (policy, password) = line.split(': ')
    (counts, letter) = policy.split(' ')
    (num1, num2) = [int(x) for x in counts.split('-')]
    return (password[num1 - 1] == letter) != (password[num2 - 1] == letter)

print(len([x for x in lines if isValid1(x)]))
print(len([x for x in lines if isValid2(x)]))