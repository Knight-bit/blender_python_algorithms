import bpy
import random
from math import pi, sin, cos 
#Hace translado una funcion más adelante

class SimpleCube:
    
    def __init__(self, location):
        bpy.ops.mesh.primitive_cube_add(size = 0.5, location = location)
        self.reference = bpy.context.object # get the object created
        self.value = int(random.random() * 100)
    
    def translation_xz(self, radius, offset, limit_offset, left):
        r = radius
        self.reference.keyframe_insert(data_path="location", frame = offset)
        grade = 0 if left else pi
        for step in range(int(offset + (limit_offset / 4)), limit_offset + 1, int(limit_offset / 4)):
            grade += (pi / 4)
            #print(f"Cos : {cos(grade) * radius}, Sin: {sin(grade) * radius}")
            self.reference.location = (cos(grade) * radius, 0.0,(sin(grade) * radius) / 4)
            self.reference.keyframe_insert(data_path="location", frame = step)
    
    def __str__(self):
        return f"Object {self.reference}"
      
    
if __name__ == '__main__':
    cube = SimpleCube((3, 0,0 ))
    cube.translation_xz(3, 0, 60, True  )