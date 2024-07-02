# Creating file in JSON format, writing certain information of users and then these information will be accessed by another python file
# filename = 9_write_json.py

# we will create a dictionary in JSON format

book = {}

book['rashid'] = {
    'name':'Rashid Hussain',
    'address': 'H#19, St#12, Eden Palace Villas, Lahore',
    'phone': 3155235698
}

book['adil'] = {
    'name':'Adil Ali',
    'address': 'H#14, St#13, Eden Palace Villas, Lahore',
    'phone': 344558999
}

import json as js

# It will dump dictionary object: book into string, it will convert it into json format
mystr = js.dumps(book)
print(mystr)

# Write mystr to a file in json format called book.txt in directory called Data within this path

with open ("D://Data_Science//1_Python//Data//book.txt", "w") as f:
    f.write(mystr)
    f.close()



