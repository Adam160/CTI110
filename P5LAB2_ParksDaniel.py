# Define function
def feet_to_steps(NumOfSteps):
    # Take user iput and apply step-to-feet calculation
    return int(NumOfSteps / 2.5)


if __name__ == '__main__':
    # Identify user input as floated variable
    NumOfSteps = float(input())
    # Display Results
    print(feet_to_steps(NumOfSteps))