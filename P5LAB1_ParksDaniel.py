def laps_to_miles(user_laps):
    user_laps = user_laps*0.25
    return user_laps


if __name__ == '__main__':
    laps = float(input())
    print("{:.2f}".format (laps_to_miles(laps)))

