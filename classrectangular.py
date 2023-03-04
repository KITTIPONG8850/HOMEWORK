import math
class Rectangular :
    def __init__(self,x: float, y: float):
        self.x = x
        self.y = y

    def position(self):
        return self.x,self.y

    def Is_on_Xaxis(self)->bool:
        return self.y==0
    
    def Is_on_Yaxis(self)->bool:
        return self.x==0
    
    def quadrant(self):
        if PRAYUTH.Is_on_Xaxis()==True and PRAYUTH.Is_on_Yaxis()==True:
            return print("This point is on origin")
        elif PRAYUTH.Is_on_Xaxis()==True:
            return print("This point is on X axis")
        elif PRAYUTH.Is_on_Yaxis()==True:
            return print("This point is on Y axis")        
        elif self.x>0 and self.y>0:
            return print("This point is on Quadrant 1")
        elif  self.x<0 and self.y>0:
            return print("This point is on Quadrant 2")
        elif  self.x<0 and self.y<0:
            return print("This point is on Quadrant 3")    
        else:
            return print("This point is on Quadrant 4")
    
    def distance_fromXaxis(self):
        return self.y
    
    def distance_fromYaxis(self):
        return self.x
    
    def far_from_origin(self):
        return math.sqrt((self.x*self.x)+(self.y*self.y))
    
    def midpoint_between_given_point(self,a: float, b: float):
        return float(self.x+a)/2,float(self.y+b)/2
    
    def distance_from_given_point(self,a: float, b: float):
        return math.sqrt( (a-self.x)*(a-self.x)+(b-self.y)*(b-self.y) )
    
    def angle_with_Xaxis(self):
        return math.degrees(math.atan((self.y/self.x)))
 
PRAYUTH = Rectangular(x=3.2,y=4)
print(PRAYUTH.position())
print(PRAYUTH.Is_on_Xaxis())  
print(PRAYUTH.Is_on_Yaxis())

PRAYUTH.quadrant()
print(PRAYUTH.distance_fromXaxis())
print(PRAYUTH.distance_fromYaxis())

print(PRAYUTH.far_from_origin())
print(PRAYUTH.midpoint_between_given_point(8,10.4))
print(PRAYUTH.distance_from_given_point(8,10.4))
print(PRAYUTH.angle_with_Xaxis())


                                    
    
