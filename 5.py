import input

bps = input.lines(5)

def seatId(code: str) -> int:
    return int(code.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

ids = [seatId(x) for x in bps]

print(max(ids))

print([x for x in range(971) if x not in ids and x-1 in ids and x+1 in ids][0])