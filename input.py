import os

def get(puzzle):
    return open(os.path.join(os.path.dirname(__file__), 'inputs/{}.txt'.format(puzzle))).read()

def lines(puzzle):
    return get(puzzle).rstrip().split('\n')