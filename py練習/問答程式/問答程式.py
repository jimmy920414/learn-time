from question import Question #從question.py檔中引入Question

test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公使等幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色\n(a) 黑色\n(b) 藍色\n(c) 黃色\n\n"
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"c")
]

def runtest(questions):  #跑測驗 傳入questions(新的資料型態)
    score = 0 #剛開始的值(number)
    for question in questions: #跑每一題的測驗
        answer = input(question.description)  #存放使用著的輸入
        if (answer == question.answer):
            score+=1                           #列表的長度 len
    print("你得到" + str(score) + "分,共" + str(len(questions)) + "題")
runtest(questions)