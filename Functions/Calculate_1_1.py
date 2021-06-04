def Calculate():
    # FUNCTIONS
    def BasicOperations():

        basicOperationsLoop = True

        print("\n~~ BASIC OPERATIONS ~~\n    + = Add\n    - = Minus\n    * = Multiply\n    / = Divide\n    ** = To the power of\n    % = Modulus\n\n    ! = Back")

        while basicOperationsLoop == True:
            calculation = input("\n    > ")
            
            try:
                exec(f"\nprint({calculation})")
            except:
                if calculation == "!":
                    basicOperationsLoop = False
                else:
                    print("\nERR: Invalid Entry -> Incorrect Syntax")

    # LOOP VARS
    calculateLoop = True

    # CALCULATE
    while calculateLoop == True:
        print("\n~~ CALCULATE ~~\n   [0] - Basic Operations\n   [1] - Geometry\n   [2] - Other\n\n   [!] - Back")
        calculateChoice = input("\n   > ")

        if calculateChoice == "0":
            calculateLoop = False
            
            # BASIC OPERATIONS
            BasicOperations()

            calculateLoop = True

        elif calculateChoice == "1":
            calculateLoop = False

            # GEOMETRY


            calculateLoop = True

        elif calculateChoice == "2":
            calculateLoop = False
            
            # OTHER

            
            calculateLoop = True

        elif calculateChoice == "!":
            calculateLoop = False

        else:
            print("\nERR: Invalid Entry -> Enter one of the numbers or symbols.")

