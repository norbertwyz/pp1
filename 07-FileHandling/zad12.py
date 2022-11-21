add=input("Enter a name of a next product you want to buy:\n")
file=open('shopping.txt', 'a', encoding="utf-8")
file.write(f"{add}\n")
file.close()
