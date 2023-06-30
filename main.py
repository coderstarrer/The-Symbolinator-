
rows = int(input("Enter the amount of rows you want to use"))
columns = int(input("Enter the amount of columns you want to use"))
symbols = str(input("Enter a symbol to use"))

for i in range(rows):
    for j in range(columns):
        print(symbols,end="")