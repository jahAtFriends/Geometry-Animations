from manim import *
import math

class ExteriorAngles(Scene):

    def angleBetween(u, v):
        dotProd = u[0] * v[0] + u[1] * v[1]
        magU = math.sqrt(u[0]**2 + u[1]**2)
        magV = math.sqrt(v[0]**2 + v[1]**2)
        cosine = dotProd / (magU + magV)
        theta  = math.acos(cosine)
        return theta
        
    def construct(self):
        self.next_section("Drawing the Pentagon")
        position_list = [
            [2, -2.5, 0],  # bottom right
            [-2, -2.5, 0],  # bottom left
            [-4, 0, 0],  # upper left
            [0, 3, 0],  # top
            [3, 2, 0],  # upper right
        ]
        vectors = [
            [position_list[0][0] - position_list[1][0], position_list[0][1] - position_list[1][1], 0],
            [position_list[4][0] - position_list[0][0], position_list[4][1] - position_list[0][1], 0],
            [position_list[3][0] - position_list[4][0], position_list[3][1] - position_list[4][1], 0],
            [position_list[2][0] - position_list[3][0], position_list[2][1] - position_list[3][1], 0],
            [position_list[1][0] - position_list[2][0], position_list[1][1] - position_list[2][1], 0]]
            
        penta = Polygon(*position_list, color=RED)
        self.play(Create(penta))
        self.wait(0.1)
        
        self.next_section("Drawing the little man")
        circle = Circle(radius=0.2, color = YELLOW, fill_opacity=1.0)
        circx = position_list[1][0]
        circy = position_list[1][1]
        circle.shift(circx*RIGHT,circy*UP)
        heading = Arrow(start = LEFT, end=RIGHT, color=BLUE)
        heading.shift((circx+0.7)*RIGHT,circy*UP)
        tinyDude = Group(circle,heading)
        self.play(FadeIn(tinyDude))
        self.wait(0.1)
        
        self.next_section("Slide the dude")
        oldDudes = []
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[0])
        
        shiftx = position_list[0][0] - position_list[1][0]
        shifty = position_list[0][1] - position_list[1][1]
        self.play(tinyDude.animate.shift(shiftx*RIGHT,shifty*UP))
        self.wait(0.1)
        
        self.next_section("rotate and slide the dude")
        dx = position_list[4][0] - position_list[0][0]
        dy = position_list[4][1] - position_list[0][1]
        m = dy/dx
        theta = math.atan(m)
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[1])
        self.play(Rotate(tinyDude, theta, about_point=position_list[0]))
        self.play(tinyDude.animate.shift(dx*RIGHT,dy*UP))
        self.wait(0.1)
        
        self.next_section("rotate and slide the dude again")
        dx = vectors[2][0]
        dy = vectors[2][1]
        u = vectors[1]
        v = vectors[2]
        dotProd = u[0] * v[0] + u[1] * v[1]
        magU = math.sqrt(u[0]**2 + u[1]**2)
        magV = math.sqrt(v[0]**2 + v[1]**2)
        cosine = dotProd / (magU * magV)
        theta  = math.acos(cosine)
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[2])
        self.play(Rotate(tinyDude, theta, about_point=position_list[4]))
        self.play(tinyDude.animate.shift(dx*RIGHT,dy*UP))
        self.wait(0.1)
        
        self.next_section("rotate and slide the dude again")
        dx = vectors[3][0]
        dy = vectors[3][1]
        u = vectors[2]
        v = vectors[3]
        dotProd = u[0] * v[0] + u[1] * v[1]
        magU = math.sqrt(u[0]**2 + u[1]**2)
        magV = math.sqrt(v[0]**2 + v[1]**2)
        cosine = dotProd / (magU * magV)
        theta  = math.acos(cosine)
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[3])
        self.play(Rotate(tinyDude, theta, about_point=position_list[3]))
        self.play(tinyDude.animate.shift(dx*RIGHT,dy*UP))
        self.wait(0.1)
        
        self.next_section("rotate and slide the dude again")
        dx = vectors[4][0]
        dy = vectors[4][1]
        u = vectors[3]
        v = vectors[4]
        dotProd = u[0] * v[0] + u[1] * v[1]
        magU = math.sqrt(u[0]**2 + u[1]**2)
        magV = math.sqrt(v[0]**2 + v[1]**2)
        cosine = dotProd / (magU * magV)
        theta  = math.acos(cosine)
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[4])
        self.play(Rotate(tinyDude, theta, about_point=position_list[2]))
        self.play(tinyDude.animate.shift(dx*RIGHT,dy*UP))
        self.wait(0.1)
        
        self.next_section("rotate dude")
        u = vectors[4]
        v = vectors[0]
        dotProd = u[0] * v[0] + u[1] * v[1]
        magU = math.sqrt(u[0]**2 + u[1]**2)
        magV = math.sqrt(v[0]**2 + v[1]**2)
        cosine = dotProd / (magU * magV)
        theta  = math.acos(cosine)
        oldCirc = circle.copy()
        oldCirc.set_opacity(0.25)
        oldHeading = heading.copy()
        oldHeading.set_opacity(0.25)
        oldDudes.append(Group(oldCirc,oldHeading))
        self.add(oldDudes[5])
        self.play(Rotate(tinyDude, theta, about_point=position_list[1]))
        self.wait(0.1)
        
        self.next_section("Extend sides")
        ###Extend the sidelengths and show angles
        unit_vects = []
        for x in vectors:
            mag = math.sqrt(x[0]**2+x[1]**2)
            unit_vect = [x[0]/mag, x[1]/mag,0]
            unit_vects.append(unit_vect)
            
        ext_factor = 3
        endPoints = [
            [position_list[0][0] + ext_factor * unit_vects[0][0], position_list[0][1] + ext_factor * unit_vects[0][1],0],
            [position_list[4][0] + ext_factor * unit_vects[1][0], position_list[4][1] + ext_factor * unit_vects[1][1],0],
            [position_list[3][0] + ext_factor * unit_vects[2][0], position_list[3][1] + ext_factor * unit_vects[2][1],0],
            [position_list[2][0] + ext_factor * unit_vects[3][0], position_list[2][1] + ext_factor * unit_vects[3][1],0],
            [position_list[1][0] + ext_factor * unit_vects[4][0], position_list[1][1] + ext_factor * unit_vects[4][1],0]]

        dlines = []
        guide_lines = []
        
        dline = DashedLine(position_list[0],endPoints[0], color = RED)
        gline = Line(position_list[1],endPoints[0])
        guide_lines.append(gline)
        dlines.append(dline)
        
        dline = DashedLine(position_list[4], endPoints[1], color = RED)
        gline = Line(position_list[0],endPoints[1])
        guide_lines.append(gline)
        dlines.append(dline)
        dline = DashedLine(position_list[3], endPoints[2], color = RED)
        gline = Line(position_list[4],endPoints[2])
        guide_lines.append(gline)
        dlines.append(dline)
        dline = DashedLine(position_list[2], endPoints[3], color = RED)
        gline = Line(position_list[3],endPoints[3])
        guide_lines.append(gline)
        dlines.append(dline)
        dline = DashedLine(position_list[1], endPoints[4], color = RED)
        gline = Line(position_list[2],endPoints[4])
        guide_lines.append(gline)
        dlines.append(dline)
        
        angles = VGroup()
        
        angle = Angle(guide_lines[0],guide_lines[1], radius = 0.6)
        angles.add(angle)
        
        angle = Angle(guide_lines[1],guide_lines[2], radius = 0.6)
        angles.add(angle)
        
        angle = Angle(guide_lines[2],guide_lines[3], radius = 0.6)
        angles.add(angle)
        
        angle = Angle(guide_lines[3],guide_lines[4], radius = 0.6)
        angles.add(angle)
        
        angle = Angle(guide_lines[4],guide_lines[0], radius = 0.6)
        angles.add(angle)
        
        self.play(Create(dlines[0]), Create(dlines[1]), Create(dlines[2]), Create(dlines[3]), Create(dlines[4]))
        self.play(Create(angles))
        
        self.play(FadeOut(tinyDude), FadeOut(oldDudes[0]), FadeOut(oldDudes[1]), FadeOut(oldDudes[2]), FadeOut(oldDudes[3]), FadeOut(oldDudes[4]), FadeOut(oldDudes[5]))
        
        self.wait(0.1)
        
    
        