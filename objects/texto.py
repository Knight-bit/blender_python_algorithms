import bpy
 
data_font =  bpy.data.fonts.load(filepath="//..\\..\\..\\..\\..\\Windows\\Fonts\\Gabriola.ttf")


class Text:
    def __init__(self, value):
        bpy.ops.object.text_add()
        self.reference = bpy.context.object # get ref of object created
        self.reference.data.font = data_font
        self.reference.data.body = f"{value}"
        
        
    def ohaiho():
        pass

if __name__ == '__main__':
    text = Text(10)
    text1 = Text(20)
    text1.reference.parent = text.reference