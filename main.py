def add(a,b):
    return int(a+b)

def subtract(a,b):
    return int(a-b)

def multiply(a,b):
    return int(a*b)

def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

a=float(input("Enter First Number: "))
for symbols in operations:
    print(symbols)
operation_symbol=input("Choose an operation: ")
b=float(input("Enter Second Number: "))

print(operations[operation_symbol](a,b))
