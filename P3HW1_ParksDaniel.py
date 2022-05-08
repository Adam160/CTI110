# CTI-110
# P3HW1 - Debugging
# Daniel Parks 
# 20 MAR 2022
#
#
# This program takes a number grade and outputs a letter grade.
#    Identify program function.
#    Identify 10-point grading scale.
#    Ask for user input.
#      User enters score.
#    Identify score ask a letter grade and print results.
#    Restart Program.
#
#
# I changed the program's output to reflect what the assignment's "Example of output is shown below" section shows.
#
# Identify program function.
def main():

    # 10-point grading scale identified.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Ask user for input and save as variable.
    score = float(input('Please enter score: '))

    # Identify grade and print results.
    if score >= A_score:
        print('Grade is A.')
    elif score >= B_score:
        print('Grade is B.')
    elif score >= C_score:
        print('Grade is C.')
    elif score >= D_score:
        print('Grade is D.')
    else:
        print('Grade is F.')

# Program start.
main()