
fd = open('input.txt')
#fd = open('input_small.txt')

depth = 0
horizontal = 0

for line in fd.readlines():
    move = line.strip().split()
    direction = move[0]
    value = int(move[1])

    if direction == 'forward':
        horizontal += value
    elif direction == 'up':
        depth -= value
    else:
        depth += value

print(f'Depth is {depth}, horizontal position is {horizontal}')
print(f'Product is {depth*horizontal}')
