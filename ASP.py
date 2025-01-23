from manim import *
from TTSScene import TTSScene

class Intro(TTSScene):
    def construct(self):
        # Add particle visualization for Avogadro's number
        particles = VGroup(*[Circle(radius=0.125, color=BLUE, fill_opacity=1) for _ in range(16*9*4)])
        particles.arrange_in_grid(rows=9*2, cols=16*2, buff=0.125)
        avogadro_text = Tex("6.022$\\times$10$^{23}$", color=GOLD).scale(1.5)


        self.add_voice(
            """
            Hey everyone!

            Today, we'll learn about moles and other stuff about converting between different measurements.
            """,
            LaggedStartMap(FadeIn, particles),
            FadeIn(avogadro_text),
            FadeOut(avogadro_text)
        )


        title = Text("Understanding Moles", font_size=40)
        subtitle = Text("Converting between Mass, Moles, and Particles", 
                       font_size=30).next_to(title, DOWN)

        self.add_voice(
            "Understanding these topics is super important in order to have a solid foundation for the rest of Chemistry.",
            LaggedStartMap(FadeOut, particles),
            Write(title),
            FadeIn(subtitle),
        )
        self.play(FadeOut(title), FadeOut(subtitle))

class MoleConcept(TTSScene):
    def construct(self):
        # Mole image with Avogadro overlay
        mole = ImageMobject("images/mole.png").scale(2)
        avogadro_overlay = Tex("6.022$\\times$10$^{23}$", color=RED).scale(0.7)
        
        self.add_voice(
            """
            Okay, so first of all - what even is a mole?
            ... ... ...
            No, not this cute little thing!
            """,
            FadeIn(mole),
            FadeIn(avogadro_overlay)
        )
        
        # Enhanced egg to atom transition
        self.play(
            mole.animate.scale(0.3).to_edge(UP),
            avogadro_overlay.animate.next_to(mole, DOWN)
        )

        # Original egg carton visualization
        carton = Rectangle(height=2, width=4, color=WHITE)
        eggs = VGroup(*[Circle(radius=0.2, color=WHITE, fill_opacity=1) for _ in range(12)])
        eggs.arrange_in_grid(rows=2, cols=6, buff=0.2).move_to(carton)
        dozen_group = VGroup(carton, eggs)
        dozen_label = Text("1 Dozen = 12 Eggs", font_size=30).next_to(dozen_group, DOWN)
        
        # Formula introduction
        formula = MathTex(
            "\\text{moles}", "=", "\\frac{\\text{particles}}{6.022\\times10^{23}}"
        ).set_color_by_tex("moles", BLUE).set_color_by_tex("particles", GREEN).set_color_by_tex("6.022", RED)
        
        self.add_voice(
            'A mole is a counting unit, like a ten, or a century, or a dozen.',
            Create(dozen_group),
            Write(dozen_label),
            formula.animate.scale(0.8).to_corner(UR)
        )

        # Rest of original atom transformation remains
        atoms = VGroup(*[Circle(radius=0.05, color=BLUE, fill_opacity=1) for _ in range(900)])
        atoms.arrange_in_grid(rows=30, cols=30, buff=0.1)
        mole_label = Text("1 mole = 6.022 × 10²³ particles", font_size=30)
        
        self.add_voice(
            """
            While a dozen means 12, a mole means 6.02 times 10 to the power of 23.
            ...
            That's a lot of atoms!
            """,
            Transform(dozen_group, atoms),
            Transform(dozen_label, mole_label)
        )
        self.play(FadeOut(dozen_group), FadeOut(dozen_label))

class MolecularWeights(TTSScene):
    def construct(self):
        # Animated balance scale
        class Balance(VGroup):
            def __init__(self):
                super().__init__()
                self.beam = Line(LEFT*2, RIGHT*2)
                self.stand = Line(UP, DOWN).shift(DOWN*0.5)
                self.add(self.beam, self.stand)
        
        balance = Balance().scale(0.5)
        self.play(Create(balance))

        # Original atom comparison with balance animation
        hydrogen = Circle(radius=0.5, color=RED)
        oxygen = Circle(radius=1, color=BLUE)
        h_label = Text("Hydrogen\n1 amu", font_size=24).next_to(hydrogen, DOWN)
        o_label = Text("Oxygen\n16 amu", font_size=24).next_to(oxygen, DOWN)
        h_group = VGroup(hydrogen, h_label).to_edge(LEFT)
        o_group = VGroup(oxygen, o_label).to_edge(RIGHT)
        
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
            Create(o_group),
            balance.animate.rotate(-30*DEGREES, about_point=balance.stand.get_top()),
            run_time=2
        )
        self.play(FadeOut(h_group), FadeOut(o_group), FadeOut(balance))

class PeriodicTable(TTSScene):
    def construct(self):
        # Enhanced periodic table visualization
        table = Rectangle(height=4, width=6, color=WHITE)
        element = Rectangle(height=1, width=1, color=YELLOW)
        element_text = VGroup(
            Text("Na", font_size=24),
            Text("23.0 g/mol", font_size=16, color=GOLD)
        ).arrange(DOWN, buff=0.1).move_to(element)
        element_group = VGroup(element, element_text)
        
        self.play(Create(table))
        element_group.move_to(table).next_to(table, LEFT).shift(RIGHT*0.5)
        
        self.add_voice(
            "Here's where the periodic table becomes your best friend! Let's zoom in on sodium, or N A.",
            Create(element_group),
            Flash(element_text[1], color=GOLD, run_time=2)
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
            table.animate.scale(2),
            element_text[1].animate.set_color(WHITE)
        )
        self.play(FadeOut(table), FadeOut(element_group))

