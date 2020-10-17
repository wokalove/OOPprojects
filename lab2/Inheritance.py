from abc import ABCMeta, abstractmethod
import math
import numpy as np

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
        ox = [self._x,0]

        abs_ox = math.sqrt(pow(ox[0],2)+pow(ox[1],2))

        cos = (self._x*ox[0] + self._y*ox[1])/self.Abs()*abs_ox
        angle = math.degrees(math.acos(cos))
        return angle

    def cdot(self, vector):
        dot_product = self._x *vector._x + self._y*vector._y
        return dot_product
        
class Vector3D(Vector2D):
   def __init__(self,x,y,z):
        Vector2D.__init__(self,x,y)
        self.__z = z
   def Abs(self):
       return math.sqrt(pow(self._x,2)+pow(self._y,2)+pow(self.__z,2))
   def getComponents(self):
       return[self._x,self._y,self.__z]
   def getAngles(self):
       ox = [self._x,0,0]
       ox_abs = math.sqrt(pow(ox[0],2)+pow(ox[1],2)+pow(ox[2],2))
       cos = (self._x *ox[0]+self._y*ox[1]+self.__z*ox[2])/self.Abs()*ox_abs
       angle = math.degrees(math.acos(cos))
       return angle
   def cdot(self, vector):
       dot_product = self._x *vector._x + self._y*vector._y +self.__z *vector.__z
       return dot_product

v2= Vector2D(1,1)
v2_2 = Vector2D(1,2)

print(v2.Abs())
print(v2.getAngles())

print("DOOOt",v2.cdot(v2_2))

v3= Vector3D(1,3,5)
v3_2 =Vector3D(1,2,7)
print(v3.getAngles())
print(v3.cdot(v3_2))