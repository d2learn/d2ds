from manim import *

from .base import DElement

class DArray(VGroup):

    def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)
        self.elements = elements
        for i, e in enumerate(elements):
            self.add(DElement(str(e)))

        self.arrange(RIGHT)
        self.move_to(ORIGIN)

        # adapt screen size, not too big
        #if self.get_width() > config["frame_width"] - 10:
        #    self.set_width(config["frame_width"] - 10)