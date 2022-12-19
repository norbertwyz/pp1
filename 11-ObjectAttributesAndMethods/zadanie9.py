from array import array
from os import stat


class Arays():
    @staticmethod
    def same_values(number_of_array_elements, value_of_array_elements):
        array = []
        for i in number_of_array_elements:
            array.append(value_of_array_elements)
        return array

    @staticmethod
    def random_value(number_of_array_elements, value_from, value_to):
        import random
        array_random = []
        for i in range(number_of_array_elements):
            x=random.randrange(value_from, value_to)
            array_random.append(x)
        return array_random

    @staticmethod
    def  arrat_checker(array, value_from, value_to):
        licznik = 0
        for i in array:
            if i>=value_from and i <= value_to:
                licznik+=1
        return licznik



            
 
# class Arrays():

#     @staticmethod
#     def print_in_col(array):
#         for c in array:
#             print(c)
            
# my_array = [4,1,8,7,2]
# Arrays.print_in_col(my_array)
