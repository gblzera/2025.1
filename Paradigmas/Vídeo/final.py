from manim import *

class MapaMentalParadigmas(Scene):
    def construct(self):
        # Título inicial
        titulo = Text("Quando usar cada paradigma?", font_size=40)
        self.play(FadeIn(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Paradigma Estruturado
        estruturado_titulo = Text("Paradigma Estruturado", font_size=36, color=BLUE)
        estruturado_caso = Text("✅ Scripts rápidos e simples", font_size=28).next_to(estruturado_titulo, DOWN)
        
        exemplo_estruturado = Text(
            "def soma(n):\n"
            "    total = 0\n"
            "    for i in range(n + 1):\n"
            "        total += i\n"
            "    return total",
            font_size=24
        ).next_to(estruturado_caso, DOWN * 2)

        self.play(FadeIn(estruturado_titulo, estruturado_caso))
        self.wait(2)
        self.play(FadeIn(exemplo_estruturado))
        self.wait(3)
        self.play(FadeOut(estruturado_titulo, estruturado_caso, exemplo_estruturado))

        # Paradigma Orientado a Objetos
        poo_titulo = Text("Paradigma Orientado a Objetos", font_size=36, color=GREEN)
        poo_caso = Text("✅ Grandes sistemas e reuso de código", font_size=28).next_to(poo_titulo, DOWN)

        exemplo_poo = Text(
            "class Soma:\n"
            "    def __init__(self, n):\n"
            "        self.n = n\n"
            "    def calcular(self):\n"
            "        return sum(range(self.n + 1))",
            font_size=24
        ).next_to(poo_caso, DOWN * 2)

        self.play(FadeIn(poo_titulo, poo_caso))
        self.wait(2)
        self.play(FadeIn(exemplo_poo))
        self.wait(3)
        self.play(FadeOut(poo_titulo, poo_caso, exemplo_poo))

        # Paradigma Funcional
        funcional_titulo = Text("Paradigma Funcional", font_size=36, color=PURPLE)
        funcional_caso = Text("✅ Concorrência e cálculos matemáticos", font_size=28).next_to(funcional_titulo, DOWN)

        exemplo_funcional = Text(
            "from functools import reduce\n"
            "soma = lambda n: reduce(lambda x, y: x + y, range(n + 1))",
            font_size=24
        ).next_to(funcional_caso, DOWN * 2)

        self.play(FadeIn(funcional_titulo, funcional_caso))
        self.wait(2)
        self.play(FadeIn(exemplo_funcional))
        self.wait(3)
        self.play(FadeOut(funcional_titulo, funcional_caso, exemplo_funcional))

        # Mensagem final
        mensagem_final = Text(
            "O melhor paradigma é aquele que resolve o problema\n"
            "de forma mais eficiente no contexto certo!", font_size=36
        )
        self.play(FadeIn(mensagem_final))
        self.wait(4)
        self.play(FadeOut(mensagem_final))
