#Python project - clicker
import json
import ast

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

def into_file():
    with open('clickersave.txt', 'w') as convert_file:
        convert_file.write(json.dumps(vars))

def outoffile():
    file = open("clickersave.txt", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()

    global output
    output = (dictionary)
    print (output['points'])
    print (output)
    
output = {}
vars = {}

new_game()
into_dict()
into_file()
outoffile()

print (output['points'])
#print(vars)
#print (vars['points'])
