# if判斷 if elif else

# hungy = True
# if (hungy):
#     print("go eat food")

# rainy = True
# if (rainy):
#     print("by MRT")
# else:
#     print("wolk")

# test = 100
# if (test == 100):
#     print("give 1000")
# elif (test>= 80):
#     print("give 500")
# elif(test>= 60):
#     print("100")
# else:
#     print("u give me 300 ")

# score = 100
# rainy = True
# if (score == 100 and rainy):
#     print("give u 100$")
# else:
#     print("i give u 100$")

# score = 100
# rainy = True
# if (score == 100 or rainy):
#     print("give u 100$")
# else:
#     print("i give u 100$")

# score = 100
# rainy = True
# # if (score == 100 or not(rainy)):
# #     print("give u 100$")
# # else:
# #     print("i give u 100$")

# if (score == 100 and not(rainy) or score == 100):
#     print("give u 100$")
# else:
#     print("i give u 100$")

def max_num(a,b,c):
    if (a>b and a>c):
        return a 
    elif (b>c and b>a):
        return b 
    else:
        return c
print(max_num(2,3,4))
