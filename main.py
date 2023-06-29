import math

print("Welcome to the Mathinator! Choose an operand: *, /, +, -, sqrt, abs, sin, cos, pow,log,tan,arc-sine or asin")
operand = input("Enter the operand: ")

if operand == "*" or operand == "product" or operand == "multiplication" or operand == "multiply":
    print("You chose multiplication!")
    mult = float(input("Enter your first product: "))
    mult2 = float(input("Enter your second product: "))
    mult3 = mult * mult2
    print(mult3)
elif operand == "+" or operand == "addition" or operand == "sum" or operand == "add":
    print("You chose addition!")
    add = float(input("Enter your first sum: "))
    add2 = float(input("Enter your second sum: "))
    add3 = add + add2
    print(add3)
elif operand == "-" or operand == "difference" or operand == "subtraction" or operand == "minus":
    print("You chose subtraction!")
    sub = float(input("Enter your first difference: "))
    sub2 = float(input("Enter your second difference: "))
    sub3 = sub - sub2
    print(sub3)
elif operand == "/" or operand == "quotient" or operand == "division":
    print("You chose division!")
    div = float(input("Enter your first quotient: "))
    div2 = float(input("Enter your second quotient: "))
    div3 = div / div2
    print(div3)
elif operand == "%" or operand == "modulus" or operand == "remainder":
    print("You chose modulus!")
    mod = float(input("Enter your first quotient: "))
    mod2 = float(input("Enter your second quotient to find out the remainder: "))
    mod3 = mod % mod2
    print("The remainder is:", mod3)
elif operand == "sqrt" or operand == "square root":
    print("You chose square root!")
    sqrt1 = float(input("Enter the square root: "))
    res1313 = math.sqrt(sqrt1)
    print(res1313)
elif operand == "abs" or operand == "absolute" or operand == "absolute value":
    print("You chose absolute value!")
    abs1 = float(input("Enter the absolute value: "))
    absres = math.fabs(abs1)
    print(absres)
elif operand == "sin" or operand == "sine":
    print("You chose sine!")
    sine1 = float(input("Enter the sine: "))
    sinres = math.sin(sine1)
    print(sinres)
elif operand == "cos" or operand == "cosine":
    print("You chose cosine!")
    cosine1 = float(input("Enter the cosine: "))
    desultoriness = math.cos(cosine1)
    print(desultoriness)
elif operand == "pow" or operand == "power of" or operand == "exponents":
    print("You chose the power of!")
    powof = float(input("Enter the base number: "))
    powof1 = float(input("Enter the exponent: "))
    powres = math.pow(powof, powof1)
    print(powres)
elif operand == "log" or operand == "log10" or operand == "logarithmic":
    print("You chose log10")
    log10 = float(input("Enter the logarithmic number."))
    log10res = math.log10(log10)
    print(log10res)
elif operand == "tan" or operand == "tangent":
    print("You chose tan")
    tan = float(input("Enter the tangent number"))
    tanres = math.tan(tan)
    print(tanres)
elif operand == "arc-sine" or operand == "arcsine" or operand == "asin":
    print("You chose arc-sine")
    arcsine = float(input("Enter the arc-sine number"))
    arcsine = math.asin(arcsine)
    print(arcsine)
else:
    while True:
        operand = input("Enter a valid operand:")


