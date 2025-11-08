# calculator.py
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    elif op == '%':
        return a % b
    elif op == '**':
        return a ** b
    else:
        raise ValueError("Unsupported operation")

def main():
    print("=== Simple Calculator ===")
    print("Supported operations: +  -  *  /  %  **")

    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+ - * / % **): ").strip()

            result = calculate(a, b, op)
            print(f"Result: {result}\n")
        except Exception as e:
            print("Error:", e)

        again = input("Do you want to calculate again? (y/n): ").lower().strip()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
