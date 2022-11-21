import random

file = open('randomintegers.txt', 'w',  encoding='utf-8')

for i in range(50):
    x = random.randrange(100,999)
    file.write(f"{x}\n")

file.close()


