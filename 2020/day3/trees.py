
from functools import reduce

def main():
    fd = open('path.txt')
    path = fd.readlines()
    path = [p.strip() for p in path]

    patterns = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    num_trees = map(lambda pattern: count_trees(path, pattern), patterns)
    print(reduce(lambda x,y: x*y, num_trees))
    


def count_trees(path, travel_pattern):
    rightward_move = travel_pattern[0]
    downward_move = travel_pattern[1]
    width = len(path[0])
    
    count = 0
    curr_x = 0
    curr_y = 0

    while curr_y < len(path):
        if path[curr_y][curr_x] == '#':
            count += 1
        curr_x, curr_y = get_next_position(curr_x, curr_y, width, rightward_move, downward_move)
    return count
    

def get_next_position(curr_x, curr_y, width, rightward_offset=3, downward_offset=1):
    next_y = curr_y + downward_offset
    next_x = (curr_x + rightward_offset) % width
    return next_x, next_y

if __name__ == '__main__':
    main()
