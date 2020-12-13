import input

(time, buses) = input.lines(13)
time = int(time)
buses = [int(x) for x in buses.split(',') if x != 'x']
print(buses)
print([x - (time % x) for x in buses])