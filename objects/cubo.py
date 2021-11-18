import bpy
import random
from math import pi, sin, cos


#Class to get reference of the cube and other values
def distance_between_points(location_a, location_b): #Usa Vectores para calcular la distancia
    return ((location_b.x - location_a.x)**2 + (location_b.z - location_a.z)**2 + (location_b.y - location_a.y)**2 )**(1/2)

class SimpleCube:
    def __init__(self, location):
        bpy.ops.mesh.primitive_cube_add(size = 0.5, location = location)
        self.reference = bpy.context.object # get the object created
        self.value = int(random.random() * 100)
        
    def __str__(self):
        return f"Object {self.reference}"
    
    def translation_xz(self, radius, offset, limit_offset, left):
        r = radius
        self.reference.keyframe_insert(data_path="location", frame = offset)
        grade = 0 if left else pi
        for step in range(int(offset + (limit_offset / 4)), limit_offset + 1, int(limit_offset / 4)):
            grade += (pi / 4)
            location = self.get_location()
            #print(f"Cos : {cos(grade) * radius}, Sin: {sin(grade) * radius}")
            self.reference.location = (cos(grade) * radius, 0.0,(sin(grade) * radius) / 4)
            self.reference.keyframe_insert(data_path="location", frame = step)
            
        
    def get_location(self):
        return self.reference.location 
    
    def scale(self, scale): # scale must be a array of 3 floats
        self.reference.scale = scale
        
if __name__ == '__main__':
    cubos = []
    for x in range(10):
        cubos.append( SimpleCube( location = ( 5 - x, 0, 0)))
        
    for x in range(10):
        print(cubos[x].get_location().x)

    radio = distance_between_points(cubos[0].get_location(), cubos[9].get_location()) / 2
    cubos[0].translation_xz(radio, 0, 60, True)
    cubos[9].translation_xz(radio, 0, 60, False)
        
# call the value with .get_location().<x , y, z>