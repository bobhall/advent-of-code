
data = open('depths.txt', 'r')
depths = data.readlines()
depths = [int(depth.strip()) for depth in depths]


num_increases = 0
last = None


for ix in range(0, len(depths)-2):
    group = depths[ix:ix+3]
    group_sum = sum(group)

    if last and group_sum > last:
        num_increases += 1
        
    last = group_sum


print(f"Answer: {num_increases}")
