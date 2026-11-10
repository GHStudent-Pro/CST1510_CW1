# Task 4: Body Mass Index (BMI)

KG_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

weight_kg = weight_pounds * KG_PER_POUND
height_m = height_inches * METERS_PER_INCH
bmi = weight_kg / (height_m ** 2)

print(f"BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")
