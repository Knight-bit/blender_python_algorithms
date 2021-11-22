import bpy
import random


class Rows:
    def __init__(self, x_z):
        self.value = random.random() * 10
        bpy.ops.mesh.primitive_cube_add(location = (x_z, self.value, x_z), scale = (.5, self.value, .5))
        self.reference = bpy.context.object
        
    def change_color(self, color):
        self.reference.active_material = color
    
    
if __name__ == '__main__':
    row = Rows(0)
    color = bpy.data.materials["Rojo"]
    #print(color)