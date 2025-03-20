from manim import *

class DElement(VGroup):
    def __init__(self, text, box_size=2, max_font_size=48, color=BLUE, **kwargs):

        super().__init__(**kwargs)

        self.box = Square(side_length=box_size, color=color)
        
        self.text = Text(text, font_size=max_font_size)
        
        # auto adjust font size
        while self.text.width > box_size * 0.8 or self.text.height > box_size * 0.8:
            self.text.set_font_size(self.text.font_size - 2)
        
        # align text and box
        self.add(self.box, self.text)
        self.text.move_to(self.box.get_center())