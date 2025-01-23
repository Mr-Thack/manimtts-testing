from manim import *
from TTSScene import TTSScene


class ChemistryConversions(TTSScene):
    def construct(self):
        self.set_voice("am_adam")

        self.intro()

        # Mole concept using egg carton analogy
        self.explain_mole_concept()
        
        # Molecular weights explanation
        self.explain_molecular_weights()
        
        # Periodic table demonstration
        self.show_periodic_table()
        
        # Conversion examples
        self.show_conversion_examples()

    def intro(self):
        introtext = """
            Hey everyone!

            Today, we'll learn about moles and other stuff about converting between different measurements.
            These topics are super important to understand in order to have a solid foundation for the rest of Chemistry.
        """
        title = Text("Understanding Moles", font_size=40)
        subtitle = Text("Converting between Mass, Moles, and Particles", 
                       font_size=30).next_to(title, DOWN)
        
        # self.add_voice(introtext)
        self.add_voice(
            introtext,
            Write(title),
            FadeIn(subtitle),
            voice_offset=1
        )
        

        self.play(FadeOut(title), FadeOut(subtitle))

    def explain_mole_concept(self):
        # First, we'll add a cute little mole 
        mole = ImageMobject("images/mole.png")
        self.add_voice(
            """
            Okay, so first of all - what even is a mole?
            ... ... ...
            No, not this cute little thing!
            """,
            FadeIn(mole)
        )
        self.play(FadeOut(mole))

        # Create egg carton visual
        carton = Rectangle(height=2, width=4, color=WHITE)
        eggs = VGroup(*[Circle(radius=0.2, color=WHITE, fill_opacity=1)
                       for _ in range(12)])
        eggs.arrange_in_grid(rows=2, cols=6, buff=0.2)
        eggs.move_to(carton)
        dozen_group = VGroup(carton, eggs)

        # Create atom representation
        atoms = VGroup(*[Circle(radius=0.05, color=BLUE, fill_opacity=1)
                        for _ in range(1600)])
        atoms.arrange_in_grid(rows=40, cols=40, buff=0.1)
        
        dozen_label = Text("1 Dozen = 12 Eggs", font_size=30)
        dozen_label.next_to(dozen_group, DOWN)
        
        mole_label = Text("1 mole = 6.022 × 10²³ particles", font_size=30)

        # Animation sequence
        self.add_voice(
            'A mole is a counting unit, like a ten, or a century, or a dozen.',
            Create(dozen_group),
            Write(dozen_label)
        )

        self.add_voice(
            """
            While a dozen means 12, a mole means 6.02 times 10 the power of 23.
            ...
            That's a lot of atoms!
            """,
            Transform(dozen_group, atoms),
            Transform(dozen_label, mole_label)
        )
        self.play(FadeOut(dozen_group), FadeOut(dozen_label))

    def explain_molecular_weights(self):
        # Create atom size comparison
        hydrogen = Circle(radius=0.5, color=RED)
        oxygen = Circle(radius=1, color=BLUE)
        
        h_label = Text("Hydrogen\n1 amu", font_size=24).next_to(hydrogen, DOWN)
        o_label = Text("Oxygen\n16 amu", font_size=24).next_to(oxygen, DOWN)
        
        h_group = VGroup(hydrogen, h_label).to_edge(LEFT).shift(RIGHT * 0.2)
        o_group = VGroup(oxygen, o_label).to_edge(RIGHT).shift(LEFT * 0.2)
        
        self.add_voice(
            """
            Now, one thing that can be confusing at first, is:
            "Why do moles of different elements weigh different amounts?"

            ...
            
            Think about it this way: it's like comparing ping pong balls to bowling balls.
            If you had a dozen ping pong balls and a dozen bowling balls, they wouldn't weigh the same, right?
            
            ...

            It's the same with atoms!

            ...

            Here, Hydrogen is our ping pong ball ... super light.
            But oxygen is our bowling ball ... super heavy because it's got more stuff packed into it.
            """,
            Create(h_group),
            Create(o_group)
        )
        self.wait(2)
        self.play(FadeOut(h_group), FadeOut(o_group))

    def show_periodic_table(self):
        # Create simplified periodic table
        table = Rectangle(height=4, width=6, color=WHITE)
        element = Rectangle(height=0.8, width=0.8, color=YELLOW)
        element_text = VGroup(
            Text("Na", font_size=24),
            Text("23.0 g/mol", font_size=16)
        ).arrange(DOWN, buff=0.1)
        element_text.move_to(element)
        element_group = VGroup(element, element_text)
        
        # Create magnifying glass effect
        magnifier = Circle(radius=1, color=WHITE)
        handle = Line(
            magnifier.get_bottom(),
            magnifier.get_bottom() + DOWN + RIGHT,
            color=WHITE
        )
        magnifying_glass = VGroup(magnifier, handle)
        
        self.play(Create(table))
        element_group.move_to(table)
        self.play(Create(element_group))
        
        magnifying_glass.next_to(element_group, UP)
        self.play(Create(magnifying_glass))
        self.play(
            magnifying_glass.animate.scale(1.5),
            element_group.animate.scale(1.5)
        )
        self.wait()
        self.play(
            FadeOut(table),
            FadeOut(element_group),
            FadeOut(magnifying_glass)
        )

    def show_conversion_examples(self):
        # Example conversion equations
        conversions = VGroup(
            Text("Mass ↔ Moles:", font_size=36),
            Text("4.6g Na × (1 mol/23.0g) = 0.2 mol Na", font_size=30),
            Text("Moles ↔ Particles:", font_size=36),
            Text("0.2 mol Na × (6.022×10²³ atoms/1 mol) = 1.2×10²³ atoms", font_size=30)
        ).arrange(DOWN, buff=0.5)
        
        for i in range(len(conversions)):
            self.play(Write(conversions[i]))
            self.wait()
        
        self.wait(2)
        self.play(FadeOut(conversions))
