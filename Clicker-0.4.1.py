#Python project - clicker
import json
import ast
import os

def into_dict ():
    global vars
    for variable in ["points", "buil01", "buil02", "buil03", "buil04", "buil05", "buil06", "buil07", "buil08", "buil09", "buil10", "achi01", "upgr01", "x10"]:
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

    global x10

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

    x10 = 0

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

    global x10

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

    x10 = vars['x10']
vars = {}

if not os.path.isfile(f"C:\\Users\\{os.getlogin()}\\clickersave.txt"):
    new_game ()
    into_dict ()
    into_file()

out_from_file()
out_from_dict()

price_buil01 = 5+(0.2*buil01)
price_buil01 = round(price_buil01,1)

x10price_buil01 = 50+(2*(buil01 + 10))
x10price_buil01 = round(x10price_buil01,1)

gain_buil01 = 0.2*buil01
gain_buil01 = round(gain_buil01,1)

points = points + gain_buil01
points = round(points,1)



price_buil02 = 30+(2*buil02)
price_buil02 = round(price_buil02,1)

x10price_buil02 = 300+(20*(buil02 + 100))
x10price_buil02 = round(x10price_buil02,1)

gain_buil02 = 5*buil02
gain_buil02 = round(gain_buil02,1)

points = points + gain_buil02
points = round(points,1)


points = round(points,1)
print (f"\nYou have {points} points !")

if x10 == 1:
    print ("YOU ARE STILL IN x10 MODE, if u want to go out of x10 mode, u can type no x10.")

print ("\nIf u dont know what to do, u can type (h) for help")

control = input("What do u want to do ? : ")

if control == "h" or control ==  "cheat" or control ==  "c" or control ==  "b" or control ==  "b1" or control ==  "s" or control ==  "x10" or control ==  "no x10" or control ==  "b2":
    if control == "h":
       print ("Welcome to clicker ! \n If u want to start new game, type (s). If u want to click, type (c). If u want to open buy menu, u can type (b).")

    if control == "cheat":
       points += 1000

    if control == "c":
      points += 1
      points = round(points,1)

    if control == "b":
        print(f"\n BUY MENU: \n  If you want to buy 10 buildings at once, you can type (x10).")

        print(f"  You have {buil01} buidlings1, building1 will cost u {price_buil01}, in x10 mode 10 building1 will cost you {x10price_buil01}, you can buy it by typing (b1), buildings1 gain u {gain_buil01}")
        
    if control == "b1":
        if x10 == 0:
            if price_buil01 > points:
                print (f"Price of building1 is {price_buil01} points, but u have only {points} points")

            if price_buil01 <= points:
                points = points - price_buil01
                buil01 += 1
                print (f"You successfully bought building 1 ! Now u have {buil01} buildings1 \n")

        if x10 == 1:
            if x10price_buil01 > points:
                print (f"Price of 10 building1 is {x10price_buil01} points, but u have only {points} points")

            if x10price_buil01 <= points:
                points = points - x10price_buil01
                buil01 += 10
                print (f"You successfully bought 10 buildings1 ! Now u have {buil01} buildings1 \n")

    if control == "x10":
        x10 = 1
        print ("You are now in x10 mode")

    if control == "no x10":
        x10 = 0
        print ("You are now out of x10 mode")

    if control == "s":
        start_control = input("Are you sure you want to start new game ? This is going to wipe out all your progress ! Type (y) for yes or (n) for no : ")
        if start_control == "y":
            new_game ()
            into_file()
            print ("You have successfully wiped all your progress and started new game !")

        if start_control != "y":
           print("You have r still continuing this game !")         


else:
    print (f"\n THERE IS NO SUCH CONTROL AS ({control}) !\n")

points = round(points,1)
print (f"You have {points} points !\n")

into_dict()
into_file()
