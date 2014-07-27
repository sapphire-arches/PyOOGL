Resize
======

The ``resize`` module provides various sane default functions to pass to the `resize_func` of the :class:`PyOOGL.windowmanagement.Window` class constructor.

.. py:module:: PyOOGL.simple.resize

.. py:function:: sdl_resize()

    Returns a function that emulates SDL's resize behavior (one unit per pixel, (0,0) in the top left corner)
