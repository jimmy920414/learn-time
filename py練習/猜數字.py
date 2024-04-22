secret_num = 25
guess = None
guess_count = 0
guess_limit = 3
out_of_limit =False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if (guess_count <= guess_limit):
        guess = int(input("Input One Number:"))
        if (guess < secret_num):
            print("猜大一點")
        elif (guess > secret_num):
             print("猜小一點")
    else:
        out_of_limit = True

if (out_of_limit):
    print("你輸了")
else:
    print("猜對了")





