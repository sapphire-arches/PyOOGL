from OpenGL.GL import glBegin, glEnd, glVertex2f, glColor3f, glGetError
from OpenGL.GL import GL_QUADS, GL_TRIANGLE_FAN
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
