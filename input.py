import os

def get(puzzle):
    return open(os.path.join(os.path.dirname(__file__), 'inputs/{}.txt'.format(puzzle))).read()

def lines(puzzle):
    return get(puzzle).rstrip().split('\n')

def ints(puzzle):
    return [int(x) for x in lines(puzzle)]

def floats(puzzle):
    return [float(x) for x in lines(puzzle)]