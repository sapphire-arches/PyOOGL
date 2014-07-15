from OpenGL.GL import *
from math import pi, cos, sin

def draw_circle(x, y, radius, color, verts=32):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(color[0], color[1], color[2])

    angle = 0
    glVertex2f(x, y)
    while angle < 2 * pi:
        glVertex2f(x + radius * cos(angle), y + radius * sin(angle))
        angle += 2 * pi / verts
    glVertex2f(x + radius, y)
    glEnd()

def draw_rectangle(x, y, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_line(x1, y1, x2, y2, color):
    glBegin(GL_LINE)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
