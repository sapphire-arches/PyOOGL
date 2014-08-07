from OpenGL.GLUT import *
from OpenGL.GL   import *

def draw_text(text, x, y, color):
    glRasterPos(x, y)
    glColor3f(color[0], color[1], color[2])
    glutBitmapString(GLUT_BITMAP_HELVETICA_18, text.encode('ascii'))
