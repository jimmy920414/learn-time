#class
class phone :
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof =is_waterproof

    
        
phone1 = phone("ios",123,True)
print(phone1.os)
phone2 = phone("andriod",456,False)
print(phone2.number)


