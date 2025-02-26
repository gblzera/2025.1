from manim import *

class EvolutionProgrammingLanguages(Scene):
    def construct(self):
        title = Text("Evolução das Linguagens de Programação", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        decades_info = [
            ("Anos 1950-1960: O Nascimento da Programação", [
                ("Assembly (década de 1950)", "Código de máquina humanamente legível, essencial para programação de baixo nível.", "MOV AX, 4C00h\nINT 21h"),
                ("Fortran (1957)", "Criado pela IBM, pioneiro na computação científica.", "PRINT *, 'Hello, World!'"),
                ("Lisp (1958)", "Introduziu conceitos como listas encadeadas e recursão, influenciando a IA.", "(print \"Hello, World!\")"),
                ("COBOL (1959)", "Voltado para negócios e ainda em uso em sistemas bancários.", "DISPLAY 'Hello, World!'.")
            ]),
            ("Anos 1970: Expansão e Estruturação", [
                ("C (1972)", "Criado para Unix, base para diversas linguagens modernas.", "printf('Hello, World!');"),
                ("Pascal (1970)", "Focado em ensino e boas práticas de programação.", "WriteLn('Hello, World!');"),
                ("Prolog (1972)", "Usado em IA e sistemas especialistas.", "write('Hello, World!').")
            ]),
            ("Anos 1980: Programação Orientada a Objetos", [
                ("C++ (1983)", "Extensão do C com suporte a POO.", "std::cout << 'Hello, World!';"),
                ("Objective-C (1984)", "Base para desenvolvimento no macOS/iOS.", "NSLog(@'Hello, World!');"),
                ("Perl (1987)", "Muito utilizado para scripts e manipulação de texto.", "print 'Hello, World!';")
            ]),
            ("Anos 1990: A Era da Internet", [
                ("Python (1991)", "Simplicidade e legibilidade como foco.", "print('Hello, World!')"),
                ("Java (1995)", "Executável em qualquer sistema via JVM.", "System.out.println('Hello, World!');"),
                ("JavaScript (1995)", "Fundamental para a web interativa.", "console.log('Hello, World!');"),
                ("PHP (1995)", "Voltado para aplicações web dinâmicas.", "echo 'Hello, World!';")
            ]),
            ("Anos 2000: Novos Paradigmas", [
                ("C# (2000)", "Desenvolvimento corporativo na plataforma .NET.", "Console.WriteLine('Hello, World!');"),
                ("Scala (2003)", "Funcional e orientado a objetos.", "println('Hello, World!')"),
                ("Go (2009)", "Eficiência e simplicidade para sistemas distribuídos.", "fmt.Println('Hello, World!')")
            ]),
            ("Anos 2010: Segurança e Eficiência", [
                ("Rust (2010)", "Focado em segurança e performance.", "println!(\"Hello, World!\");"),
                ("Swift (2014)", "Criado para iOS/macOS, mais moderno e seguro.", "print('Hello, World!')"),
                ("TypeScript (2012)", "Superconjunto do JavaScript com tipagem estática.", "console.log('Hello, World!');"),
                ("Julia (2012)", "Voltado para computação científica e alta performance.", "println('Hello, World!')")
            ]),
            ("Anos 2020: IA e Escalabilidade", [
                ("Tendências", "Foco em IA, escalabilidade e segurança na nuvem.", "print('Deep Learning!')")
            ])
        ]

        for decade, languages in decades_info:
            decade_text = Text(decade, font_size=36).to_edge(UP)
            self.play(Write(decade_text))
            self.wait(1)
            
            for lang, desc, example in languages:
                lang_text = Text(lang, font_size=28).shift(UP * 0.5)
                desc_text = Text(desc, font_size=24).shift(DOWN * 0.5)
                example_text = Text(example, font_size=24).shift(DOWN * 2)

                self.play(Write(lang_text))
                self.wait(1)
                self.play(Write(desc_text))
                self.wait(1)
                self.play(Write(example_text))
                self.wait(2)

                self.play(FadeOut(lang_text, desc_text, example_text))

            self.play(FadeOut(decade_text))

        conclusion = Text("A evolução continua!", font_size=32).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))