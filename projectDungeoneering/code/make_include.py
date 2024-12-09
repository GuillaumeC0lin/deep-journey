import os

dir_paths = ['\\classes\\','\\foes\\','\\interface\\','\\npc\\','\\tools\\']

res = []
cur_path = os.path.dirname(os.path.abspath(__file__))
for dir_path in dir_paths:
    for path in os.listdir(cur_path+dir_path):
        if os.path.isfile(os.path.join(cur_path+dir_path, path)):
            if(".py" in path):
                res.append(dir_path,path)

for one_res in res:
    one_res[0].replace("\\",".")
    one_res[1].replace(".py","")
    print(one_res) ##replace to go for the include.py
print(res)