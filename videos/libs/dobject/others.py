from manim import *

class DContents(VGroup):

    def __init__(self, contents, **kwargs):
        super().__init__(**kwargs)

        for i, e in enumerate(contents):
            self.add(Text(str(e)))

        self.arrange(DOWN)
        self.move_to(ORIGIN)

        self.select_rect = SurroundingRectangle(self[0])
        self.select_rect.set_opacity(0)
        self.add(self.select_rect)

        self.index = -1

    def anim_next_chapter(self):
        # return animation
        self.index = self.index + 1

        if self.index >= len(self) - 1:
            self.index = 0

        return Transform(self.select_rect, self._create_selector())

    def anim_prev_chapter(self):
        self.index = self.index - 1

        if self.index < 0:
            self.index = len(self) - 2

        return Transform(self.select_rect, self._create_selector())

    def _create_selector(self):
        s = SurroundingRectangle(self[self.index])
        s.set_color(YELLOW)
        s.set_opacity(0.15)
        return s