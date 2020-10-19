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
        self.__x = x
        self.__y = y
        
    def Abs(self):
        return math.sqrt(pow(self.__x,2)+pow(self.__y,2))
        
    def getComponents(self):
       return[self.__x,self.__y]
        
    def getAngles(self):
        ox = Vector2D(self.__x,0)
        abs_ox = ox.Abs()

        cos = (self.__x*ox.__x + self.__y*ox.__y)/self.Abs()*abs_ox
        angle = math.degrees(math.acos(cos))
        return angle

    def cdot(self, vector):
        dot_product = self.__x *vector.__x + self.__y*vector.__y
        return dot_product
    
        
class Vector3D(Vector2D):
   def __init__(self,x,y,z):
        Vector2D.__init__(self,x,y)
        self.__z = z
   def Abs(self):
       x,y = super().getComponents()
       return math.sqrt(pow(x,2)+pow(y,2)+pow(self.__z,2))

   def getComponents(self):
       x,y = super().getComponents()
       return[x,y,self.__z]

   def getAngles(self):
       x,y = super().getComponents()
       
       fi = math.atan(y/x)
       psi = math.atan(math.sqrt(pow(x,2)+ pow(y,2))/self.__z)
       
       angles = [fi, psi]
       return angles
       

   def cdot(self, vector):
       x,y = super().getComponents()
       x_v,y_v,z_v = vector.getComponents()
       dot_product = x *x_v + y*y_v +self.__z *z_v
       return dot_product

   def cross_product(self,vector):
       x_v,y_v,z_v = vector.getComponents()
       x,y = super().getComponents()

       x = y*z_v - (self.__z*y_v)
       y = self.__z *x_v - (self.__x *z_v)
       z = x*y_v - (y *x_v)
       new_vector = [x,y,z]

       
       return new_vector

class Adapter2D:
    #def __init__(self,angle,r):
    def from_polar_to_cartesian(self):
        x = r*math.cos(angle)
        y = r*math.sin(angle)
        return [x,y]

   
class Adapter3D:
    
    def spherical_coordinates(self,fi,psi,r):
       x = r* math.cos(psi)*math.cos(fi)
       y = r*math.cos(psi)*math.sin(fi)
       z = r* math.sin(psi)
       return [x,y,z]



v2= Vector2D(1,1)
v2_2 = Vector2D(1,2)

print(v2.Abs())
print(v2.getAngles())

print("DOOOt",v2.cdot(v2_2))

v3= Vector3D(1,3,5)
v3_2 =Vector3D(1,2,7)
print(v3.Abs())
print(v3.getAngles())
#print(v3.cdot(v3_2))
#print(v3.cross_product(v3_2))
