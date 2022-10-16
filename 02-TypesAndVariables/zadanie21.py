import random


throw=random.randint(1, 6)
guess=int(input("Enter a number from 1 to 6: "))
if throw==guess: print("True")
elif throw!=guess: print("False")