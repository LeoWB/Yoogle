# NONLOCAL IMPORTS
import time

# LOCAL IMPORTS
from Functions import Log_In_1_1, Sign_In_1_1, Search_1_1, Calculate_1_1

# LOOP VARS
menuLoop = True

# MENU
print("Welcome to Yoogle 1.1")
time.sleep(2)

while menuLoop == True:
    print("\n  [0] - Log In\n  [1] - Sign Up\n  [2] - Search\n  [3] - Calculate\n  [!] - End")
    menuChoice = input("   > ")

    if menuChoice == "0":
        menuLoop = False

        # LOG IN
        Log_In_1_1.LogIn()
        
        menuLoop = True

    elif menuChoice == "1":
        menuLoop = False

        # SIGN UP
        Sign_In_1_1.SignIn()

        menuLoop = True

    elif menuChoice == "2":
        menuLoop = False

        # SEARCH
        Search_1_1.Search()

        menuLoop = True

    elif menuChoice == "3":
        menuLoop = False

        # CALCULATE
        Calculate_1_1.Calculate()

        menuLoop = True

    elif menuChoice == "!":
        menuLoop = False

    else:
        print("\nInvalid Entry -> Enter one of the numbers.\n")