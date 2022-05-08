# P5HW1 - Score List
# 26 April 2022
# CTI-110 P5HW1 - Score List
# Daniel Parks
#
# This program displays a menu for the user to create a list and evaluate data manipulation.
# PLEASE HELP! -  I have been working on this code for over a week and cannot seem to correct the major issue I have with the code.
#                 The issue this program has is that you cannot display the results with an empty list. If the list is empty, the program 
#                 "should" display the menu, instead I get an error. There are 2 ways to get this error;
#                        1) Create a list and display the results until the list data is extinguished and instead of displaying the menu
#                               at the end, you get an error. 
#                        2) Bypass creating a list and initially try to display the results with no list.
# PLEASE HELP! - Regardless of grade, I want to know what I'm doing wrong.


# Identify Letter Grade.
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Set list
scores = []

# Create user input for list.
def createList():
    # Identify how many tests.
    NumOfScores = int(input("How many scores do you want to enter? "))
    for i in range(1, NumOfScores+1):
        while True:
                IndividualScore = int(input("Enter score {}: ".format(i)))
                # Set range of scores.
                if IndividualScore >= 0 and IndividualScore <=100:
                    # Add user input as list score.
                    scores.append(IndividualScore)
                    break
                # Print Error if invalid entry.
                else:
                    print()
                    print("INVALID Score entered!!!!")
                    print("Score should be between 0 and 100")
                    print()
        continue
# Evaluate Data.
def analyseData(scores):
    # If list was not created, display no new list created.
    if scores==None:
        print("New list was not created.")
        
        return  0,0,0,0/ menu()
    # Identify and calculate modifications to data.
    else:
        minimum = min(scores)

        total   = sum(scores)

        average = total/len(scores)
        return minimum,total,average/main()

# Display data modifications.
def display(scoresModified,result):

    if scores==None:
        print("Orignal data :", scores)

    else:
        print("Orignal data : ", scores)
    # Evaluate data modifications.
    scoresModified = scores
    lowestScore= min(scoresModified)
    scoresModified.remove(lowestScore)
    average=sum(scoresModified)/len(scoresModified)

    # Display data modifications.
    print("")
    print("---------------------")
    print("Modified List : ",scoresModified)
    print("Lowest Score Removed : ",lowestScore)
    print("Average : ", average)

    if average >= A_score:
        print('Letter Grade : A')
    elif average >= B_score:
        print('Letter Grade : B')
    elif average >= C_score:
        print('Letter Grade : C')
    elif average >= D_score:
        print('Letter Grade : D')
    else:
        print('Letter Grade : F')
    print("---------------------")
    print("")

    if scores ==None:
        print("Set : ", scores)
        print("")
        return

# Create display menu.
def menu():
    print("""-----------MENU-------------
        1) Create List
        2) Display Results
        3) Exit
----------------------------------\n""")
    # Set user input to an integer variable.
    UserInput = int(input())
    if UserInput<1 or UserInput>3:
        return menu()
    return  UserInput

# Define menu entries.
def main():
    scores = None
    while True:
        reply = menu()
        if reply == 1:
            scores = createList()
        if reply == 2:
            display(scores,list(analyseData(scores)))
        if reply == 3:
            exit(0)
    


if __name__=="__main__":
    main()
