import bpy
import random
from math import pi, cos, sin
data_font =  bpy.data.fonts.load(filepath="//..\\..\\..\\..\\..\\Windows\\Fonts\\Gabriola.ttf")            

class SimpleCube:
    
    def __init__(self, location):
        bpy.ops.mesh.primitive_cube_add(size = 0.5, location = location)
        self.reference = bpy.context.object # get the object created
        self.value = int(random.random() * 100)
        self.text = Text(self.value, self.reference)
        
    """    
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
    """
    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"Object {self.reference}"            

def intercambie_position(cube_a, cube_b, offset):
    cube_a.reference.keyframe_insert(data_path="location", frame = offset)
    cube_b.reference.keyframe_insert(data_path="location", frame = offset)
    left = True if cube_a.reference.location.x < cube_b.reference.location.x else False
    step = 15
    #Subimos un espacio arriba
    set_keyframes_zx(cube_a, offset + step, cube_a.reference.location.x , -1 if left else 1) 
    set_keyframes_zx(cube_b, offset + step, cube_b.reference.location.x , 1 if left else -1)
    
    #Intercambiamos posicion x en ambos cubos
    a_x = cube_b.reference.location.x
    b_x = cube_a.reference.location.x
    set_keyframes_zx(cube_a, offset + step * 3, a_x , -1 if left else 1) 
    set_keyframes_zx(cube_b, offset + step * 3, b_x , 1 if left else -1)
    
    #Intercambiamos posicion x en ambos cubos
    set_keyframes_zx(cube_a, offset + step * 4, cube_a.reference.location.x , 0) 
    set_keyframes_zx(cube_b, offset + step * 4, cube_b.reference.location.x , 0) 

def set_keyframes_zx(cube, step, location_x, location_y):
    cube.reference.location = (location_x, location_y, 0.0 )
    cube.reference.keyframe_insert(data_path="location", frame = step)
  
"""
def set_keyframes_zx(cube, step, grade, radius):
    cube.reference.location = (cos(grade) * radius + radius , (sin(grade) * radius ), 0.0 )
    cube.reference.keyframe_insert(data_path="location", frame = step)
""" 
def distance(cube_a, cube_b):
    x  = cube_b.reference.location.x - cube_a.reference.location.x 
    y  = cube_b.reference.location.y - cube_a.reference.location.y 
    z  = cube_b.reference.location.z - cube_a.reference.location.z
    return  (( x ** 2 + y**2 + z**2)**(1/2)) / 2

class Text:
    def __init__(self, value, cube):
        bpy.ops.object.text_add(location = (cube.location.x, cube.location.y, 1))
        self.reference = bpy.context.object # get ref of object created
        self.reference.data.font = data_font
        self.reference.data.body = f"{value}"
        #self.reference.location = (cube.location.x, cube.location.y, 1)
        self.reference.parent = cube
        self.reference.matrix_parent_inverse = cube.matrix_world.inverted()
    

def set_parent(father, child):
    child.parent = father
      

def insertionSort(cube):
    N = len(cube)
    sum = 0
    offset = 0
    for x in range(1, N, 1):
        j = x
        while(j > 0 and cube[j].value < cube[j - 1].value):
            t = cube[j]
            cube[j] = cube[ j - 1]
            cube[j - 1] = t
            intercambie_position(cube[j- 1], cube[j], offset)
            offset += 60
            j -= 1
            sum += 1
    print(f"sum equals {sum}")


"""
def selectionSort(cube):
    N = len(cube)
    offset = 0
    for x in range(N):
        min = x
        for j in range(x + 1, N):
            if(cube[j].value < cube[min].value): 
                min = j;
        t = cube[x]
        cube[x] = cube[min]
        cube[min] = t
        intercambie_position(cube[x], cube[min], offset)
        offset += 60
"""
def selectionSort(cube):
    N = len(cube)
    offset = 0
    for x in range(N):
        min = x
        for j in range(x + 1, N):
            if(cube[j].value < cube[min].value): 
                min = j;
        exch(cube, x, min, offset)
        offset += 60

def shellSort(cube):
    N = len(cube)
    h = 1
    offset = 0
    while(h < N/3):
        h = int(3 * h + 1)
    while(h >= 1):
        for x in range(h, N):
            j = x
            while( j >= h and cube[j].value < cube[j - h].value):
                exch(cube, j, j-h, offset)
                offset += 60
                j -= h
        h = int( h / 3 )
        
"""
   public static void sort(Comparable[] a)
     { 
        int N = a.length;
        int h = 1;
        while (h < N/3) h = 3*h + 1; // 1, 4, 13, 40, 121, 364, 1093, ...
        while (h >= 1)
        { // h-sort the array.
            for (int i = h; i < N; i++)
            { // Insert a[i] among a[i-h], a[i-2*h], a[i-3*h]... .
                for (int j = i; j >= h && less(a[j], a[j-h]); j -= h)
                    exch(a, j, j-h);
            }
        h = h/3;
        }
     }
"""
def exch(cube, i, j, offset):
    t = cube[j]
    cube[j] = cube[i]
    cube[i] = t
    intercambie_position(cube[i], cube[j], offset)

    
if __name__ == '__main__':
    cube = [SimpleCube(( x, 0, 0 )) for x in range(10)]
    #selectionSort(cube)
    shellSort(cube)
    #print(lista) 
    #print(cubo[0].value)
    #cube_a = SimpleCube((-5 , 0, 0))
    #cube_b = SimpleCube((5, 0, 0))
    #intercambie_position(cube_a, cube_b, 0)  