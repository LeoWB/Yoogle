def Calculate():

    calculateLoop = True

    print("\n~~ CALCULATE ~~")
    
    while calculateLoop == True:
        print("\n   [0] - Basic Operations\n   [1] - Geometry\n   [2] - Other\n   [!] - Back")
        calculateChoice = input("   > ")

        if calculateChoice == "0":
            calculateLoop = False
            
            # BASIC OPERATIONS
            

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
            print("\nInvalid Entry -> Enter one of the numbers or symbols.")