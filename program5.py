weekday = 38.00
weekend = 42.00
twilight = 24.00
fltsubtotal = 0.00
fltservicefee = 0.7
def menu():
    strChoice =""
    while strChoice != "X":
        print("Menu of Options")
        print("-" * 50)
        print()
        print("C: Calculate Ticket Cost")
        print("D: Ticket Options")
        print("X: Exit")
        print()
        strChoice = input("What would you like to do?: ").upper()
        print()
        # user choice
        if strChoice == "C": 
            CalculatePrice()
        elif strChoice == "D": 
            DisplayOptions() 

def DisplayOptions():
    print("-" * 50)
    print("Ticket Options")
    print("-" * 50)
    print()
    print("Weekday     38.00")
    print("Weekend     42.00")
    print("Twilight    24.00")
    print()
    input("Please press enter to return to the menu:")

def CalcServiceFee(subtotal):
    ServiceFee = .07
    return subtotal * ServiceFee
def CalculatePrice():
    print("-" * 50)
    print("Ticket Price Calculator")
    print("-" * 50)
    print()
    print("Weekday     38.00")
    print("Weekend     42.00")
    print("Twilight    24.00")
    print()
    input("What ticket would you like?:")
    if input == 1:
        print( (weekend * fltservicefee))
menu()