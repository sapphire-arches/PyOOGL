Window Management
=================

The ``windowmanagement`` module provides utilities for getting an OpenGL context.
This is necessary for all the :mod:`PyOOGL.simple` modules.

.. py:module:: PyOOGL.windowmanagement

.. py:class:: Window(winname, size=(800, 600), display_func=None, resize_func=None)

    The Window class represents a window.

    .. py:method:: clear()

        Clears the screen. Uses ``glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT``

    .. py:method:: get_height()

        Get the current height of the window in pixels

    .. py:method:: get_height()

        Get the current height of the window in pixels
