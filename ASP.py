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
        
        self.add_voice(
            """
            Okay, so first of all - what even is a mole?
            """,
            FadeIn(mole)
        )
        
        # Enhanced egg to atom transition
        self.add_voice(
            "No, not this cute little thing!",
            mole.animate.scale(0).to_edge(UP),
        )

        # Original egg carton visualization
        carton = Rectangle(height=2, width=4, color=WHITE)
        eggs = VGroup(*[Circle(radius=0.2, color=WHITE, fill_opacity=1) for _ in range(12)])
        eggs.arrange_in_grid(rows=2, cols=6, buff=0.2).move_to(carton)
        dozen_group = VGroup(carton, eggs)
        dozen_label = Text("1 Dozen = 12 Eggs", font_size=30).next_to(dozen_group, DOWN)
        
        # Formula introduction
        formula = MathTex(
            "\\text{moles}", "=", "\\frac{\\text{\\# Particles}}{6.022\\times10^{23}}"
        ).set_color_by_tex("moles", BLUE).set_color_by_tex("particles", GREEN).set_color_by_tex("6.022", RED)
        
        self.add_voice(
            'A mole is a counting unit, like a ten, or a century, or a dozen.',
            Create(dozen_group),
            Write(dozen_label),
            formula.animate.scale(0.8).to_corner(UR)
        )

        # Rest of original atom transformation remains
        atoms = VGroup(*[Circle(radius=0.125, color=BLUE, fill_opacity=1) for _ in range(16 * 9 * 4)])
        atoms.arrange_in_grid(rows=9*2, cols=16*2, buff=0.125)
        mole_label = Text("1 mole = 6.022 × 10²³ particles", font_size=30, color=RED)
        
        self.add_voice(
            """
            While a dozen means 12, a mole means 6.02 times 10 to the power of 23.
            ...
            That's a lot of atoms!
            """,
            ReplacementTransform(dozen_group, atoms),
            ReplacementTransform(dozen_label, mole_label),
            formula.animate.scale(0).to_edge(UP)
        )

        avogadro_title = Text("Avogadro's Number", font_size=36, color=ORANGE)
        avogadro_label = MathTex("6.02 \\times 10^{23}", color=RED)

        avogadro_group = VGroup(
            avogadro_title,
            avogadro_label
        ).arrange(DOWN)
        
        self.add_voice(
            """
            Since we often work with incredibly large numbers of particles in Chemistry,
            we use a number called AhvohGahdroh's Number: ... 6.02 times 10 to the power of 23.
            ... ... ...
            This constant represents the number of particles in one mole of anything.
            """,
            FadeIn(avogadro_title),
            ReplacementTransform(mole_label, avogadro_label)
        )

        self.play(FadeOut(atoms), FadeOut(avogadro_group))
        self.wait()

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
            balance.beam.animate.rotate(
                -20*DEGREES,
                about_point=balance.beam.get_center()
            ),
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
        element_group.move_to(table).next_to(table, LEFT).shift(RIGHT * 2)
        
        self.add_voice(
            "Here's where the periodic table becomes your best friend! Let's zoom in on sodium, or N A.",
            Create(element_group),
            Flash(element_text[1], color=GOLD, run_time=2),
            voice_factor=0.8
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
            AnimationGroup(
                element_group.animate.scale(2).move_to(ORIGIN),
                table.animate.scale(2),
                lag_ratio=0
            ),
            # element_text[1].animate.set_color(WHITE)
        )
        self.play(FadeOut(table), FadeOut(element_group))

