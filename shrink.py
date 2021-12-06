##############
#
# Exterior Angles Demonstration on Arbitrary Polygon
# 
# (c) 2021 Joel Hammer
# Friends School of Baltimore
#
# This janky code is governed by the GNU GPL 3.0 License
# https://www.gnu.org/licenses/gpl-3.0.en.html
#
#
#############

from manim import *
import math

class shrink(Scene):
    def construct(self):
        self.next_section("Draw the Polygon")
        vertices = [
            [-2, -2.5, 0],  # bottom left
            [2, -2.5, 0],  # bottom right
            [3, 2, 0],  # upper right
            [0, 3, 0],  # top
            [-4, 0, 0],  # upper left
        ] ##Should still work if you add or change vertices (obviously there have to be at least three)
        
        print(vertices)
        
        poly = VGroup() ##Group of lines connecting the points edges of the polygon.
        
        ##Construct the Polygon
        current_vertex = vertices[len(vertices)-1]
        for x in vertices:
            line = Line(current_vertex, x, color = RED)
            poly.add(line)
            current_vertex = x
            
        self.play(Create(poly))
        
        self.wait(1)
        
        self.next_section("Draw the exterior angles")
        side_unit_vectors = []
        
        ##determine the unit vectors in the direction of each side
        current_vertex = vertices[0]
        for k in range(1, len(vertices) + 1):
            i = k % len(vertices)
            v = [vertices[i][0] - current_vertex[0], vertices[i][1] - current_vertex[1], vertices[i][2] - current_vertex[2]]
            mag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
            v = [v[0]/mag, v[1]/mag, v[2]/mag]
            side_unit_vectors.append(v)
            current_vertex = vertices[i]
            
        side_extensions_list = []
        side_extensions = VGroup()
        ext_animations = []
        ext_length = 3
        guide_lines = []
        
        ##Build side extensions and guidelines for angles
        for i in range(len(vertices)):
            k = (i + 1) % len(vertices)
            print(i)
            start = vertices[i]
            x = vertices[k]
            y = side_unit_vectors[i]
            end = [x[0] + ext_length * y[0], x[1] + ext_length * y[1], x[2] + ext_length * y[2]]
            guide_lines.append(Line(start, end))
            line = DashedLine(x,end,color = RED)
            side_extensions_list.append(line)
            side_extensions.add(line)
            ext_animations.append(Create(line))
        
        ##Draw all the side extensions simultaneously
        self.play(*ext_animations)
        
        angle_list = []
        angle_group = VGroup()
        for i in range(len(vertices)):
            k = (i + 1) % len(vertices)
            x = guide_lines[i]
            y = guide_lines[k]
            angle = Angle(x,y,radius = 0.6)
            angle_list.append(angle)
            angle_group.add(angle)
        
        self.play(Create(angle_group))
        
        self.wait(0.1)
        
        ##Shrink the polygon and move the extensions and angles, but don't shrink them
        self.next_section("shrink the whole business down")
        shrink_point = [0,0,0]
        dilation_factor = 0.00000001
        shrink_vertices = []
        
        for x in vertices:
            v = [(x[0] - shrink_point[0]) * dilation_factor,
                (x[1] - shrink_point[1]) * dilation_factor, 
                (x[2] - shrink_point[2]) * dilation_factor]
            shrink_vertices.append([shrink_point[0] + v[0], shrink_point[1] + v[1], shrink_point[2] + v[2]])
            
        shrink_poly = VGroup()
        current_vertex = shrink_vertices[len(vertices)-1]
        for x in shrink_vertices:
            line = Line(current_vertex, x, color = RED)
            shrink_poly.add(line)
            current_vertex = x
           
        
        vertices = shrink_vertices
        
        shrink_side_extensions_list = []
        shrink_side_extensions = VGroup()
        guide_lines = []
        
        ##Build side extensions and guidelines for angles
        for i in range(len(vertices)):
            k = (i + 1) % len(vertices)
            print(i)
            start = vertices[i]
            x = vertices[k]
            y = side_unit_vectors[i]
            end = [x[0] + ext_length * y[0], x[1] + ext_length * y[1], x[2] + ext_length * y[2]]
            guide_lines.append(Line(start, end))
            line = DashedLine(x,end,color = RED)
            shrink_side_extensions_list.append(line)
            shrink_side_extensions.add(line)

            
        shrink_angle_list = []
        shrink_angle_group = VGroup()
        for i in range(len(vertices)):
            k = (i + 1) % len(vertices)
            x = guide_lines[i]
            y = guide_lines[k]
            angle = Angle(x,y,radius = 0.6)
            shrink_angle_list.append(angle)
            shrink_angle_group.add(angle)
            
        self.play(Transform(poly, shrink_poly), Transform(angle_group,shrink_angle_group), Transform(side_extensions,shrink_side_extensions))
        
        self.wait(0.1)
        
        
        
                
            
            