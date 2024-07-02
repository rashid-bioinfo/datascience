# Write a program to print multiplication of a given number using for loop


num = int(input("Please enter number for calculating multiplication number: "))

i = 1
# printing table using range function
# for i in range (i, 11):
#     print(f"{i} x {num} = {i*num}")

# printing table using for while loop only

while (i <= 10):
    print(f"{i} x {num} = {i*num}")
    i = i + 1