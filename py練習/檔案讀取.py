# 檔案的讀取、寫入

file = open("C:/Users/jimmy/Desktop/python/py練習/123.txt", mode="r")
print(file.read()) #readline()讀一行
                   #for line in file:
                        # print(line)
file.close()

# 絕對入徑C:/Users/jimmy/Desktop/python/py練習/123.txt
# 相對入徑 以程式位製作延伸 123.txt

#mode = "r" 讀取
#mode = "w" 覆寫
#mode = "a" 在原先的資料後寫東西