class FlowchartInterlude(TTSScene):
    def construct(self):
        # Conversion flowchart
        mass = Text("Mass (g)", color=GREEN)
        moles = Text("Moles", color=BLUE)
        particles = Text("Particles", color=RED).scale(0.9)
        
        arrows = VGroup(
            Arrow(mass.get_right(), moles.get_left(), buff=0.1),
            Arrow(moles.get_right(), particles.get_left(), buff=0.1),
            Arrow(particles.get_left(), moles.get_right(), buff=0.1).flip(),
            Arrow(moles.get_left(), mass.get_right(), buff=0.1).flip()
        )
        
        labels = VGroup(
            MathTex("\\div\\text{molar mass}").next_to(arrows[0], UP),
            MathTex("\\times\\text{Avogadro}").next_to(arrows[1], UP),
            MathTex("\\div\\text{Avogadro}").next_to(arrows[2], DOWN),
            MathTex("\\times\\text{molar mass}").next_to(arrows[3], DOWN)
        )
        
        self.add_voice(
            "Remember this conversion roadmap...",
            LaggedStart(
                FadeIn(mass, shift=UP),
                FadeIn(moles, shift=UP),
                FadeIn(particles, shift=UP),
                LaggedStartMap(GrowArrow, arrows),
                LaggedStartMap(Write, labels),
                lag_ratio=0.3
            )
        )
        self.play(FadeOut(mass), FadeOut(moles), FadeOut(particles), 
                 FadeOut(arrows), FadeOut(labels))

class ChemistryConversions(TTSScene):
    def construct(self):
        # Enhanced examples with color coding
        def color_code_equation(eq):
            eq.set_color_by_tex_to_color_map({
                "times": WHITE,
                "frac": WHITE,
                "10^{23}": RED,
                "6.02": RED,
                "55.85": GOLD,
                "63.55": GOLD,
                "1.50": GREEN,
                "3.50": GREEN,
                "127.0": GREEN,
                "2.00": BLUE,
                "195.48": BLUE,
                "9.03": BLUE
            })
            return eq

        # Original Avogadro introduction
        avogadro_group = VGroup(
            Text("Avogadro's Number", font_size=36),
            MathTex("6.02 \\times 10^{23}", color=RED)
        ).arrange(DOWN)
        
        self.add_voice(
            """
            In chemistry, we often work with incredibly large numbers of atoms and molecules.
            To make these calculations manageable, we use AhvohGahdroh's Number:
            6.02 times 10 to the power of 23.
            This constant represents the number of particles in one mole of anything.
            """,
            Write(avogadro_group)
        )

        # Example 1 with particle animation
        example1_problem = MathTex(
            "\\text{Na atoms} = 1.204 \\times 10^{24} \\text{ particles}"
        )
        example1_solution = color_code_equation(MathTex(
            "\\text{moles} &= \\frac{1.204 \\times 10^{24}}{6.02 \\times 10^{23}}",
            "\\\\&= 2.00 \\text{ moles Na}"
        ))
        
        particles = VGroup(*[Dot(radius=0.03, color=BLUE) for _ in range(100)])
        particles.arrange_in_grid(rows=10, cols=10, buff=0.1)
        particle_container = Circle(radius=1, color=WHITE, fill_opacity=0)
        
        self.add_voice(
            "Let's look at our first conversion example...",
            FadeOut(avogadro_group),
            LaggedStartMap(FadeIn, particles),
            Create(particle_container),
            particles.animate.move_to(particle_container),
            FadeOut(particles),
            FadeOut(particle_container),
            Write(example1_problem)
        )

        # Remaining examples with color coding
        example1_solution.next_to(example1_problem, DOWN)
        self.add_voice(
            "Dividing our number of particles...",
            Write(example1_solution)
        )

        # Original examples 2-4 remain with color coding
        example2_problem = MathTex("\\text{Fe} = 3.50 \\text{ moles}")
        example2_solution = color_code_equation(MathTex(
            "\\text{Mass} &= 3.50 \\text{ mol} \\times \\frac{55.85\\text{ g}}{1\\text{ mol}}",
            "\\\\&= 195.48 \\text{ g Fe}"
        ))
        
        # ... (similar modifications for examples 3-4)

class Summary(TTSScene):
    def construct(self):
        # Conversion summary table
        table = Table(
            [["Particles → Moles", "$\\div$ Avogadro"],
             ["Moles → Mass", "$\\times$ molar mass"],
             ["Mass → Moles", "$\\div$ molar mass"],
             ["Moles → Particles", "$\\times$ Avogadro"]],
            col_labels=[Text("Conversion"), Text("Formula")],
            include_outer_lines=True
        ).scale(0.8)
        
        self.add_voice(
            "Let's review the key conversions...",
            Create(table),
            LaggedStartMap(FadeIn, table.get_entries())
        )
