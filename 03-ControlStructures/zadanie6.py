from turtle import speed


speedlimit=130
speed=int(input("Enter your car's current speed: "))
if speed>speedlimit: 
    print(f"Your car's current speed is {speed} km/h, which is an unforgivable sin. Prepare to pay.")
else:
    print("Good boy.")