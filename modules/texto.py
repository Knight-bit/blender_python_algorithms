import bpy
from os.path import normpath
 
data_font =  bpy.data.fonts.load(filepath="//..\\..\\..\\..\\..\\Windows\\Fonts\\Gabriola.ttf")


class Text:
    def __init__(self, value):
        bpy.ops.object.text_add()
        self.reference = bpy.context.object # get ref of object created
        self.reference.data.font = data_font
        self.reference.data.body = f"{value}"
        

def set_parent(father, child):
    child.parent = father

if __name__ == '__main__':
    text = Text(10)
    text1 = Text(20)
    set_parent(text.reference, text1.reference)