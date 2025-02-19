from manim import *

class ParadigmasIntro(Scene):
    def construct(self):
        #titulo
        title = Text("Paradigmas de Programação", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        #def de paradigma
        definition = Text("Paradigma é um estilo ou modelo de programação", font_size=32)
        self.play(FadeIn(definition))
        self.wait(3)
        self.play(FadeOut(definition))

        #linha de tempo
        timeline = NumberLine(x_range=[1950, 2025, 10],length=10,include_numbers=True, decimal_number_config={"num_decimal_places": 0}) #verify
        self.play(Create(timeline))

        #linha do tempo dos tipos de paradigmas
        structured = Text("Estruturada", font_size=26).move_to(timeline.n2p(1960) +  UP * 0.5) #começo do paradigma estruturado
        oop = Text("POO", font_size=26).move_to(timeline.n2p(1980) +  UP * 0.5) #mais ou menos o começo de OOP
        functional = Text("Funcional", font_size=26).move_to(timeline.n2p(1990) +  UP * 0.5) #começo do paradigma funcional (perto)

        self.play(Write(structured))
        self.wait(1)
        self.play(Write(oop))
        self.wait(1)
        self.play(Write(functional))
        self.wait(2)
        self.play(FadeOut(title, structured, oop, functional, timeline))