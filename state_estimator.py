import math
class projectile:
    def __init__(self):
        self.ang=float(input("Enter the angle of projection: "))*math.pi/180
        self.vel=float(input("Enter the velocity of projection: "))
    def time(self):
        return 2*self.vel*math.sin(self.ang)/9.81
    def range(self):
        return (self.vel**2)*math.sin(2*self.ang)/9.81
    def height(self):
        return (self.vel**2)*math.sin(self.ang)**2/(2*9.81)
