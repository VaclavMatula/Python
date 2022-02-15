#Python project - clicker
import json
import ast
import os

def into_dict ():
    global vars
    for variable in ["points", "buil01", "buil02", "buil03", "buil04", "buil05", "buil06", "buil07", "buil08", "buil09", "buil10", "achi01", "upgr01"]:
        vars[variable] = eval(variable)

def new_game():

    global points

    global buil01
    global buil02
    global buil03
    global buil04
    global buil05
    global buil06
    global buil07
    global buil08
    global buil09
    global buil10
        
    global achi01
    
    global upgr01
    
    points = 0

    buil01 = 0
    buil02 = 0
    buil03 = 0
    buil04 = 0
    buil05 = 0
    buil06 = 0
    buil07 = 0
    buil08 = 0
    buil09 = 0
    buil10 = 0

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

def out_from_dict():

    global points

    global buil01
    global buil02
    global buil03
    global buil04
    global buil05
    global buil06
    global buil07
    global buil08
    global buil09
    global buil10
    global achi01

    global upgr01

    points = vars['points']

    buil01 = vars['buil01']
    buil02 = vars['buil02']
    buil03 = vars['buil03']
    buil04 = vars['buil04']
    buil05 = vars['buil05']
    buil06 = vars['buil06']
    buil07 = vars['buil07']
    buil08 = vars['buil08']
    buil09 = vars['buil09']
    buil10 = vars['buil10']


    achi01 = vars['achi01']

    upgr01 = vars['upgr01']

vars = {}

if not os.path.isfile(f"C:\\Users\\{os.getlogin()}\\clickersave.txt"):
    new_game ()
    into_dict ()
    into_file()

out_from_file()
out_from_dict()

print ("\nIf u dont know what to do, u can type (h) for help\n")
control = input("What do u want to do ? : ")

if control == "h":
    print ("Welcome to clicker ! \n If u want to start new game, type (s). If u want to click, type (c). If u want to open buy menu, u can type (b). If u want to buy a building, type: (b1) for building 1")

if control == "s":
    new_game ()
    into_file()

if control == "c":
    points += 1

if control == "b":
    print(f"You have {buil01} buidlings 1")

if control == "b1":
    pass

print (f"You have {points} points")

into_dict()
into_file()
