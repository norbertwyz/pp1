file=open("numbers.txt",'r')
total=0
for line in file:
    print(line, end='')
    total=total+int(line)

print(f'\nThe sum off the integers is {total}.')
file.close()