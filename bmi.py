choice, height, weight, BMI = 0, 0, 0, 0
while choice != 1 and choice != 2:
    choice = int(input("This program requires your height and weight. Do you know them in (1)imperial or (2)metric units? "))

if choice == 1:
    height = 0.0254 * float(input("How tall are you in inches? "))
    weight = 0.4536 * float(input("What is your weight in pounds? "))
else:
    height = float(input("How tall are you in meters? "))
    weight = float(input("What is your weight in kilograms? "))

BMI = round(weight/(height*height), 1)
if BMI <= 18.5:
    category = "underweight"
elif BMI<=24.9:
    category = "average"
elif BMI<=29.9:
    category = "overweight"
else:
    category = "obese"
print("Your BMI indicates you are {0}. Your BMI is {1}".format(category, BMI))
