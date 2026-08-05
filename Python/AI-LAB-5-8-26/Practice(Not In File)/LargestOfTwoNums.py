a = int(input("Input Number 1 : "))
b = int(input("Input Number 2 : "))

if a>b:
    print(f"A : {a} is greater than B : {b}")
elif b>a:
    print(f"B : {b} is greater than A : {a}")
elif a==b:
    print(f"Both A: {a} and B: {b} are same")
else:
    print("Invalid Input")