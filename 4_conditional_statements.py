# Write a program to calculate whether a given username contains more than 10 characters or not


user_name = input("Please enter a username: ")

char_count = len(user_name)

if (char_count > 10):
    print(f"The entered user name: {user_name} contains MORE than 10 characters")
elif (char_count < 10):
    print(f"The entered user name: {user_name} contains LESS than 10 characters")
else:
    print(f"The entered user name: {user_name} contains 10 characters")

