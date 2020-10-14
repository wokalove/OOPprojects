import numpy as np

class IVector:
    def abs(self,vector):
        vector_abs = np.absolute(vector)
        return vector_abs
    def getComponents(self, vector):
        x = vector[1][0] - vector[0][0]
        y = vector[1][1] - vector[0][1]
        
        x_component = [vector[0],[vector[0][0]+x,vector[0][1]]]
        #y_component = [vector[0],vector[]]
        print(x_component)
        
        print(vector[1][1],vector[0][1])
        '''  '''
    def getAngles(self,vector1,vector2):
        unit_vector1 = vector1 / np.linalg.norm(vector1)
        unit_vector2 = vector2 / np.linalg.norm(vector2)
        dot_product = np.dot(unit_vector1, unit_vector2)
        angle = np.arccos(dot_product)
        return angle
        
    def cdot(self, vector1,vector2):
        dot_product = np.dot(vector1, vector2)
        return dot_product
class Vector2D:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    #def Vector2D:
     #   ''' '''

ob =  IVector()
v1 = [[-1.2,-3.0],[-1.2,-3.1]]
#v1 = [[3,1.0],[4.0,2.0]]
v2 = [[-4,6],[-1.2,-3.0]]
#print("Abs:",ob.abs(v1))
#print(ob.cdot(v1,v2))


print(ob.getAngles(v1,v2))
print(ob.getComponents(v1))
