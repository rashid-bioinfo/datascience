# Write a program to accept age of 6 students and display them in a sorted manner

rashid = int(input("Enter age of rashid: "))
yasir = int(input("Enter age of yasir: "))
ahmad = int(input("Enter age of ahmad: "))
bakar = int(input("Enter age of bakar: "))
ashar = int(input("Enter age of ashar: "))
ali = int(input("Enter age of ali: "))

mylist = [rashid, yasir, ahmad, bakar, ashar, ali]

mylist.sort()
print(mylist)
