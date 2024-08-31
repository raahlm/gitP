x1:int=int((input("Enter first num: ")))
x2:int=int(input(("Enter second num: ")))
operation = {
    '+': lambda x1, x2: x1 + x2, '-': lambda x1, x2: x1 - x2,'*': lambda x1, x2: x1 * x2,'/': lambda x1, x2: x1 / x2}
s:str=" "
while s not in operation:
    s=input("operation (+, -, *, /): ")
    if s not in operation:
        print("invalid operation")
result = operation[s](x1,x2)
print(f"{x1} {s} {x2} = {result}")

