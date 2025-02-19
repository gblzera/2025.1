from manim import *

class ExemplosParadigmas(Scene):
    def construct(self):
        # PE
        structured_title = Text("Programação Estruturada", font_size=36)
        self.play(FadeIn(structured_title))
        self.play(FadeOut(structured_title))

        structured_code = Text(
            "C:\n"


            "#include <stdio.h>\n"
            "int soma(int n) {\n"
            "    int total = 0;\n"
            "    for (int i = 1; i <= n; i++) {\n"
            "        total += i;\n"
            "    }\n"
            "    return total;\n"
            "}", 
            font_size=24, font="Courier"
        )
        self.play(FadeIn(structured_code))
        self.wait(3)
        self.play(FadeOut(structured_code))

        # POO
        oop_title = Text("Programação Orientada a Objetos", font_size=36)
        self.play(FadeIn(oop_title))
        self.wait(1)
        self.play(FadeOut(oop_title))

        oop_code = Text(
            "Java:\n"


            "class Pessoa {\n"
            "    String nome;\n"
            "    public Pessoa(String nome){\n"
            "    this.nome = nome;\n"
            "    }\n"
            "    public void dizerOla(){\n"
            "    System.out.println('Olá, meu nome é ' + nome);\n"
            "    }\n"
            "}\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Pessoa p = new Pessoa('Gabriel');\n"
            "        p.dizerOla();\n"
            "    }\n"
            "}", 
            font_size=24, font="Courier"
        )
        self.play(FadeIn(oop_code))
        self.wait(3)
        self.play(FadeOut(oop_code))

        # PF (nao é prato feito)
        functional_title = Text("Programação Funcional", font_size=36)
        self.play(FadeIn(functional_title))
        self.wait(1)
        self.play(FadeOut(functional_title))

        functional_code = Text(
            "Python:\n"



            "numeros = [1, 2, 3, 4]\n"
            "dobrados = list(map(lambda x: x * 2, numeros))\n"
            "print(dobrados)  # Saída: [2, 4, 6, 8]",
            font_size=24, font="Courier"
        )
        self.play(FadeIn(functional_code))
        self.wait(3)
        self.play(FadeOut(functional_code))

        final_message = Text("Cada paradigma tem seu propósito e aplicação!", font_size=36)
        self.play(FadeIn(final_message))
        self.wait(3)
        self.play(FadeOut(final_message))
