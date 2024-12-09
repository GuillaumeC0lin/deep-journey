from random import randint

def generate_grid(size_x,size_y):
    grid = ["#"*size_x for i in range(size_y)]
    return grid

def make_room_empty(grid,size,pos):     ##size is (x,y) pos is top-left (x,y)
    empty = '.'
    grid_copy = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i < pos[0]+size[0] and i >=pos[0]:
                if j < pos[1]+size[1] and j >= pos [1]:
                    grid_copy[i] = grid_copy[i][:j] + empty + grid_copy[i][j + 1:]
    return grid_copy

def make_big_corridor(grid,length,pos,dir): # dir is 1-4 on a 4 pointed counterclockwise star pattern starting from the top
    grid_copy = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            match(dir):
                case 3:
                    if i>= pos[0] and i<pos[0]+length:
                        if j == pos[1]+1:
                            grid_copy[i] = grid_copy[i][:j] + "." + grid_copy[i][j + 1:]
                        if j == pos[1]:
                            grid_copy[i] = grid_copy[i][:j] + "W" + grid_copy[i][j + 1:]
                case 1:
                    if i>= pos[0]-length and i<pos[0]:
                        if j == pos[1]:
                            grid_copy[i] = grid_copy[i][:j] + "." + grid_copy[i][j + 1:]
                        if j == pos[1]+1:
                            grid_copy[i] = grid_copy[i][:j] + "W" + grid_copy[i][j + 1:]
                case 4:
                    if j>= pos[1] and j<pos[1]+length:
                        if i == pos[0]:
                            grid_copy[i] = grid_copy[i][:j] + "." + grid_copy[i][j + 1:]
                        if i == pos[0]+1:
                            grid_copy[i] = grid_copy[i][:j] + "W" + grid_copy[i][j + 1:]
                case 2:
                    if j>= pos[1]-length and j<pos[1]:
                        if i == pos[0]+1:
                            grid_copy[i] = grid_copy[i][:j] + "." + grid_copy[i][j + 1:]
                        if i == pos[0]:
                            grid_copy[i] = grid_copy[i][:j] + "W" + grid_copy[i][j + 1:]
    return grid_copy

def random_rooms(room_list,size):
    err = 0
    ((x,y),(sizex,sizey)) = ((randint(1,size-5),randint(1,size-5)),(randint(5,9),randint(5,9)))
    while ((x+sizex > size or y+sizey > size) or err ==1):
        err = 0
        ((x,y),(sizex,sizey)) = ((randint(1,size-5),randint(1,size-5)),(randint(5,9),randint(5,9)))
        for i in room_list:
            if((i[0][0]+i[1][0] < x -2 or x +sizex < i[0][1] - 2)) :
                err = 1
            if ( i[0][1]+i[1][1] < y -2 or i[0][1] -2 > y+sizey):
                err = 1
    return ((x,y),(sizex,sizey))



if __name__ == '__main__':
    max_size = 100
    grid = generate_grid(max_size,max_size)
    rooms = []
    for i in range(randint(15,20)):
        ((x,y),(sizex,sizey)) = random_rooms(rooms,max_size)
        rooms.append(((x,y),(sizex,sizey)))
        grid = make_room_empty(grid,(sizex,sizey),(x,y))
    for j in grid:
        print(j)