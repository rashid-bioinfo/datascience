# Iterator

a = ["Rashid", "Hussain",'is','learning', 'Data Science']

for i in a:
    print(i)

# To print all objects in array, a
print(dir(a))

# It will give location of array, a, stored in memory
location = iter(a)
print (location)

# It will print first element of array, a
# In fact when above for loop is called it internally call next object
print(next(location)) # prints Rashid

# It will print next element of array, a
print(next(location)) # prints Hussain

# reverse iterator is also available

rev_iter = reversed(a)
print(next(rev_iter)) # prints Data Science
