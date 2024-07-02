# write a program to find greatest of three numbers

def find_max_number(n1, n2, n3):
    if (n1>n2 and n1>n3):
        return n1
    elif (n2>n3 and n2>n1):
        return n2
    else:
        return n3
    
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

greatest_number = find_max_number(n1,n2,n3)

print(f"The greatest number is {greatest_number}")