from manim import *


# AnimationGroup: Parallel Animation
# Scuccession: Sequential Animation

class DHighlight(Succession):
    def __init__(self, mobject, color=YELLOW, **kwargs):
        start_mobject = mobject.copy()
        target_mobject = mobject.copy().scale(1.1).set_color(color)
        super().__init__(
            Transform(mobject, target_mobject),
            Transform(mobject, start_mobject),
            run_time=1, # default run_time
            **kwargs
        )