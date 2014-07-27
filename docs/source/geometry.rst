Geometry
========

The ``geometry`` module provides utilities for rendering solid color geometrical objects.
All the functions in this module use the deprecated OpenGL1.1 immediate mode.

.. py:module:: PyOOGL.simple.geometry

.. py:function:: draw_circle(x, y, radius, color, verts=32)

    Renders a circle

    :param x float: The x coordinate to draw the circle at
    :param y float: The y coordinate to draw the circle at
    :param radius float: the radius of the circle
    :param color iterable: a 3 element iterable describing the r,g,b color of the circle using 0-1 float notation
    :param verts integer: Number of points to use when rendering the circle.

.. py:function:: draw_rectangle(x, y, w, h, color)

    Renders a rectangle

    :param x float: The x coordinate to draw the rectangle at
    :param y float: The y coordinate to draw the rectangle at
    :param w float: The width of the rectangle
    :param h float: The height of the rectangle
    :param color iterable: a 3 element iterable describing the r,g,b color of the circle using 0-1 float notation

.. py:function draw_line(x1, y1, x2, y2, color)

    Renders a line

    :param x1 float: The x coordinate to start the line at
    :param y1 float: The y coordinate to start the line at
    :param x1 float: The x coordinate to end the line at
    :param y1 float: The y coordinate to end the line at
    :param color iterable: a 3 element iterable describing the r,g,b color of the circle using 0-1 float notation