class FlowchartInterlude(TTSScene):
    def construct(self):
        # Conversion flowchart
        mass = Text("Mass (g)", color=GREEN)
        moles = Text("Moles", color=BLUE)
        particles = Text("Particles", color=RED).scale(0.9)

        flowchart_elements = VGroup(mass, moles, particles)
        flowchart_elements.arrange(RIGHT, buff=2)

        arrows = VGroup(
            Arrow(mass.get_right(), moles.get_left(), buff=0.1),
            Arrow(moles.get_right(), particles.get_left(), buff=0.1),
            Arrow(particles.get_left(), moles.get_right(), buff=0.1),
            Arrow(moles.get_left(), mass.get_right(), buff=0.1)
        )
        arrows[0].shift(UP)
        arrows[1].shift(UP)
        arrows[2].shift(DOWN)
        arrows[3].shift(DOWN)
        
        labels = VGroup(
            MathTex("\\div\\text{Molar Mass}").next_to(arrows[0], UP),
            MathTex("\\times\\text{Avogadro}").next_to(arrows[1], UP),
            MathTex("\\div\\text{Avogadro}").next_to(arrows[2], DOWN),
            MathTex("\\times\\text{Molar Mass}").next_to(arrows[3], DOWN)
        )
       
        intro_title = Text("Ultimate Conversion Roadmap", font_size=40)

        self.add_voice(
            "Now that we've seen the pieces, let's put them all together into the Ultimate Conversion Roadmap.",
            FadeIn(intro_title)
        )

        self.add_voice(
            "The first point on our diagram is the mass, (in grams)",
            FadeOut(intro_title),
            FadeIn(mass, shift=UP)
        )

        self.wait(.5)

        self.add_voice(
            """
            The second point, is the mole.
            This is our central transportation hub.
            All conversions must go through the mole first.
            """,
            FadeIn(moles, shift=UP)
        )

        self.wait(.5)

        self.add_voice(
            "And our final stop, is the world of counting individual atoms and molecules.",
            FadeIn(particles, shift=UP)
        )

        self.add_voice(
            """
            See how moles are in the center?

            ... ... ...

            It's as if everything rotates around them!

            ... ... ...

            Moles are the central unit of Chemistry.
            Whenever you convert anything between any units, make sure to convert to moles first!
            Then convert to whatever unit you want after that.

            ... ... ...

            This will prevent you from making many mistakes.
            """,
            *[
                Rotate(
                    item,
                    angle=720 * DEGREES,
                    about_point=ORIGIN,
                    run_time=12,
                    rate_func=rate_functions.ease_in_quint
                )
                for item in (mass, particles) 
            ],
            voice_factor=0.6
        )


        self.add_voice(
            """
            When leaving the mole station ... multiply.
            When returning ... divide.
            ...
            When converting between grams and moles, multiply or divide by molecular mass.
            When converting between particles and moles, multiply or divide by AhvohGahdroh's Number.
            """,
            LaggedStart(
                LaggedStartMap(GrowArrow, arrows, lag_ratio=0),
                LaggedStartMap(Write, labels),
                lag_ratio=0.3
            )
        )
        self.play(*[FadeOut(o) for o in (mass, moles, particles, arrows, labels)])

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
        particle_container = Circle(radius=1.1, color=WHITE, fill_opacity=0)
        particles.move_to(particle_container) 

        self.add_voice(
            "Let's look at our first conversion example...",
            Create(particle_container),
            LaggedStartMap(FadeIn, particles),
            Write(example1_problem)
        )

        self.add_voice(
            "Here, we are converting Sodium particles to moles.",
            LaggedStartMap(FadeOut, particles),
            FadeOut(particle_container),
        )
        example1_solution.next_to(example1_problem, DOWN)
        self.add_voice(
            "Dividing our number of particles by AhvohGahdroh's Number, we get 2 Moles of Sodium.",
            Write(example1_solution)
        )

        # Example 2: Moles to Mass (Iron) with animation
        example2_problem = MathTex("\\text{Fe} = 3.50 \\text{ moles}")
        example2_solution = color_code_equation(MathTex(
            "\\text{Mass} &= 3.50 \\text{ mol} \\times \\frac{55.85\\text{ g}}{1\\text{ mol}}",
            "\\\\&= 195.48 \\text{ g Fe}"
        ))
        
        # Animation for moles (Fe)
        moles_blocks = VGroup(*[Square(side_length=0.15, color=GREEN, fill_opacity=0.5) for _ in range(35)])
        moles_blocks.arrange_in_grid(rows=5, cols=7, buff=0.1)
        moles_container = Rectangle(width=2.5, height=1.5, color=WHITE, fill_opacity=0)
        moles_blocks.move_to(moles_container)

        self.add_voice(
            """
            For our second example, we have 3.5 moles of iron.
            Iron has an atomic mass of 55.85 grams per mole.
            To find the mass in grams, we'll multiply the moles by the atomic mass.
            """,
            FadeOut(example1_problem, example1_solution),
            Create(moles_container),
            LaggedStartMap(FadeIn, moles_blocks),
            Write(example2_problem)
        )

        self.add_voice(
            "Multiplying 3.50 moles by 55.85 grams per mole, we get 195.48 grams of iron.",
            LaggedStartMap(FadeOut, moles_blocks),
            FadeOut(moles_container),
            Write(example2_solution)
        )

        # Example 3: Mass to Moles (Copper) with animation
        example3_problem = MathTex("\\text{Cu} = 127.0 \\text{ g}")
        example3_solution = color_code_equation(MathTex(
            "\\text{moles} &= 127.0 \\text{ g} \\times \\frac{1\\text{ mol}}{63.55\\text{ g}}",
            "\\\\&= 2.00 \\text{ mol Cu}"
        ))
        
        # Animation for mass (Cu)
        mass_icon = Rectangle(width=2, height=1, color=GOLD, fill_opacity=0.5)
        mass_label = Tex("127.0 g", color=WHITE).scale(0.5).move_to(mass_icon)
        mass_group = VGroup(mass_icon, mass_label)

        self.add_voice(
            """
            Our third example starts with 127 grams of copper.
            Copper's atomic mass is 63.55 grams per mole.
            To convert to moles, we'll divide the mass by the atomic mass.
            """,
            FadeOut(example2_problem, example2_solution),
            Create(mass_group),
            Write(example3_problem)
        )

        self.add_voice(
            "Dividing 127.0 grams by 63.55 grams per mole, we get exactly 2.00 moles of copper.",
            FadeOut(mass_group),
            Write(example3_solution)
        )

        # Example 4: Moles to Particles (Aluminum) with animation
        example4_problem = MathTex("\\text{Al} = 1.50 \\text{ moles}")
        example4_solution = color_code_equation(MathTex(
            "\\text{particles} &= 1.50 \\text{ mol} \\times 6.02 \\times 10^{23} \\frac{\\text{particles}}{\\text{mol}}",
            "\\\\&= 9.03 \\times 10^{23} \\text{ Al atoms}"
        ))
        
        # Animation for particles (Al)
        particles_al = VGroup(*[Dot(radius=0.03, color=BLUE) for _ in range(150)])
        particles_al.arrange_in_grid(rows=10, cols=15, buff=0.1)
        particle_container_al = Circle(radius=1.5, color=WHITE, fill_opacity=0)
        particles_al.move_to(particle_container_al)

        self.add_voice(
            """
            Finally, let's convert 1.50 moles of aluminum to atoms.
            To find the number of atoms, we'll multiply the moles by AhvohGahdroh's Number
            """,
            FadeOut(example3_problem, example3_solution),
            Create(particle_container_al),
            LaggedStartMap(FadeIn, particles_al),
            Write(example4_problem)
        )

        self.add_voice(
            "Multiplying 1.50 moles by 6.02 times 10 to the power of 23 particles per mole, we get 9.03 times 10 to the power of 23 aluminum atoms.",
            LaggedStartMap(FadeOut, particles_al),
            FadeOut(particle_container_al),
            Write(example4_solution)
        )

        self.add_voice(
            "Thank you for watching! I hope you learned something!",
            FadeOut(example4_solution)
        )
