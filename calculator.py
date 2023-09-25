#problem1 
class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    
Newcalculator=calculator(5,5)
print(Newcalculator.sum())
print(Newcalculator.sub())
print(Newcalculator.mul())
print(Newcalculator.divide())
    
