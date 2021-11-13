import bpy
from math import radians

##create 10 simple cubes
#for x in range(10):
#    bpy.ops.mesh.primitive_cube_add(location = (x - 5, 0 , 0), size = 0.5)


##Simple function to remobe all the meshes
#for x in bpy.data.meshes:
#    bpy.data.meshes.remove(x)   


#Simple function to move up all the elements
#meshes_reference = []
#for x in bpy.data.objects:
#    try:
#        print(x.data.rotation_euler)
#        x.data.rotation_euler[0] += radians(45)
#    except:
#        pass

#objects = bpy.data.collections["Cubes"].objects
#for x in objects:
#    print(x)
#    
if __name__ == '__main__':
    while True:
        value = input("Put value")
        print(value)            
            
            
            
            
            
            
            
            
            
            
            
        