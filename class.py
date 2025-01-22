# ELECTRICITY BILL
def bill(units):
    bill = 50  
    if units <= 100:
        bill += units * 5
    elif units <= 200:
        bill += (100 * 5) + (units - 100) * 27
    else:
        bill += (100 * 5) + (100 * 27) + (units - 200) * 710

    return bill
print(f"Total electricity bill: ₹{bill(100)}")



# FIBANOCCI SERIES
n = int(input("Enter the position (n): "))

if n <= 0:
    print("Invalid input. Please enter a positive integer.")
elif n == 1:
    print("The 1st Fibonacci number is 0")
elif n == 2:
    print("The 2nd Fibonacci number is 1")
else:
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(f"The {n}th Fibonacci number is {b}")
    

# FACTORIAL
    num = int(input("Enter a number: "))
fact= 1

for i in range(1, num + 1):
    fact *= i

print(f"The factorial of {num} is {fact}")


# ARITHEMATIC OPERATIONS

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print('Type "end_code" to exit.')
    
    choice = input("Enter your choice: ")
    
    if choice == "end_code":
        print("Exiting the program. Goodbye!")
        break
    
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please try again.")
        
    # GREATEST OF 3
    
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c  

print(greatest(1, 10, 50))



# FIZBUZZ
for i in range(1, 101):
     if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
     elif i % 3 == 0:
         print("Fizz")
     elif i % 5 == 0:
         print("Buzz")
     else:
        print(i)


 # DIVISORS
n = int(input("Enter a number: "))

print(f"Divisors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]

# DIGITS COUNT
count = len(digits)
digit_sum = sum(digits)
digit_product = 1
for d in digits:
    digit_product *= d

print(f"Number of digits: {count}")
print(f"Sum of digits: {digit_sum}")
print(f"Product of digits: {digit_product}")