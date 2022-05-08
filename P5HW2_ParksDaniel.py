# Find the answer of randomly generated numbers added or subtracted together.
# 28 April 2022
# CTI-110 P5HW2 - Math Quiz
# Daniel Parks
#
import random
#Project/Application header.
print("Welcome to Math Quiz")

#Identify fuction for addition of random numbers.
def addRandomNumbers():
    #Set the attempt number as 1.
    attempt = 1
    #Set random numbers 1 & 2, 1- 100 and display.
    n1=random.randint(0,100)
    n2=random.randint(0,100)

    print(f"{n1:>6}")
    print(f"+{n2:>5}")
    #Enter User Answer.
    print("Enter answer.")
    ans=int(input())

    #Add paramaters for incorrect answers. 
    while ans!=n1+n2:    
        #Add attempt number.
        attempt += 1           

        #Answers too low.
        if ans<n1+n2:
            print("Sorry, guess is too low.")  
        #Answers too high.
        else:
            print("Sorry, guess is too high")
        #Ask for next attempt.
        ans=int(input("try again : "))

    #Print Correct answer response/number of attempts.
    print("Congratulations!!!! your answer is correct..")
    print("Number of guesses: ", attempt )

#Identify fuction for subtraction of random numbers.
def sbutractRandomNumbers():
    #Set the attempt number as 1.
    attempt = 1
    #Set random numbers 1 & 2, 1- 100 and display.
    n1=random.randint(0,100)
    n2=random.randint(0,100)

    print(f"{n1:>6}")
    print(f"-{n2:>5}")
    #Enter User Answer.
    print("Enter answer.")
    ans=int(input())
      
    #Add paramaters for incorrect answers. 
    while ans!=n1-n2:
        #Add attempt number.         
        attempt += 1           
        #Answers too low.
        if ans<n1-n2:
            print("Sorry, guess is too low.")  
        #Answers too high.
        else:
            print("Sorry, guess is too high")
        #Ask for next attempt.
        ans=int(input("try again : "))

    #Print Correct answer response/number of attempts.
    print("Congratulations!!!! your answer is correct..")
    print("Number of guesses: ", attempt)

#Load nmenu.
if __name__=="__main__":

    while 1:
        #Display nmenu.
        print("MAIN MENU")
        print("----------------------")
        print("1. Add Random Numbers ")
        print("2. Subtract Random Numbers")
        print("3. Exit")
        num=int(input("Please choose one of the menu options: "))
        #Identify menue user entry.
        #User enter "3" = end program.
        if num==3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        #user enter "1" = load "addRandomNumbers".
        if num==1:
            addRandomNumbers()
        #If user enters "2" = load "sbutractRandomNumbers"
        if num==2:
            sbutractRandomNumbers()