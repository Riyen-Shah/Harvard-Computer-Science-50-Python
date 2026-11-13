expression = input("Expression: ")
a, y, b = expression.split(" ", 2)
x = float(a)
z = float(b)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(result)
