#Python project - clicker

#def intodict ():
#    for variable in ["points", "build1", "achi1", "up1"]:
#        vars[variable] = eval(variable)

vars = {}

points = 50
build1 = 3
achi1 = 1
up1 = 0

for variable in ["points", "build1", "achi1", "up1"]:
    vars[variable] = eval(variable)

print(vars)
print (vars['points'])