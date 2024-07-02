# This program will import the user defined functions/modules from the file contained within the same path called user_defined_modules.py
'''
import modules.user_defined_modules as user_func

area_of_square = user_func.calculate_area_of_square(6,4)
area_of_triangle = user_func.calculate_area_of_trainagle(25,2)

print(area_of_square)
print(area_of_triangle)


'''

# This program will import the user defined functions/modules from the file called user_defined_modules.py located somewhere else

import sys

sys.path.append('D:\Data_Science\999_Code_Basics_Resources')

import user_defined_modules as user_func

area_of_square = user_func.calculate_area_of_square(6,4)
area_of_triangle = user_func.calculate_area_of_trainagle(25,2)

print(area_of_square)
print(area_of_triangle)






