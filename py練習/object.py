
class phone :
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof =is_waterproof

    def is_ios(self):
        if (self.os == "ios"):
            return True
        else:
            return False
        
    def add(selr,n1,n2):
        return n1+n2

    
        
phone1 = phone("ios",123,True)
print(phone1.is_ios())
print(phone1.add(3,4))
phone2 = phone("andriod",456,False)
print(phone2.number)

