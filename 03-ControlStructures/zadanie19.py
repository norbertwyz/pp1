human = int(input("Enter the dog's age in human years: "))

if human < 0:
	print("Age must be a positive number.")
elif human <= 2:
	dog = human * 10.5
else:
	dog = 21 + (human - 2)*4
print(f"The dog's age in dog's years is, {dog} years")


#19.	Write a program that calculates a dog's age in dog’s years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. Sample result:
#Enter the dog's age in human years: 15
#The dog's age in dog’s years is 73 years.
