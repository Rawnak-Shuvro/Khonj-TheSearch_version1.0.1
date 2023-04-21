import random

print("\n\t\t\t\t\t\t\tKHONJ: THE SEARCH!!!")
print("\n\t\t\t\t\t\t\t Version 1.0.1\n")

while not False:
    score = 0

    MENU = input("Enter MENU to see the chart: ")
    menu = MENU.lower().strip()

    if menu == "menu":
        print("\nLEVEL")
        print("HELP")
        print("QUIT\n")

        MENU_TYPE = input("Enter MENU TYPE: ")
        menu_type = MENU_TYPE.lower().strip()

        if menu_type == "level":
            print("\nEASY")
            print("INTERMEDIATE")
            print("DIFFICULT\n")

            LEVEL_TYPE = input("Enter LEVEL TYPE: ")
            level_type = LEVEL_TYPE.lower().strip()

            if level_type == "easy":
                print("\nROUND 1")
                print("ROUND 2\n")

                ROUND = input("Enter ROUND NUMBER: ")
                round = ROUND.lower().strip()

                if round == "round 1":
                    randomNum = random.randrange(1, 50)

                    print("\n\t\t\t\t\tThe random number is between 1 to 50.")
                    print("\t\t\t\t\t\t   Try in 10 times!")
                    print("\t\t\t\t\t\t     Let's Start!")

                    for i in range(randomNum):

                        if i == 10:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)
                        if gamerNum > randomNum:

                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break

                elif round == "round 2":
                    randomNum = random.randrange(1, 100)

                    print("\n\t\t\t\t\tThe random number is between 1 to 100.")
                    print("\t\t\t\t\t\t   Try in 10 times!")
                    print("\t\t\t\t\t\t     Let's Start!")

                    for i in range(randomNum):

                        if i == 10:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)

                        if gamerNum > randomNum:
                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break
                else:
                    print("Please try again!")

            elif level_type == "intermediate":
                print("\nROUND 1")
                print("ROUND 2\n")

                ROUND = input("Enter ROUND NUMBER: ")
                round = ROUND.lower().strip()

                if round == "round 1":
                    randomNum = random.randrange(1, 500)

                    print("\n\t\t\t\t\tThe random number is between 1 to 500.")
                    print("\t\t\t\t\t\t   Try in 10 times!")
                    print("\t\t\t\t\t\t     Let's Start!")

                    for i in range(randomNum):

                        if i == 10:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)

                        if gamerNum > randomNum:
                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break

                elif round == "round 2":
                    randomNum = random.randrange(1, 1000)

                    print("\n\t\t\t\t\tThe random number is between 1 to 1000.")
                    print("\t\t\t\t\t\t   Try in 10 times!")
                    print("\t\t\t\t\t\t     Let's Start!")

                    for i in range(randomNum):

                        if i == 10:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)

                        if gamerNum > randomNum:
                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break
                else:
                    print("Please try again!")

            elif level_type == "difficult":
                print("\nROUND 1")
                print("ROUND 2\n")

                ROUND = input("Enter ROUND or QUIT to exit : ")
                round = ROUND.lower().strip()

                if round == "round 1":
                    randomNum = random.randrange(1, 5000)

                    print("\n\t\t\t\t\tThe random number is between 1 to 5000.")
                    print("\t\t\t\t\t\t    Try in 5 times!")
                    print("\t\t\t\t\t\t      Let's Start!")

                    for i in range(randomNum):

                        if i == 5:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)

                        if gamerNum > randomNum:
                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break

                elif round == "round 2":
                    randomNum = random.randrange(1, 10000)

                    print("\n\t\t\t\t\tThe random number is between 1 to 10000.")
                    print("\t\t\t\t\t\t    Try in 5 times!")
                    print("\t\t\t\t\t\t      Let's Start!")

                    for i in range(randomNum):

                        if i == 5:
                            print("GAME OVER!")
                            break

                        else:
                            print(i + 1)

                            gamerNum = input("Enter the number : ")
                            gamerNum = int(gamerNum)

                        if gamerNum > randomNum:
                            print("Your number is big!")
                            continue

                        elif gamerNum < randomNum:
                            print("Your number is small!")
                            continue

                        elif gamerNum == randomNum:
                            print("Bravo!!!\n")
                            break
                else:
                    print("Please try again!")
                    continue

        elif menu_type == "help":
            with open("help.txt", "r") as ht:
                help = ht.read()
                print(help)
                continue

        elif menu_type == "quit":
            print("Thank You!")
            break

        else:
                print("Please try again!")
                continue
    else:
        print("Please try again!")
        continue
    