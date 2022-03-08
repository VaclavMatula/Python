#Python project - Army typer
#warning: if u want to try some other versions,  u will have to detele the save file: "clickersave.txt" for the game to work
#for playtesting you can use type (cheat)

import json
import ast
import os

#build01 is soldier
#build02 is sniper
#build03 is tank
#buiůd04 is plane


def into_dict ():
    global vars
    for variable in ["points", "buil01", "buil02", "buil03", "buil04", "buil05", "buil06", "buil07", "buil08", "buil09", "buil10", "achi01", "achi02", "achi03", "achi04", "achi05", "achi06", "achi07", "achi08", "achi09", "achi10", "achi11", "achi12", "achi13", "achi14", "achi15", "achi16", "achi17", "achi18", "achi19", "achi20", "upgr01", "upgr02", "upgr03", "upgr04", "upgr05", "upgr06", "upgr07", "upgr08", "upgr09", "upgr10", "upgr11", "upgr12", "upgr13", "upgr14", "upgr15", "upgr16", "upgr17", "upgr18", "upgr19", "upgr20", "x10","pause"]:
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
    global achi02
    global achi03
    global achi04
    global achi05
    global achi06
    global achi07
    global achi08
    global achi09
    global achi10
    global achi11
    global achi12
    global achi13
    global achi14
    global achi15
    global achi16
    global achi17
    global achi18
    global achi19
    global achi20

    global upgr01
    global upgr02
    global upgr03
    global upgr04
    global upgr05
    global upgr06
    global upgr07
    global upgr08
    global upgr09
    global upgr10
    global upgr11
    global upgr12
    global upgr13
    global upgr14
    global upgr15
    global upgr16
    global upgr17
    global upgr18
    global upgr19
    global upgr20

    global x10
    global pause


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
    achi02 = 0
    achi03 = 0
    achi04 = 0
    achi05 = 0
    achi06 = 0
    achi07 = 0
    achi08 = 0
    achi09 = 0
    achi10 = 0
    achi11 = 0
    achi12 = 0
    achi13 = 0
    achi14 = 0
    achi15 = 0
    achi16 = 0
    achi17 = 0
    achi18 = 0
    achi19 = 0
    achi20 = 0

    upgr01 = 0
    upgr02 = 0
    upgr03 = 0
    upgr04 = 0
    upgr05 = 0
    upgr06 = 0
    upgr07 = 0
    upgr08 = 0
    upgr09 = 0
    upgr10 = 0
    upgr11 = 0
    upgr12 = 0
    upgr13 = 0
    upgr14 = 0
    upgr15 = 0
    upgr16 = 0
    upgr17 = 0
    upgr18 = 0
    upgr19 = 0
    upgr20 = 0

    x10 = 0
    pause = 0

    print("\n Welcome to army typer !")

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
    global achi02
    global achi03
    global achi04
    global achi05
    global achi06
    global achi07
    global achi08
    global achi09
    global achi10
    global achi11
    global achi12
    global achi13
    global achi14
    global achi15
    global achi16
    global achi17
    global achi18
    global achi19
    global achi20

    global upgr01
    global upgr02
    global upgr03
    global upgr04
    global upgr05
    global upgr06
    global upgr07
    global upgr08
    global upgr09
    global upgr10
    global upgr11
    global upgr12
    global upgr13
    global upgr14
    global upgr15
    global upgr16
    global upgr17
    global upgr18
    global upgr19
    global upgr20

    global x10
    global pause


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
    achi02 = vars['achi02']
    achi03 = vars['achi03']
    achi04 = vars['achi04']
    achi05 = vars['achi05']
    achi06 = vars['achi06']
    achi07 = vars['achi07']
    achi08 = vars['achi08']
    achi09 = vars['achi09']
    achi10 = vars['achi10']
    achi11 = vars['achi11']
    achi12 = vars['achi12']
    achi13 = vars['achi13']
    achi14 = vars['achi14']
    achi15 = vars['achi15']
    achi16 = vars['achi16']
    achi17 = vars['achi17']
    achi18 = vars['achi18']
    achi19 = vars['achi19']
    achi20 = vars['achi20']

    upgr01 = vars['upgr01']
    upgr02 = vars['upgr02']
    upgr03 = vars['upgr03']
    upgr04 = vars['upgr04']
    upgr05 = vars['upgr05']
    upgr06 = vars['upgr06']
    upgr07 = vars['upgr07']
    upgr08 = vars['upgr08']
    upgr09 = vars['upgr09']
    upgr10 = vars['upgr10']
    upgr11 = vars['upgr11']
    upgr12 = vars['upgr12']
    upgr13 = vars['upgr13']
    upgr14 = vars['upgr14']
    upgr15 = vars['upgr15']
    upgr16 = vars['upgr16']
    upgr17 = vars['upgr17']
    upgr18 = vars['upgr18']
    upgr19 = vars['upgr19']
    upgr20 = vars['upgr20']

    x10 = vars['x10']
    pause = vars['pause']

    
vars = {}


