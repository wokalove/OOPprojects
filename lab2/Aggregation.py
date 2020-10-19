from abc import ABCMeta, abstractmethod
import math


class IVector:
    __metaclass__ = ABCMeta
    @abstractmethod
    def Abs(self):
        pass
    @abstractmethod
    def getComponents(self):
        pass
    @abstractmethod
    def getAngles(self):
        pass
    @abstractmethod
    def cdot(self):
        pass
 
class Vector2D(IVector):
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    def Abs(self):
        return math.sqrt(pow(self._x,2)+pow(self._y,2))
        
    def getComponents(self):
       return[self._x,self._y]
        
    def getAngles(self):
        ox = Vector2D(self._x,0)
        abs_ox = ox.Abs()

        cos = (self._x*ox._x + self._y*ox._y)/self.Abs()*abs_ox
        angle = math.degrees(math.acos(cos))
        return angle

    def cdot(self, vector):
        dot_product = self._x *vector._x + self._y*vector._y
        return dot_product
    def from_polar_to_cartesian(self):
        x = self.Abs()*math.cos(self.getAngles())
        y = self.Abs()*math.sin(self.getAngles())
        return [x,y]
        
class Vector3D(IVector):
   def __init__(self,x,y,z):
        self.__vector = Vector2D(x,y)
        self.__z = z
   def Abs(self):
       x, y = self.__vector.getComponents()
       return math.sqrt(pow(x,2)+pow(y,2)+pow(self.__z,2))

   def getComponents(self):
       x, y = self.__vector.getComponents()
       return[x,y,self.__z]

   def getAngles(self):
       x, y = self.__vector.getComponents()
       fi = math.atan(y/x)
       psi = math.atan(math.sqrt(pow(x,2)+ pow(y,2))/self.__z)
       
       angles = [fi, psi]
       return angles

   def cdot(self, vector):
       x, y = self.__vector.getComponents()
       x_v,y_v,z_v = vector.getComponents()
       dot_product = x *x_v + y *y_v +self.__z *z_v
       return dot_product


   def spherical_coordinates(self):
       fi,psi = self.getAngles()
       r = self.Abs()
       x = r* math.cos(psi)*math.cos(fi)
       y = r*math.cos(psi)*math.sin(fi)
       z = r* math.sin(psi)
       return [x,y,z]

class Decorator(Vector3D):
    def __init__(self,x,y,z):
        Vector3D.__init__(self,x,y,z)
    def cross_product(self,vector):
        x,y,z = self.getComponents()
        x_2,y_2,z_2 = vector.getComponents()
        x_v = y*z_2 - (z*y_2)
        y_v = z *x_2 - (x *z_2)
        z_v = x*y_2 - (y *x_2)
        new_vector = Vector3D(x_v,y_v,z_v)
        return new_vector
class Adapter2D:
    pass
    
        
v2= Vector2D(1,1)
v2_2 = Vector2D(1,2)

print(v2.Abs())
print(v2.getAngles())
'''
print("DOOOt",v2.cdot(v2_2))

v3= Vector3D(1,3,5)
v3_2 =Vector3D(1,2,7)
print(v3.getAngles())
print(v3.cdot(v3_2))
print(v3.cross_product(v3_2))
'''
deco = Decorator(1,3,5)
v3_2 = Vector3D(1,2,7)
print(deco.cross_product(v3_2).getComponents())

v3= Vector3D(1,3,5)
print(v3.getAngles())
