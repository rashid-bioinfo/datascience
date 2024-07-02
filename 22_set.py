# set

s = set([1,2,3,4,2,4,5])
print(s) # prints unique value only

# to print even numbers we will initialize the set with curly braces instead of square brackers


even = {i for i in s if i%2==0}
print(even) # prints only even numbers