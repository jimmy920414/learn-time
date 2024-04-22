op = input("請輸入運算符號")
num1 = float(input("Input One Number:"))
num2 = float(input("Input Second Number:"))
num3 = float(input("Input Third Number:"))

if (op == "+"):
    print(num1+num2+num3)
elif (op =="-"):
    print(num1-num2-num3)
elif (op =="*"):
    print(num1*num2*num3)
elif (op =="/"):
    print(num1/num2/num3)
else:
    print("error")