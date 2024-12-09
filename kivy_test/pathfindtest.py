from pathfinding.core.grid import Grid
from pathfinding.finder.best_first import BestFirst

import json

matrix = []
true_map=[]
a=0
with open('projectDungeoneering/config/new_testmap.json',encoding='utf-8') as jsonfile:
    matrix=json.load(jsonfile)
for i in matrix["1"]:
    true_map.append([])
    for j in range(len(i)-1):
        true_map[a].append(int(i[j]))
    a+=1
grid = Grid(matrix = true_map)


start = grid.node(7,7)
end = grid.node(43,34)
finder = BestFirst()
path,runs = finder.find_path(start,end,grid)

print(str(path))