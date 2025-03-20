import sys, os
from manim import *

# manim -pql videos/array/d2ds_array.py
# python videos/array/d2ds_array.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libs import *

class D2DSArray(Scene):
    def construct(self):
        self.start_scene()
        self.wait(1)

    def start_scene(self):
        text = Text("你第一个接触的数据结构是什么？")
        self.play(Write(text), run_time=1)
        self.wait(1)

        arr1 = DArray(["数", "组"])
        self.play(Transform(text, arr1))
        self.wait(1)

        arr2 = DArray([i for i in range(10)]).scale(0.5)
        self.play(Transform(text, arr2))
        self.wait(1)

if __name__ == "__main__":
    scene = D2DSArray()
    scene.render()