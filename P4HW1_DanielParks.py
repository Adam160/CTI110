
    # 31 March 2022
    # CTI-110 P4HW1 - Score List
    # Daniel Parks
    #

# Set user input as variable for future function - How many scores do you have to enter?
NumOfScores = int(input("How many scores do you want to enter? "))

# Identify grading scheme
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Identify container/empty list for user entered scores
scores = []

# Set criteria for number of inputes based on user entry
for i in range(1, NumOfScores+1):
    while True:
        try:
            IndividualScore = int(input("Enter score {}: ".format(i)))
            # Set criteria for valid response
            if IndividualScore >= 0 and IndividualScore <=100:
                # Add valid response to list
                scores.append(IndividualScore)
                break
            # Invalide response
            else:
                print()
                print("INVALID Score entered!!!!")
                print("score should be betweek 0 and 100")
                print()
        except:
            # Repeat loop until "range" is complete
            continue

print()
print("-----------------Results-----------------")
# Identify lowest score and display
lowestscore= min(scores)
print("Lowest Score   : {}".format(lowestscore))

# Display list without lowest score
scores.remove(lowestscore)
print("Modified List  :", scores)

# Identify and calulate the average of the inputed scores
scoresAverage = sum(scores)/len(scores)

# Change variable to allow for differences in format (int and str)
scoresAverages = (f'{scoresAverage:.2f}')

# Print Average Score
print("Scores Average : {}".format(scoresAverages))  

# Identify and print leter grade
if scoresAverage >= A_score:
    print('Grade          : A')
elif scoresAverage >= B_score:
    print('Grade          : B')
elif scoresAverage >= C_score:
    print('Grade          : C')
elif scoresAverage >= D_score:
    print('Grade          : D')
else:
    print('Grade          : F')

print("-----------------------------------------")
print()

# Program start.
main()