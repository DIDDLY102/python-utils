# calculator.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero!"

if __name__ == "__main__":
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+": print("Result:", add(a, b))
    elif op == "-": print("Result:", subtract(a, b))
    elif op == "*": print("Result:", multiply(a, b))
    elif op == "/": print("Result:", divide(a, b))
    else: print("Invalid operation")
      
