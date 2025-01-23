from manim import *
from TTSScene import TTSScene

class Intro(TTSScene):
    def construct(self):
        introtext = """
            Hey everyone!

            Today, we'll learn about moles and other stuff about converting between different measurements.
            These topics are super important to understand in order to have a solid foundation for the rest of Chemistry.
        """
        title = Text("Understanding Moles", font_size=40)
        subtitle = Text("Converting between Mass, Moles, and Particles", 
                       font_size=30).next_to(title, DOWN)

        self.add_voice(
            introtext,
            Write(title),
            FadeIn(subtitle),
            voice_offset=1
        )

        self.play(FadeOut(title), FadeOut(subtitle))

class MoleConcept(TTSScene):
    def construct(self):
        # First, we'll add a cute little mole 
        mole = ImageMobject("images/mole.png")
        mole.scale(2)
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
                        for _ in range(900)])
        atoms.arrange_in_grid(rows=30, cols=30, buff=0.1)
        
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

class MolecularWeights(TTSScene):
    def construct(self):
        # Create atom size comparison
        hydrogen = Circle(radius=0.5, color=RED)
        oxygen = Circle(radius=1, color=BLUE)
        
        h_label = Text("Hydrogen\n1 amu", font_size=24).next_to(hydrogen, DOWN)
        o_label = Text("Oxygen\n16 amu", font_size=24).next_to(oxygen, DOWN)
        
        h_group = VGroup(hydrogen, h_label).to_edge(LEFT).shift(RIGHT * 0.5)
        o_group = VGroup(oxygen, o_label).to_edge(RIGHT).shift(LEFT * 0.5)
        
        self.add_voice(
            """
            One thing that can be confusing at first, is:
            "Why do moles of different elements weigh different amounts?"

            Think about it this way: it's like comparing ping pong balls to bowling balls.
            If you had a dozen ping pong balls and a dozen bowling balls, they wouldn't weigh the same, right?

            It's the same with atoms!

            Here, Hydrogen is our ping pong ball ... super light.
            But oxygen is our bowling ball ... super heavy because it's got more stuff packed into it.
            """,
            Create(h_group),
            Create(o_group)
        )
        self.play(FadeOut(h_group), FadeOut(o_group))

class PeriodicTable(TTSScene):
    def construct(self):
        # Create simplified periodic table
        table = Rectangle(height=4, width=6, color=WHITE)
        element = Rectangle(height=1, width=1, color=YELLOW)
        element_text = VGroup(
            Text("Na", font_size=24),
            Text("23.0 g/mol", font_size=16)
        ).arrange(DOWN, buff=0.1)
        element_text.move_to(element)
        element_group = VGroup(element, element_text)
        
        
        self.play(Create(table))
        element_group.move_to(table)
        element_group.next_to(table, LEFT).shift(RIGHT, 0.5)
        self.add_voice(
            """
            Here's where the periodic table becomes your best friend! Let's zoom in on sodium, or N A.
            """,
            Create(element_group)
        )
        
        self.add_voice(
            """
            See that number under sodium? ... 23 grams per mole?

            ...
            ...
            ...

            That tells us that one mole of sodium atoms has a mass of 23 grams.
            Every element on the periodic table has its own unique atomic mass. 
            The atomic mass is how much one mole of that element weighs.
            """,
            element_group.animate.scale(2),
            table.animate.scale(2)
        )
        self.wait()
        self.play(
            FadeOut(table),
            FadeOut(element_group),
        )
