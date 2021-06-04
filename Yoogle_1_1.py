# NONLOCAL IMPORTS
import time

# LOCAL IMPORTS
from Functions import Log_In_1_1, Sign_In_1_1, Search_1_1, Calculate_1_1

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
        Log_In_1_1.LogIn()

    elif menuChoice == "1":
        menuLoop = False

        # SIGN UP
        Sign_In_1_1.SignIn()

    elif menuChoice == "2":
        menuLoop = False

        # SEARCH
        Search_1_1.Search()

    elif menuChoice == "3":
        menuLoop = False

        # CALCULATE
        Calculate_1_1.Calculate()

    else:
        print("\nInvalid Entry -> Enter one of the numbers.\n")