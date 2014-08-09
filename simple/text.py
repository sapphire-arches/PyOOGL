from OpenGL.GLUT import  glutBitmapString,\
                         GLUT_BITMAP_8_BY_13,\
                         GLUT_BITMAP_9_BY_15,\
                         GLUT_BITMAP_TIMES_ROMAN_10,\
                         GLUT_BITMAP_TIMES_ROMAN_24,\
                         GLUT_BITMAP_HELVETICA_10,\
                         GLUT_BITMAP_HELVETICA_12,\
                         GLUT_BITMAP_HELVETICA_18
                         
from OpenGL.GL   import glRasterPos, glColor3f

def draw_text(text, x, y, color, font = GLUT_BITMAP_HELVETICA_18, enc = 'ascii'):
    glRasterPos(x, y)
    glColor3f(color[0], color[1], color[2])
    glutBitmapString(font, text.encode(enc))

# Maybe have a way to resize text?
# Dunno how hard that would be.

bitmap_font = {"8x13" : GLUT_BITMAP_8_BY_13,
         "9x15" : GLUT_BITMAP_9_BY_15,
         "tnr": GLUT_BITMAP_TIMES_ROMAN_10,
         "tnr10": GLUT_BITMAP_TIMES_ROMAN_10,
         "tnr24": GLUT_BITMAP_TIMES_ROMAN_24,
         "helvetica": GLUT_BITMAP_HELVETICA_12,
         "helvetica10": GLUT_BITMAP_HELVETICA_10,
         "helvetica12": GLUT_BITMAP_HELVETICA_12,
         "helvetica18": GLUT_BITMAP_HELVETICA_18,
    }
