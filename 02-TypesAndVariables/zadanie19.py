height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/((height/100)**2)

if bmi<18.49 and bmi>25: print("Your BMI index is invalid and may be dangerous for your health.")
elif bmi>18.5 and bmi<24.99: print("Your BMI is OK.")
elif bmi>25: print("Your BMI index is invalid and may be dangerous for your health.")