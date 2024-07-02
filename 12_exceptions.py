# Exceptions and handling exceptions


num1 = input("Please input a number: ")
num2 = input("Please input a number: ")

try:
    res = num1/int(num2)
except ZeroDivisionError as e:
    print(f"Division by zero exception is occured")
    res = None

# To see which type of exception has occurred
except Exception as e:
    print(f"Print exception type", type(e).__name__)
    res = None


print(f"The sum of {num1} and {num2} is {res}")