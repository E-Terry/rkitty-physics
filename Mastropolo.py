from manim import *

class ShowCharges(Scene):
    def construct(self):
     
        eName = Tex(r"$e^{-}$", color=BLUE, font_size=75)
        circle1 = Circle(color=BLUE, fill_opacity=0.2).surround(eName, buffer_factor=1.5)
        startSize = circle1.width
        electron = VMobject()
        electron.add(eName, circle1)

        self.play(Create(electron))
        self.play(electron.animate.shift(LEFT*5))

        coulombVal1 = Tex(r"$= -1.6 \times 10^{-19}$", " Mastropolos", font_size=75)
        coulombVal1.next_to(electron, RIGHT, buff=0.25)
        eC = Tex(" C", font_size=75)
        eC.next_to(coulombVal1[0], RIGHT)

        self.play(Write(coulombVal1), run_time=0.5)
        self.wait()

        self.play(Transform(coulombVal1[1], eC))

        electron.add(coulombVal1)

        #I don't know a better way to make 2 animations happen at once
        def toSide(mob):
            mob.scale(0.5)
            mob.to_edge(UL)
            return mob
        self.play(ApplyFunction(toSide, electron))

        proton = VGroup()
        pName = Tex(r"$p^{+}$", color=RED, font_size=75)
        circle2 = Circle(color=RED, fill_opacity=0.2).surround(pName)
        circle2.width=startSize
        proton.add(pName,circle2)
        self.play(Create(proton))
        self.play(proton.animate.shift(LEFT*5))

        coulombVal2 = Tex(r"$= 1.6 \times 10^{-19}$", " Mastropolos", font_size=75)
        coulombVal2.next_to(proton, RIGHT, buff=0.25)
        pC = Tex(" C", font_size=75)
        pC.next_to(coulombVal2[0], RIGHT)

        self.play(Write(coulombVal2), run_time=0.5)
        self.wait()
        self.play(Transform(coulombVal2[1], pC))

        proton.add(coulombVal2)

        def unders(mob):
            mob.scale(0.5)
            mob.next_to(electron, DOWN,)
            mob.align_to(electron, LEFT)
            return mob
        self.play(ApplyFunction(unders, proton))

#####################################################################################
#####################################################################################

        force = str("F")
        q1 = str(r"(q_1)")
        q2 = str(r"(q_2)")
        masLaw = MathTex(force, "= { ", "k", q1, q2 ,r"\over", "r", "^2}")
        self.play(Create(masLaw))
        self.wait()
        self.play(Indicate(masLaw[3]), Indicate(electron), run_time=2)
        self.play(Indicate(masLaw[4]), Indicate(proton), run_time=2)
        self.play(masLaw.animate.to_edge(UR))
        self.wait()

        k = str(r"8.987 \times 10^{9}")
        masCon = Tex("Mastropolo's Constant")
        kDisp = MathTex("k = ", k)
        self.play(Create(VGroup(masCon,kDisp).arrange(DOWN)))
        self.wait(2)
        self.play(Indicate(kDisp), Indicate(masLaw[2]), run_time=2)
        self.wait()

        self.play(FadeOut(masCon), FadeTransform(kDisp,masLaw[2]))
        self.wait()
        
#####################################################################################
#####################################################################################
        eName2 = MathTex("e^{-}", font_size=50).shift(LEFT*2)
        circle3 = Circle(color=BLUE, fill_opacity=0.2).surround(eName2, buffer_factor=1.5)
        startSize1 = circle3.width
        e1 = VMobject()
        e1.add(eName2, circle3)

        pName2 = MathTex("p^{+}", font_size=50).shift(RIGHT*2)
        circle4 = Circle(color=RED, fill_opacity=0.2).surround(pName2)
        circle4.width = startSize1
        p1 = VMobject()
        p1.add(pName2, circle4)

        self.play(Create(p1), masLaw[4].animate.set_color(RED), Create(e1), masLaw[3].animate.set_color(BLUE))
        self.wait()

        Bline = Line(e1.get_center(), p1.get_center())
        b = Brace(Bline, color=GREEN, buff=0.6)
        distance = str("r")
        bText = b.get_text(distance)
        bText.set_color(GREEN)

        self.play(Create(b),Create(bText), masLaw[6].animate.set_color(GREEN))
        self.wait()
        self.play(Indicate(VGroup(b,bText)),Indicate(masLaw[6]), run_time=2)

#####################################################################################
#####################################################################################

        













        self.wait()