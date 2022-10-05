height = input("Enter your height in inches: ")
height_inches = height
#turning height into meters
x = int(height_inches) * 0.0254
weight = input("Enter your weight in pounds: ")
weight_kg = weight
#turning weight into kg
y = int(weight_kg) * 0.45359237
#calculating BMI is weight in kg divided by height squared by 2
bmi = y / x ** 2
print(bmi)
