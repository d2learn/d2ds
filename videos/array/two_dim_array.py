import sys, os
from manim import *

# manim v0.18.1
# manim -pql videos/array/two_dim_array.py
# python videos/array/two_dim_array.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libs import *

class D2DSTwoDimArray(Scene):
    def construct(self):

        contents = DContents([
            "0.内存布局",
            "1.行/列优先存储",
            "2.性能/局部性原理",
        ]).arrange(DOWN, aligned_edge=LEFT).move_to(UR * 3 + RIGHT * 2)

        contents.scale(0.45)

        one_dim_arr =  DArray([i for i in range(1, 13)]).scale(0.3)

        mem_loyout = DMemory(
            [i for i in range(1, 13)],
            ["0x0000", "0x0004", "0x0008", "0x000C", 
             "0x0010", "0x0014", "0x0018", "0x001C",
             "0x0020", "0x0024", "0x0028", "0x002C"],
        ).move_to(RIGHT * 4).scale(0.8)

        self.play(Create(one_dim_arr))

        self.play(
            ReplacementTransform(one_dim_arr.copy(), mem_loyout),
            one_dim_arr.animate.move_to(LEFT * 2.5),
        )

        two_dim_array = DTwoDimArray([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
        ]).scale(0.3).next_to(one_dim_arr, ORIGIN).shift(DOWN * 0.5)

        self.play(
            ReplacementTransform(one_dim_arr.copy(), two_dim_array),
            one_dim_arr.animate.shift(UP * 2),
        )

        self.play(DHighlight(two_dim_array))

        for i in range(0, 4):
            self.play(
                DHighlight(two_dim_array[i]),
                DHighlight(VGroup(mem_loyout.mem[i * 3], mem_loyout.mem[i * 3 + 1], mem_loyout.mem[i * 3 + 2])),
                run_time=0.5,
            )


        #self.play(Create(contents))

        self.wait()


if __name__ == "__main__":
    scene = D2DSTwoDimArray()
    scene.render()