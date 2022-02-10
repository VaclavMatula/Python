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

def out_from_file():
    file = open("clickersave.txt", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()

    global vars
    vars = (dictionary)
    #print (output['points'])
    #print (output)

def out_from_dict():

    global points
    global buil01
    global achi01
    global upgr01

    points = vars['points']
    buil01 = vars['buil01']
    achi01 = vars['achi01']
    upgr01 = vars['upgr01']

vars = {}

out_from_file()
out_from_dict()

control = input("What do u want to do ?\n ((h) for help) : ")

if control == "h":
    print ("Welcome to clicker ! \n If u want to start new game, type (s). If u want to click, type (c).")

if control == "s":
    new_game ()
    into_file()

if control == "c":
    points += 1

print (f"You have {points} points")

into_dict()
into_file()

#print (c_save['points'])
#print(vars)
#print (vars['points'])
