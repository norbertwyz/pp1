def names(arr, length):
    arr = [Genowefa, Onufry, Celestyna, Alojzy, Pankracy]
    if length <= 0:
        return []
    max = len(arr[0])
    
    for x in arr:
        if(len(x)) > max:
            max = len(x)
            print(x)

