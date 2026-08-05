num = int(input("Enter Number to calculate factorial of : "))
if num == 0 or num == 1:
    print("1")
else:
    res = 1
    for i in range(1,num+1):
        res = res*i
    print(res)