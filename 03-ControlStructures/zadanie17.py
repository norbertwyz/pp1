x=int(input("Enter x axis coordinate: "))
print(f"x = {x}")
y=int(input("Enter y axis coordinate: "))
print(f"y = {y}")

if (x > 0 and y > 0):
	print (f"Point P{x,y} lies in First quadrant")

elif (x < 0 and y > 0):
	print (f"Point P{x,y} lies in Second quadrant")
	
elif (x < 0 and y < 0):
	print (f"Point P{x,y} lies in Third quadrant")

elif (x > 0 and y < 0):
	print (f"Point P{x,y} lies in Fourth quadrant")
	
elif (x == 0 and y > 0):
	print (f"Point P{x,y} lies at positive y axis")

elif (x == 0 and y < 0):
	print (f"Point P{x,y} lies at negative y axis")

elif (y == 0 and x < 0):
	print (f"Point P{x,y} lies at negative x axis")

elif (y == 0 and x > 0):
	print (f"Point P{x,y} lies at positive x axis")

else:
	print (f"Point P{x,y} lies at origin")
