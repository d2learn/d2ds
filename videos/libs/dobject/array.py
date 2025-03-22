from manim import *

from .base import DElement

class DArray(VGroup):

    def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)
        for i, e in enumerate(elements):
            self.add(DElement(str(e)))

        self.arrange(RIGHT)
        self.move_to(ORIGIN)

    def create_subscripts(self, scale=0.6, start_index = 0, offset=DOWN * 1.5):
        sub_scripts = VGroup()

        for i in range(len(self)):
            sub_scripts.add(Text(str(i + start_index)).scale(scale).next_to(self[i], offset))

        sub_scripts.set_color(ORANGE)

        return sub_scripts