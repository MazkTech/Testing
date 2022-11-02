def menu():
    strChoice =""
    #create loop to display menu until user exits application 
    while strChoice != "X":
        #header for user
        print("-" * 50)
        print("Miss Othmar's class grades")
        print("-" * 50)
        print()
        print("D: Display grades")
        print("C: Calculate average")
        print("X: Exit")
        print()
        strChoice = input("Enter menu selection: ").upper()
        print()
        # user choice
        if strChoice == "D": #Calc Cost
            DisplayScores()
        elif strChoice == "C": #Display Prices
            CalcAverage()


def DisplayScores():
    file = open ("s.txt", "r")
    line = file.readline()
    while line != "":
        for i, item in enumerate(line,1):
            print(i, ':' + line)
        line = file.readline()
    file.close()
 
def CalcAverage():
    print("no")

menu()