# We will read the data written in book.txt contained in directory:Data within the same path
# filename = 10_access_json.py

f = open ("D://Data_Science//1_Python//DATA//book.txt", "r")

book_content = f.read()
f.close()
# the contents of this book will be printed as string
print(book_content)

import json as js
# It will convert the string into dictionary
book_dict = js.loads(book_content)

# the contents of this book will be printed as dictionary
print(book_dict)

# to know the type of each variable
print(type(book_content)) # <class 'str'>
print(type(book_dict)) # <class 'dict'>

# To know the phone number of Rashid
print("-------")
print(book_dict['rashid']['phone'])

# to print addresses of all persons in book.txt
for person in book_dict:
    print(book_dict[person]['address'])