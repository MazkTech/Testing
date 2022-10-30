
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
        if strChoice == "C": #calc ticket cost
           CalculatePrice()
        elif strChoice == "D": #Ticket options
            DisplayOptions() #calls for ticket options 

    
        else:
            subtotal=CalculatePrice()
            servicefee=CalcServiceFee(subtotal)
            total=subtotal+servicefee
            print("\nCost $")
            if input("\nPress enter to con"):
                return

def DisplayOptions():
    #blank spaces
    print("-" * 50)
    #display itcket options
    print("Ticket Options")
    print("-" * 50)
    print()
    #display prices for tickets
    print("Weekday     38.00")
    print("Weekend     42.00")
    print("Twilight    24.00")
    #user input
    print()
    input("Please press enter to return to the menu:")
#Funtion that gets service fee
def CalcServiceFee(subtotal):
    return subtotal*.07
       
        
def CalculatePrice():
      print("-" * 50)
      print("Ticket Price Calculator")
      print("-" * 50)
      int(input("Enter Ticket Option (1- Weekday,2 - Weekend, 3 - Twilight)"))
        
menu()