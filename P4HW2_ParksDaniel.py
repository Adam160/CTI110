# CTI-110
# P3HW2 - Pizza Order
# Daniel Parks 
# 20 MAR 2022
#
#
# Program asks for number of students you want to order pizza for and number of people per pizza.
# Program identifies valid entries. Number of people = 1.5, 2 or 3.
#   Program calculates number of pizzas needed and rounds value up if decimal.
#       Individual pizza cost = $5 per pizza. Tax = 6%.
#   PRINT results.
#   Asks user if they would like to restart program - "y" = restart, anything else = exit.
# Program identifies invalid entries.
#   PRINT invalid entry result.
# RESTART program.
#
#
# IMPORT MATH FUNCTION. 
import math

# SET PROGRAM FUNCTION.
def main():

    # IDENTIFY VARIABLES AND ASK FOR USER INPUT.
    NumberOfStudents = float(input("How many students do you want to order pizza for? "))
    PeoplePerPizza = float(input("Enter number of people per pizza ( 1.5, 2, 3): "))

    # IDENTIFY VALID ENTRIES.
    if (PeoplePerPizza == 3) or (PeoplePerPizza == 2) or (PeoplePerPizza == 1.5):
        
        # CALCULATE VALID ENTRY OUTPUTS.
        NumberOfPizzas = NumberOfStudents / PeoplePerPizza
        
        PizzaCostNT = (math.ceil(NumberOfPizzas) * 5)
        PizzaTax = (PizzaCostNT *1.06)

        # DISPLAY VALID ENTRY RESULTS.
        print()
        print("----Pizza Order----------")
        print("Number of Students : ",  f'{NumberOfStudents:.0f}')
        print("Pizzas Needed : ", math.ceil(NumberOfPizzas))
        print("Price $", f'{PizzaTax:.2f}')
        print("-------------------------")
        print()
        
        # IDENTIFY USER INPUT FOR RESTART.
        Restart = input("Whould you like to run program again (y for yes): | \n")
        # If user input is "y", restart program.
        if Restart == 'y': 
            main()
        # AMY OTHER ENTRY, EXIT PROGRAM.
        else:
            print("\nThank you for your order! \n")
            Restart = input()
            exit()

    # IDENTIFY INVALID ENTRY.
    else:
        print()
        print("INVALID ENTRY!!!!")
        print("You should have entered 1.5, 2 or 3.")
        print()
        print("Run Program again.")
        print()



# RESTART PROGRAM.
main()
