# This program calculates your age in the year 2050.
# Input:  Your current age
# Output: Your current age followed by your age in 2050

# Create your variables here
# I have added a variable for the current year
# I have added a variable for the current age
# I have verified the variables run properly with each other

currentYear = int(input("Please enter the current year: "))
myCurrentAge = int(input("Please enter your current age: "))
myNewAge = myCurrentAge + (2050 - currentYear)
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")
