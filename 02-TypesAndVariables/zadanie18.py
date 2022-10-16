a=float(input("Enter the value of the 1st side: "))
b=float(input("Enter the value of the 2nd side: "))
c=float(input("Enter the value of the 3rd side: "))

x=(a+b+c)/2
print(f"The area of the triangle calculated using Heron formula is {(x*(x-a)*(x-b)*(x-c))**(1/2)}.")