try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Invalid input! Please enter numeric values.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except Exception as e:
    print("An error occurred:", e)

else:
    print("Result =", result)

finally:
    print("Program execution completed.")