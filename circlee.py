import math
class circle():
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return (self.rad ** 2)*math.pi 
    def cir(self):
        return 2 * math.pi*self.rad
    
Newcircle=circle(4)
print(Newcircle.area())
print(Newcircle.cir())
    

