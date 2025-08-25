~~~
print("welcome to my first calculator!")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
print("what do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter your choice (1/2/3/4): ")
if choice == "1":
    print("The sum is:", num1 + num2)
elif choice == "2":
    print("The difference is:", num1 - num2)
elif choice == "3":
    print("The product is:", num1 * num2)
elif choice == "4":
    print("The quotient is:", num1 / num2)
else:
    print("Invalid choice!")
~~~
