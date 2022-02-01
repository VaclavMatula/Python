#Python project - clicker
import json

def into_dict ():
    global vars
    for variable in ["points", "buil01", "achi01", "upgr01"]:
        vars[variable] = eval(variable)

def new_game():

    global points
    global buil01
    global achi01
    global upgr01
    
    points = 0
    buil01 = 0
    achi01 = 0
    upgr01 = 0

vars = {}

new_game()
into_dict()

print(vars)
print (vars['points'])

with open('clickersave.txt', 'w') as convert_file:
     convert_file.write(json.dumps(vars))