class ChemistryConversions(TTSScene):
    def construct(self):
        # Avogadro's Number Introduction (unchanged)
        avogadro = MathTex("6.02 \\times 10^{23}")
        avogadro_text = Text("Avogadro's Number", font_size=36)
        avogadro_group = VGroup(avogadro_text, avogadro).arrange(DOWN)

        self.add_voice(
            """
            In chemistry, we often work with incredibly large numbers of atoms and molecules.
            To make these calculations manageable, we use AhvohGahdroh's Number:
            6.02 times 10 to the power of 23.
            This constant represents the number of particles in one mole of anything.
            """,
            Write(avogadro_group)
        )

        # Example 1: Number of particles to Moles (Sodium)
        example1_problem = MathTex(
            "\\text{Na atoms} = 1.204 \\times 10^{24} \\text{ particles}"
        )
        
        example1_solution = MathTex(
            "\\text{moles} &= \\frac{1.204 \\times 10^{24}}{6.02 \\times 10^{23}}",
            "\\\\&= 2.00 \\text{ moles Na}"
        )
       
        self.add_voice(
            """
            Let's look at our first conversion example.
            We have 1.204 times 10 to the power of 24 sodium atoms.
            To find the number of moles, we'll divide by AhvohGahdroh's Number.
            """,
            FadeOut(avogadro_group),
            Write(example1_problem)
        )
        
        self.play(example1_problem.animate.shift(UP * 0.5))
        example1_solution.next_to(example1_problem, DOWN)
        self.add_voice(
            """
            Dividing our number of particles by AhvohGahdroh's Number,
            we get 2.00 moles of sodium.
            """,
            Write(example1_solution)
        )

        # Example 2: Moles to Mass (Iron)
        example2_problem = MathTex(
            "\\text{Fe} = 3.50 \\text{ moles}"
        )
        
        example2_solution = MathTex(
            "\\text{Mass} &= 3.50 \\text{ mol} \\times \\frac{55.85\\text{ g}}{1\\text{ mol}}",
            "\\\\&= 195.48 \\text{ g Fe}"
        )
        
        self.add_voice(
            """
            For our second example, we have 3.5 moles of iron.
            Iron has an atomic mass of 55.85 grams per mole.
            To find the mass in grams, we'll multiply the moles by the atomic mass.
            """,
            FadeOut(example1_problem, example1_solution),
            Write(example2_problem)
        )
        
        self.add_voice(
            """
            Multiplying 3.50 moles by 55.85 grams per mole,
            we get 195.48 grams of iron.
            """,
            Write(example2_solution)
        )

        # Example 3: Mass to Moles (Copper)
        example3_problem = MathTex(
            "\\text{Cu} = 127.0 \\text{ g}"
        )
        
        example3_solution = MathTex(
            "\\text{moles} &= 127.0 \\text{ g} \\times \\frac{1\\text{ mol}}{63.55\\text{ g}}",
            "\\\\&= 2.00 \\text{ mol Cu}"
        )
        
        self.add_voice(
            """
            Our third example starts with 127 grams of copper.
            Copper's atomic mass is 63.55 grams per mole.
            To convert to moles, we'll divide the mass by the atomic mass.
            """,
            FadeOut(example2_problem, example2_solution),
            Write(example3_problem)
        )
        
        self.add_voice(
            """
            Dividing 127.0 grams by 63.55 grams per mole,
            we get exactly 2.00 moles of copper.
            """,
            Write(example3_solution)
        )

        # Example 4: Moles to Number of Particles (Aluminum)
        example4_problem = MathTex(
            "\\text{Al} = 1.50 \\text{ moles}"
        )
        
        example4_solution = MathTex(
            "\\text{particles} &= 1.50 \\text{ mol} \\times 6.02 \\times 10^{23} \\frac{\\text{particles}}{\\text{mol}}",
            "\\\\&= 9.03 \\times 10^{23} \\text{ Al atoms}"
        )
        
        self.add_voice(
            """
            Finally, let's convert 1.50 moles of aluminum to atoms.
            To find the number of atoms, we'll multiply the moles by AhvohGahdroh's Number
            """,
            FadeOut(example3_problem, example3_solution),
            Write(example4_problem)
        )
        
        self.add_voice(
            """
            Multiplying 1.50 moles by 6.02 times 10 to the 23rd particles per mole,
            we get 9.03 times 10 to the power of 23 aluminum atoms.
            """,
            Write(example4_solution)
        )
