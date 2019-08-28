"""
Tung Hoang - 08/28/19
This program ask user for their status and determine
whether they are eligible for president
"""
# Constant variables
requiredAge = 35
requiredCitizen = "Yes"
requiredResidency = 14

# Ask user for their input
age = int(input("Age: "))
citizen = input("Born in the U.S.? (Yes/No): ")
residency = int(input("Years of residency: "))

# Determining whether they are eligible for president
if age >= requiredAge and citizen == requiredCitizen \
   and residency >= requiredResidency:
    print("You are eligible to run for president.")
else:
    print("You are not eligible to run for president.")
