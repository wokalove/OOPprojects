import numpy as np

class IVector:
    def abs(self,vector):
        vector_abs = np.absolute(vector)
        return vector_abs
    def getComponents(self):
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
    def Vector2D:
        ''' '''

ob =  IVector()
#v1 = [[-1.2,-3.0],[-1.2,-3.1]]
#v2 = [[-4,6],[-1.2,-3.0]]
#print("Abs:",ob.abs(v1))
#print(ob.cdot(v1,v2))
v1= [3,1]
v2= [1,4]
print(ob.getAngles(v1,v2))