if not os.path.isfile(f"C:\\Users\\{os.getlogin()}\\clickersave.txt"):
    new_game ()
    into_dict ()
    into_file()

out_from_file()
out_from_dict()

while pause == 0:

    price_buil01 = 10+(5*buil01)
    price_buil01 = round(price_buil01,1)

    x10price_buil01 = 100+(50*(buil01) + 250)
    x10price_buil01 = round(x10price_buil01,1)

    gain_each_buil01 = 0.1
    gain_buil01 = gain_each_buil01*buil01
    gain_buil01 = round(gain_buil01,1)



    price_buil02 = 100+(50*buil02)
    price_buil02 = round(price_buil02,1)

    x10price_buil02 = 1000+(500*(buil02) + 2500)
    x10price_buil02 = round(x10price_buil02,1)

    gain_each_buil02 = 10
    gain_buil02 = gain_each_buil02*buil02
    gain_buil02 = round(gain_buil02,1)



    price_buil03 = 1000+(500*buil03)
    price_buil03 = round(price_buil03,1)

    x10price_buil03 = 10000+(5000*(buil03) + 25000)
    x10price_buil03 = round(x10price_buil03,1)

    gain_each_buil03 = 100
    gain_buil03 = gain_each_buil03*buil03
    gain_buil03 = round(gain_buil03,1)



    price_buil04 = 10000+(5000*buil04)
    price_buil04 = round(price_buil04,1)

    x10price_buil04 = 100000+(50000*(buil04) + 250000)
    x10price_buil04 = round(x10price_buil04,1)

    gain_each_buil04 = 1000
    gain_buil04 = gain_each_buil04*buil04
    gain_buil04 = round(gain_buil04,1)



    price_buil05 = 100000+(50000*buil05)
    price_buil05 = round(price_buil05,1)

    x10price_buil05 = 1000000+(500000*(buil05) + 2500000)
    x10price_buil05 = round(x10price_buil05,1)

    gain_each_buil05 = 1000
    gain_buil05 = gain_each_buil05*buil05
    gain_buil05 = round(gain_buil05,1)





    gain_together = gain_buil01 + gain_buil02 + gain_buil03 + gain_buil04 + gain_buil05
    gain_together = round(gain_together,1)

    points = points + gain_together
    points = round(points,1)

    if points >= 1:
        achi01 = "1"

    if buil01 >=10:
        achi02 = "1"

    points = round(points,1)
    print (f"\nYou have {points} points !")
    print(f"All your troops combined gain you {gain_together} points each run !")

    if x10 == 1:
        print ("You are still in x10 mode, if u want to go out of x10 mode, u can type (no x10).")

    print ("\nIf u dont know what to do, u can type (h) for help")

    control = input("What do u want to do ? : ")

    if control == "h" or control ==  "cheat" or control ==  "t" or control ==  "b" or control ==  "b1" or control ==  "s" or control ==  "x10" or control ==  "no x10" or control ==  "b2" or control ==  "b3" or control ==  "b4" or control ==  "b5" or control ==  "achi" or control ==  "up" or control == "pause" or control == "c":
        if control == "h":
            print ("Welcome to army typer! \n The goal of the game is to create a nuclear bomb and destroy your enemy. If you want to see controls, you can type (c)")

        if control == "c":
            print ("If you want to start new game, type (s). If you want to get a point, type (t). If you want to open buy menu, you can type (b). If you want to open achivements menu, you can type (achi). If you want to open upgrade menu, you can type (up).")

        if control == "cheat":
            cheat = int(input("How many points do u want to add ?: "))
            points = points + cheat

        if control == "t":
            points += 1
            points = round(points,1)
            print("You gained 1 point !")

        if control == "b":
            print(f"\n BUY MENU: \n")

            print(f"  You have {buil01} soldiers, soldier will cost you {price_buil01} points, in x10 mode 10 soldiers will cost you {x10price_buil01} points, you can buy soldier by typing (b1). Each soldier can gain you {gain_each_buil01} points. All soldeirs gain u {gain_buil01} points.")
            print(f"  You have {buil02} snipers, sniper will cost you {price_buil02} points, in x10 mode 10 sniper will cost you {x10price_buil02} points, you can buy sniper by typing (b2). Each sniper can gain you {gain_each_buil02} points. All snipers gain u {gain_buil02} points.")
            print(f"  You have {buil03} tanks, tank will cost you {price_buil03} points, in x10 mode 10 tanks will cost you {x10price_buil03} points, you can buy tank by typing (b3). Each tank can gain you {gain_each_buil03} points. All tanks gain u {gain_buil03} points.")
            print(f"  You have {buil04} planes, plane will cost you {price_buil04} points, in x10 mode 10 planes will cost you {x10price_buil04} points, you can buy plane by typing (b4). Each plane can gain you {gain_each_buil04} points. All planes gain u {gain_buil04} points.")
            print(f"  You have {buil05} nuclear bombs, nuclear bomb will cost you {price_buil05} points, in x10 mode 10 nuklear bombs will cost you {x10price_buil05} points, you can buy nuclear bomb by typing (b5). Each nuclear bomb gains can gain you {gain_each_buil05} points. All nuclear bombs gain u {gain_buil04} points.")
            print("If you want to buy 10 troops at once, you can type (x10).")
            print(" ")

        if control == "b1":
            if x10 == 0:
                if price_buil01 > points:
                    print (f"Price of soldier is {price_buil01} points, but u have only {points} points")

                if price_buil01 <= points:
                    points = points - price_buil01
                    buil01 += 1
                    print (f"You successfully bought soldier ! Now u have {buil01} soldiers \n")

            if x10 == 1:
                if x10price_buil01 > points:
                    print (f"Price of 10 soldiers is {x10price_buil01} points, but u have only {points} points")

                if x10price_buil01 <= points:
                    points = points - x10price_buil01
                    buil01 += 10
                    print (f"You successfully bought 10 soldiers ! Now u have {buil01} soldiers \n")

        if control == "b2":
            if x10 == 0:
                if price_buil02 > points:
                    print (f"Price of sniper is {price_buil02} points, but u have only {points} points")

                if price_buil02 <= points:
                    points = points - price_buil02
                    buil02 += 1
                    print (f"You successfully bought sniper ! Now u have {buil02} snipers \n")

            if x10 == 1:
                if x10price_buil02 > points:
                    print (f"Price of 10 snipers is {x10price_buil02} points, but u have only {points} points")

                if x10price_buil02 <= points:
                    points = points - x10price_buil02
                    buil02 += 10
                    print (f"You successfully bought 10 snipers ! Now u have {buil02} snipers \n")

        if control == "b3":
            if x10 == 0:
                if price_buil03 > points:
                    print (f"Price of tank is {price_buil03} points, but u have only {points} points")

                if price_buil03 <= points:
                    points = points - price_buil03
                    buil03 += 1
                    print (f"You successfully bought tank ! Now u have {buil03} tanks \n")

            if x10 == 1:
                if x10price_buil03 > points:
                    print (f"Price of 10 tank is {x10price_buil03} points, but u have only {points} points")

                if x10price_buil03 <= points:
                    points = points - x10price_buil03
                    buil03 += 10
                    print (f"You successfully bought 10 tanks ! Now u have {buil03} tanks \n")

        if control == "b4":
            if x10 == 0:
                if price_buil04 > points:
                    print (f"Price of plane is {price_buil04} points, but u have only {points} points")

                if price_buil04 <= points:
                    points = points - price_buil04
                    buil04 += 1
                    print (f"You successfully bought plane ! Now u have {buil04} planes \n")

            if x10 == 1:
                if x10price_buil04 > points:
                    print (f"Price of 10 planes is {x10price_buil04} points, but u have only {points} points")

                if x10price_buil04 <= points:
                    points = points - x10price_buil04
                    buil04 += 10
                    print (f"You successfully bought 10 planes ! Now u have {buil04} planes \n")

        if control == "b5":
            if x10 == 0:
                if price_buil05 > points:
                    print (f"Price of nuclear bomb is {price_buil05} points, but u have only {points} points")

                if price_buil05 <= points:
                    points = points - price_buil05
                    buil05 += 1
                    print (f"You successfully bought nuclear bomb ! Now u have {buil05} nuclear bombs \n")

            if x10 == 1:
                if x10price_buil05 > points:
                    print (f"Price of 10 nuclear bombs is {x10price_buil05} points, but u have only {points} points")

                if x10price_buil05 <= points:
                    points = points - x10price_buil05
                    buil05 += 10
                    print (f"You successfully bought 10 nuclear bombs ! Now u have {buil05} nuclear bombs \n")

        if control == "achi":
            print(f"\n ACHIVEMENTS MENU: \n")
            print("UNLOCKED ACHIVEMENTS:")

            if achi01 == "1":
                print("My first penny! (Get a point)")

                print(" ")

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

        if control == "up":
            print ("\n UPGRADE MENU:\n")
            print("There is no upgrades available yet, progress further in the game to unlock some of them.")

            if achi02 == "1":
                if upgr01 == "0":
                    print ("Grenades ! This upgrade allows you to equip your soldiers with grenades and increase their efficiency by 20%. You can buy it by typing (up1) for 100 points.")
            else:
                print("There is no upgrades yet.")
#        if control == "pause":
#            if pause == 0:
#                pause = 1
#                print("You have paused the game.")
#            else:
#                pause = 0
#                print("You have unpaused the game")
                
    else:
        print (f"\n THERE IS NO SUCH CONTROL AS ({control}) !\n")

    if buil05 == 1:
        win = input("YOU WON THE GAME !!!, now you can either continue the game by typing (continue) or start new game by typing (start)")
        if win == "continue":
            print ("cool")
        if win == start:
            new_game ()
            into_file()
            print ("You have successfully wiped all your progress and started new game !")
            new_game ()
            into_file()
    #points = round(points,1)
    #print (f"You have {points} points !\n")

    into_dict()
    into_file()
