
data = open('depths.txt', 'r')
depths = data.readlines()
depths = [int(depth.strip()) for depth in depths]


num_increases = 0
last = None

for depth in depths:
    if not last:
        last = depth
        continue
    
    if depth > last:
        num_increases += 1
    last = depth

print(f"Answer: {num_increases}")
