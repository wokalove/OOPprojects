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
    def cdot(self,vector):
        pass
 
class Vector2D(IVector):
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    def Abs(self):
        return round(math.sqrt(pow(self._x,2)+pow(self._y,2)),2)
        
    def getComponents(self):
       return[self._x,self._y]
        
    def getAngles(self):
        ox = Vector2D(self._x,0)
        abs_ox = ox.Abs()

        cos = (self._x*ox._x + self._y*ox._y)/self.Abs()*abs_ox
        angle = math.degrees(math.acos(cos))
        return round(angle,2)

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
       return round(math.sqrt(pow(x,2)+pow(y,2)+pow(self.__z,2)),2)

   def getComponents(self):
       x, y = self.__vector.getComponents()
       return[x,y,self.__z]

   def getAngles(self):
       x, y = self.__vector.getComponents()
       fi = math.atan(y/x)
       psi = math.atan(math.sqrt(pow(x,2)+ pow(y,2))/self.__z)
       
       angles = [round(fi,2),round(psi,2)]
       return angles

   def cdot(self, vector):
       x, y = self.__vector.getComponents()
       x_v,y_v,z_v = vector.getComponents()
       dot_product = x *x_v + y *y_v +self.__z *z_v
       return round(dot_product,2)

class Decorator(Vector3D):
    def cross_product(self,vector):
        x,y,z = self.getComponents()
        x_2,y_2,z_2 = vector.getComponents()
        x_v = y*z_2 - (z*y_2)
        y_v = z *x_2 - (x *z_2)
        z_v = x*y_2 - (y *x_2)
        new_vector = Vector3D(x_v,y_v,z_v)
        return new_vector

class VectorAdapter2D:
    @abstractmethod
    def from_polar_to_cartesian(self):
        pass
class Adapter2D(VectorAdapter2D):
    def __init__(self,r,angle):
        self.r = r
        self.angle = angle
    def from_polar_to_cartesian(self):
        x = self.r*math.cos(math.radians(self.angle))
        y = self.r*math.sin(math.radians(self.angle))
        vector = Vector2D(round(x,2),round(y,2))
        return vector

   
class VectorAdapter3D:
    @abstractmethod
    def spherical_coordinate_to_polar(self):
        pass
class Adapter3D(VectorAdapter3D):
    def __init__(self,r,psi,fi):
        self.__r = r
        self.__psi = psi
        self.__fi = fi
    def spherical_coordinate_to_polar(self):
        x = self.__r* math.sin(math.radians(self.__psi))*math.cos(math.radians(self.__fi))
        y = self.__r*math.sin(math.radians(self.__psi))*math.sin(math.radians(self.__fi))
        z = self.__r* math.cos(math.radians(self.__psi))
        vector = Vector3D(round(x,2),round(y,2),round(z,2))
        return vector

        

def main():
    v2 = Vector2D(1,1)
    v2_2 = Vector2D(1,2)
    print("Abs v2:",v2.Abs(), "| Abs v2_2:",v2_2.Abs())
    print("Components v2:",v2.getComponents(),"| Components v2_2:",v2_2.getComponents())
    print("Angles v2:", v2.getAngles(),"| Angles v2_2:",v2_2.getAngles())
    print("Scalar dot of v2, v2_2:",v2.cdot(v2_2))


    v3 = Vector3D(1,3,5)
    v3_2 = Vector3D(1,2,7)
    decorator = Decorator(1,3,5)
    print("Abs v3:",v3.Abs(), "| Abs v3_2:",v3_2.Abs())
    print("Components v3:",v3.getComponents(),"| Components v3_2:",v3_2.getComponents())
    print("Angles v3:", v3.getAngles(),"| Angles v3_2:",v3_2.getAngles())
    print("Scalar dot of v3, v3_2:",v3.cdot(v3_2))
    print("Cross product:",decorator.cross_product(v3_2).getComponents())



    a_2D = Adapter2D(3,30)
    print("From polar to cartesian:",a_2D.from_polar_to_cartesian().getComponents())
    a_3D = Adapter3D(2,30,30)
    print("From spherical to cartesian:",a_3D.spherical_coordinate_to_polar().getComponents())

if __name__ == "__main__":
    main()










