from sre_parse import DIGITS


number = int(input("Enter number: "))
for i in range(1,number+1):
    digits = ""
    iterator = i
    while iterator != 0:
        digits = digits + str(i)
        iterator = iterator - 1
    print(digits)