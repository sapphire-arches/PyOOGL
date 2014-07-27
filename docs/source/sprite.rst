Sprite
======

.. py:module:: PyOOGL.simple.sprite

The ``sprite`` module provides utilities for displaying sprites.

.. py:class:: PyOOGL.simple.sprite.Sprite(filename)

   The Sprite class represents an OpenGL texture with sprite data loaded from the file specified by ``filename``

   .. py:method:: render(x, y, w, h)

      Requests the sprite render.

      :param x float: X position to render at
      :param y float: Y position to render at
      :param w float: width to render with
      :param h float: height to render with

   .. py:method:: get_width()

      Get the width in pixels of this sprite

   .. py:method:: get_height()

      Get the height in pixels of this sprite
