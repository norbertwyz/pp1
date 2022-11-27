def display_integers(n):
    integers = ""
    for i in range(1,n+1):
        if i == 1:
            integers = str(i) + " "
        else: integers = integers + str(i) + " "
    return integers
print("liczby całkowite od 1 do 15 to: " + display_integers(15))