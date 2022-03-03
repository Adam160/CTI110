
    # 03 March 2022
    # CTI-110 P2HW2 - Score Averages
    # Daniel Parks
    #

# Ask for 7 User inputs and set them as variables
score_1 = float(input('Enter scor number #1: \n'))
score_2 = float(input('Enter scor number #2: \n'))
score_3 = float(input('Enter scor number #3: \n'))
score_4 = float(input('Enter scor number #4: \n'))
score_5 = float(input('Enter scor number #5: \n'))
score_6 = float(input('Enter scor number #6: \n'))
score_7 = float(input('Enter scor number #7: \n'))

# Set test scores in a list
score_list = [score_1,score_2,score_3,score_4,score_5,score_6,score_7]
# Identify the lowest number in the list
lowest_number = min(score_list)
# Remover the lowest number from the list
modified_scores = score_list.remove(lowest_number)
# Find the average of the scores in the list andset it to 2 decimal places
score_average = sum(score_list)/len(score_list)
score_average = format(score_average,'.2f')

# Print Results
print("-----------------Results-----------------")
print("Lowest score is : ", lowest_number)
print("Modified List   : ", score_list)
print("Scores Average  : ", score_average)
print("-----------------------------------------")
