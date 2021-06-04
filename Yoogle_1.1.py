# IMPORTS
import time

# LOOP VARS
menuLoop = True

# MENU
while menuLoop == True:
    print("Welcome to Yoogle 1.1")
    time.sleep(2)
    print("\n   [0] - Log In\n   [1] - Sign Up\n   [2] - Search\n   [3] - Calculate")
    menuChoice = input("   > ")

    if menuChoice == "0":
        menuLoop = False

        # LOG IN
        pass

    elif menuChoice == "1":
        menuLoop = False

        # SIGN UP
        pass

    elif menuChoice == "2":
        menuLoop = False

        # SEARCH
        pass

    elif menuChoice == "3":
        menuLoop = False

        # CALCULATE
        pass

    else:
        print("\nInvalid Entry -> Enter one of the numbers.\n")