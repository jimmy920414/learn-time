# for 變數 in 字串or列表
#     要重複執行的程式

# for letter in "hello jimmy":
#     print(letter)

# for num in [1,2,3,4,5]:
#     print(num)

# for num in range(100):
#     print(num)

def power(base_num,pow_num): #base為基數 pow為次方
    result = base_num
    for index in range(pow_num - 1):
        result = result * base_num
    return result

print((power(2,6))) 