def Calculate():
    # NONLOCAL IMPORTS
    import math
    import time

    # FUNCTIONS
    def BasicOperations():

        basicOperationsLoop = True

        print("\n~~ BASIC OPERATIONS ~~\n    + = Add\n    - = Minus\n    * = Multiply\n    / = Divide\n    ** = To the power of\n    % = Modulus\n\n    ! = Back")

        while basicOperationsLoop == True:
            calculation = input("\n----> ")
            
            try:
                exec(f"\nprint({calculation})")
            except:
                if calculation == "!":
                    basicOperationsLoop = False
                else:
                    print("\nERR: Invalid Entry -> Incorrect Syntax")

    def Geometry():

        geometryLoop = True

        while geometryLoop == True:

            print("\n~~ GEOMETRY ~~\n    [0] - Circle Area\n    [1] - Trapezium Area\n    [2] - Pythagorean Theorem\n\n    [!] - Back")

            geometryChoice = input("\n----> ")

            if geometryChoice == "0":
                circleRadius = input("~~ CIRCLE AREA ~~\nEnter Radius\n-----> ")
                
                try:
                    print((int(circleRadius) ** 2) * math.pi)
                except:
                    print("\nERR: Invalid Entry -> Enter a number")
                time.sleep(2)

            elif geometryChoice == "1":
                trapeziumValues = input("~~ TRAPEZIUM AREA ~~\n Enter [a], [b], [height]\n-----> ").split(', ')

                try:
                    a = int(trapeziumValues[0])
                    b = int(trapeziumValues[1])
                    height = int(trapeziumValues[2])

                    print(((a + b) * height) / 2)
                except:
                    print("\nERR: Invalid Entry -> Enter a number / Incorrect Formatting")
                time.sleep(2)

            elif geometryChoice == "2":
                pythagoreanValues = input("~~ PYTHAGOREAN THEOREM ~~\nEnter [a], [b]\n-----> ").split(', ')

                try:
                    a = int(pythagoreanValues[0])
                    b = int(pythagoreanValues[1])

                    print(math.sqrt((a * a) + (b * b)))
                except:
                    print("\nERR: Invalid Entry -> Enter a number / Incorrect Formatting")
                time.sleep(2)

            elif geometryChoice == "!":
                geometryLoop = False


    # LOOP VARS
    calculateLoop = True

    # CALCULATE
    while calculateLoop == True:
        print("\n~~ CALCULATE ~~\n   [0] - Basic Operations\n   [1] - Geometry\n   [2] - Other\n\n   [!] - Back")
        calculateChoice = input("\n---> ")

        if calculateChoice == "0":
            calculateLoop = False
            
            # BASIC OPERATIONS
            BasicOperations()

            calculateLoop = True

        elif calculateChoice == "1":
            calculateLoop = False

            # GEOMETRY
            Geometry()

            calculateLoop = True

        elif calculateChoice == "2":
            calculateLoop = False
            
            # OTHER

            
            calculateLoop = True

        elif calculateChoice == "!":
            calculateLoop = False

        else:
            print("\nERR: Invalid Entry -> Enter one of the numbers or symbols.")