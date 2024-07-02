# sets

# initializing set

s = set()

s.add('rashid')
print(s)

# to remove duplicate element from a list, then use set

list = [1,2,3,4,5,2,3,4]
print(list) # prints all element
s = set(list)
print(s) # prints only unique items

s.add(6)
print(s)

# forzen set means you are not able to chnage the contents of set

fs = frozenset(list)
print(fs)
# fs.add(6) # Error: it does not allow to add/remove the contents of set

# some operations on set

x = {'a', 'b',  'c', 'd'}

for i in x:
    print(i)

print('a' in x) # True
print('g' in x) # False