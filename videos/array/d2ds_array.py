import sys, os
from manim import *

# manim -pql videos/array/d2ds_array.py
# python videos/array/d2ds_array.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libs import *

class D2DSArray(Scene):
    def construct(self):

        contents = DContents([
            "0.基本概念",
            "1.内存布局",
            "2.操作&应用",
        ]).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)

        contents.scale(0.45)

        # 1. topic enter
        arr = self.start_scene()
        self.wait(1)

        self.play(
            Create(contents),
            contents.anim_next_chapter()
        )

        self.wait(1)

        # 2. base concept
        self.base_concept(arr, contents)
        self.wait(1)

    def base_concept(self, arr, contents):

        sub_contents_0_1 = Text("下标随机访问").scale(0.8).to_corner(UL)
        sub_contents_0_2 = Text("相同数据类型").scale(0.8).to_corner(UL)
        sub_contents_0_3 = Text("连续内存空间").scale(0.8).to_corner(UL)

        self.play(ReplacementTransform(contents[0].copy(), sub_contents_0_1))
        self.wait(1)

        arr_subscripts = arr.create_subscripts()
        self.play(Write(arr_subscripts))

        lua_arr_subscripts = arr.create_subscripts(start_index=1)
        lua_arr_subscripts.next_to(arr_subscripts, DOWN)
        lua_arr_subscripts.set_color(PURPLE)

        self.play(ReplacementTransform(arr_subscripts.copy(), lua_arr_subscripts))
        self.wait(1)

        self.play(FadeOut(lua_arr_subscripts))

        sourcecode = """arr[0]"""
        code = Code(code = sourcecode, language="cpp").move_to(LEFT * 2.5 + UP * 1.5)
        self.play(Write(code))
        self.wait(1)

        self.play(
            DHighlight(arr[0]),
            DHighlight(arr_subscripts[0]),
        )

        self.play(
            DHighlight(arr[4]),
            DHighlight(arr_subscripts[4])
        )
        self.wait(1)

        return
        # 2. 下标随机访问
        self.play(
            ReplacementTransform(contents[0].copy(), sub_contents_0_2),
            FadeOut(sub_contents_0_1)
        )
        self.wait(1)

        sourcecode = """int arr[10] = {0, ... ,9};
arr[0] = 333; // ok
arr[0] = "hello"; // error"""
        code = Code(code = sourcecode, language="cpp").move_to(LEFT * 2.5 + UP * 1.5)
        self.play(Write(code))
        self.wait(1)

        # 3. 连续内存空间
        self.play(
            ReplacementTransform(contents[0].copy(), sub_contents_0_3),
            FadeOut(sub_contents_0_2)
        )

        # memory
        return

    def start_scene(self):
        text = Text("你学习的第一个数据结构是什么？")
        self.play(Write(text), run_time=1)
        self.wait(1)

        arr1 = DArray(["数", "组"])
        self.play(Transform(text, arr1))
        self.wait(1)

        arr2 = DArray([i for i in range(1, 10)]).scale(0.5)
        self.play(ReplacementTransform(text, arr2))
        self.wait(1)

        return arr2

if __name__ == "__main__":
    scene = D2DSArray()
    scene.render()