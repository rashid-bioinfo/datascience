# List Set Dict Comprehensions

list = [1,2,3,4,5,6,7,8,9,10,12]

# make a new list with even numbers only
even_num_list = []
for i in list:
    if (i%2 == 0):
        even_num_list.append(i)
print(even_num_list)

# but to make it concise we can do as:
even_list = [i for i in list if i%2==0]
print(even_list)

# Generate square of all numbers in list
# the long way:
square_num_list = []
for i in list:
    square_num_list.append(i**2)
print(square_num_list)

# the short way
square_list = [i**2 for i in list]
print(square_list)

