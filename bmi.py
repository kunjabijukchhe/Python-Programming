height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight/(height**2) 

print("Your BMI is: {0} and \nYou are: ".format(bmi), end='')

if (bmi < 16):
   print("severely underweight")

elif (bmi >= 16 and bmi < 18.5):
   print("Underweight")

elif (bmi >= 18.5 and bmi < 25):
   print("Normal")

elif (bmi >= 25 and bmi < 30):
   print("Overweight")

elif (bmi >=30):
   print("Obese")