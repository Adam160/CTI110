#Remove Grey from RGB values
#Parks, Daniel

#Set program name
def main():
    
#Enter RGB values and variables
    Red_value = int(input())
    Green_value = int(input())
    Blue_value = int(input())
    
#Find the smallest value
    if Red_value<= Green_value and Red_value <= Blue_value:
        smallest_value = Red_value
    elif Green_value <= Red_value and Green_value <= Blue_value:
        smallest_value = Green_value
    else:
        smallest_value = Blue_Value

#Subtract the smallest value
    Red_value = Red_value - smallest_value
    Green_value = Green_value - smallest_value
    Blue_value = Blue_value - smallest_value

#Display Results
    print(Red_value, Green_value, Blue_value)

#Restart Program
main()
