import bpy

class Text:
    def __init__(self, value):
        bpy.ops.object.text_add()
        self.reference = bpy.context.object # get ref of object created
        self.reference.data.body = f"{value}"
        self.reference.data.font.open(filepath = normpath(f"C:\Windows\Fonts\{Gabriola.ttf}"))
    
    def ohaiho():
        pass

if __name__ == '__main__':
    text = Text(10)