import input
import copy

class Computer:
    program: list
    acc = 0
    pos = 0

    def __init__(self, program: list):
        self.program = program
    
    def step(self):
        if self.pos > len(self.program):
            return True
        (cmd, param) = self.program[self.pos].split(' ')
        param = int(param)
        if cmd == 'acc':
            self.acc += param
        self.pos += param if cmd == 'jmp' else 1
        return False

program = input.lines(8)
computer = Computer(program)

pos = 0
jmpsAndNops = []
while (True):
    if computer.program[pos].split(' ')[0] in {'jmp', 'nop'}:
        jmpsAndNops.append(pos)
    computer.step()
    newPos = computer.pos
    computer.program[pos] = None
    pos = newPos
    if computer.program[pos] == None:
        break

print(computer.acc)

print(jmpsAndNops)
# We now backtrack through the jmpsAndNops and try changing them to see what happens
while len(jmpsAndNops):
    posToTest = jmpsAndNops.pop()
    testProgram = input.lines(8)
    testProgram[posToTest] = testProgram[posToTest].replace('jmp', 'nop') if testProgram[posToTest].startswith('jmp') else testProgram[posToTest].replace('nop', 'jmp')
    testComputer = Computer(testProgram)

    testPos = 0
    halted = False
    while not halted:
        halted = testComputer.step()
        testComputer.program[testPos] = None
        testPos = testComputer.pos
        if testPos >= len(testComputer.program):
            print(posToTest, 'Halted', testComputer.acc)
            break
        if testComputer.program[testPos] == None:
            # Found loop
            break
    if halted:
        print(posToTest, 'Halted', testComputer.acc)
        break;
    else:
        print(posToTest, 'Has loop', testComputer.acc)
