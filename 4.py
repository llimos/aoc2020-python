import input
import re

data = input.get(4)
passports = [dict([y.split(':') for y in x.replace('\n', ' ').split(' ')]) for x in data.split('\n\n')]

req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Check for all required fields

print(len([pp for pp in passports if len([x for x in req if x not in pp]) == 0]))

def between(min, max):
    return lambda value: value.isdigit() and int(value) >= min and int(value) <= max
    

validations = {
    'byr': between(1920, 2002),
    'iyr': between(2010, 2020),
    'eyr': between(2020, 2030),
    'hgt': lambda value: (between(150, 193) if value[-2:] == 'cm' else between(59, 76))(value[:-2]),
    'hcl': lambda value: re.match(r"^#[a-f0-9]{6}$", value),
    'ecl': lambda value: value in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda value: re.match(r"^[0-9]{9}$", value)
}

def isValid(passport):
    return len([k for (k, v) in validations.items() if k not in passport or not v(passport[k])]) == 0

print(len([x for x in passports if isValid(x)]))