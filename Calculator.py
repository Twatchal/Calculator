def a(x, y):
    return x + y

def s(x, y):
    return x - y

def m(x, y):
    return x * y

def d(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", a(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", s(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", m(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", d(num1, num2))
        
        next_calc = input("Let's do next calculation? (yes/no): ")
        if next_calc == "no":
          break
    
    else:
        print("Invalid Input")
