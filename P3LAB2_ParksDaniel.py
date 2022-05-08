TypeOfService = input("Enter desired auto service:")
if TypeOfService == "Oil change":
    print("\nYou entered:",TypeOfService)
    print("Cost of oil change: $35")
elif TypeOfService == "Tire rotation":
    print("\nYou entered:",TypeOfService)
    print("Cost of tire rotation: $19")
elif TypeOfService == "Car wash":
    print("\nYou entered:",TypeOfService)
    print("Cost of car wash: $7")
else:
    print("\nYou entered:",TypeOfService)
    print("Error: Requested service is not recognized")