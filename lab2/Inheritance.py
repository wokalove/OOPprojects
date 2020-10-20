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
        return round(math.sqrt(pow(self.__x,2)+pow(self.__y,2)),2)
        
    def getComponents(self):
       return[self.__x,self.__y]
        
    def getAngles(self):
        ox = Vector2D(self.__x,0)
        abs_ox = ox.Abs()

        cos = (self.__x*ox.__x + self.__y*ox.__y)/self.Abs()*abs_ox
        angle = math.degrees(math.acos(cos))
        return round(angle,2)

    def cdot(self, vector):
        dot_product = self.__x *vector.__x + self.__y*vector.__y
        return round(dot_product,2)
    
        
class Vector3D(Vector2D):
   def __init__(self,x,y,z):
        Vector2D.__init__(self,x,y)
        self.__z = z
   def Abs(self):
       x,y = super().getComponents()
       return round(math.sqrt(pow(x,2)+pow(y,2)+pow(self.__z,2)),2)

   def getComponents(self):
       x,y = super().getComponents()
       return[x,y,self.__z]

   def getAngles(self):
       x,y = super().getComponents()
       
       fi = math.atan(y/x)
       psi = math.atan(math.sqrt(pow(x,2)+ pow(y,2))/self.__z)
       
       angles = [round(fi,2), round(psi,2)]
       return angles
       

   def cdot(self, vector):
       x,y = super().getComponents()
       x_v,y_v,z_v = vector.getComponents()
       dot_product = x *x_v + y*y_v +self.__z *z_v
       return round(dot_product,2)

   def cross_product(self,vector):
       x_v,y_v,z_v = vector.getComponents()
       x,y = super().getComponents()

       x_p = y*z_v - (self.__z*y_v)
       y_p = self.__z *x_v - (x *z_v)
       z_p = x*y_v - (y *x_v)
       new_vector = [round(x_p,2),round(y_p,2),round(z_p,2)]

       
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
        return [round(x,2),round(y,2)]

   
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
       return [round(x,2),round(y,2),round(z,2)]

def main():
    v2 = Vector2D(1,1)
    v2_2 = Vector2D(1,2)
    print("Abs v2:",v2.Abs(), "| Abs v2_2:",v2_2.Abs())
    print("Components v2:",v2.getComponents(),"| Components v2_2:",v2_2.getComponents())
    print("Angles v2:", v2.getAngles(),"| Angles v2_2:",v2_2.getAngles())
    print("Scalar dot of v2, v2_2:",v2.cdot(v2_2))


    v3 = Vector3D(1,3,5)
    v3_2 = Vector3D(1,2,7)
    print("Abs v3:",v3.Abs(), "| Abs v3_2:",v3_2.Abs())
    print("Components v3:",v3.getComponents(),"| Components v3_2:",v3_2.getComponents())
    print("Angles v3:", v3.getAngles(),"| Angles v3_2:",v3_2.getAngles())
    print("Scalar dot of v3, v3_2:",v3.cdot(v3_2))
    print("Cross product:",v3.cross_product(v3_2))


    a_2D = Adapter2D(3,30)
    print("From polar to cartesian:",a_2D.from_polar_to_cartesian())
    a_3D = Adapter3D(2,30,30)
    print("From spherical to cartesian:",a_3D.spherical_coordinate_to_polar())

if __name__ == "__main__":
    main()



