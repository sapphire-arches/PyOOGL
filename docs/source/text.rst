Text
=====

The ``text`` module provides utilities for rendering text, utilizing the bitmap fonts built in to freeglut.

.. py:module:: PyOOGL.simple.text

.. py:function:: draw_text(text, x, y, color, font=GLUT_BITMAP_HELVETICA_18, enc='ascii')

    Renders a string of text

    :param text string: The text to display
    :param x float: The x coordinate to draw the text at (bottom left corner of first character)
    :param y float: The y coordinate to draw the text at (bottom left corner of first character)
    :param color iterable: a 3 element iterable describing the r,g,b color of the circle using 0-1 float notation
    :param font ctypes.c_void_p: An object font with which to draw the text. Only a certain few fonts may be used. Mostly relevant detailed description of these font objects is `here <http://openglut.sourceforge.net/group__bitmapfont.html>`_. To retreive these font objects without impoting from OpenGL, utilize the ''bitmap_font'' dictionary contained within this module, which maps the font objects to strings as demonstrated by the following table:

        ============= ==========================
        Key           Value                      
        ============= ========================== 
        "8x13"        GLUT_BITMAP_8_BY_13
        "9x15"        GLUT_BITMAP_9_BY_15
        "tnr10"       GLUT_BITMAP_TIMES_ROMAN_10
        "tnr24"       GLUT_BITMAP_TIMES_ROMAN_24
        "helvetica10" GLUT_BITMAP_HELVETICA_10
        "helvetica12" GLUT_BITMAP_HELVETICA_12
        "helvetica18" GLUT_BITMAP_HELVETICA_18
        ============= ==========================
    
    :param enc string: A string representation of the encoding to use. Valid arguments are those which are also valid for `this built-in Python function <https://docs.python.org/3.4/library/stdtypes.html#str.encode>`_.

