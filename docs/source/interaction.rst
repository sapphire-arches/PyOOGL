Interaction
===========

The ``interaction`` module provides a query-based interface to the standard input devices (mouse and keyboard)

.. py:module:: PyOOGL.simple.interaction

.. py:function:: register_callbacks()

    Register GLUT callbacks to initialize the interaction module.
    Registers the following GLUT callbacks:

    * ``glutKeyboardFunc``
    * ``glutKeyboardUpFunc``
    * ``glutSpecialFunc``
    * ``glutSpecialUpFunc``
    * ``glutMotionFunc``
    * ``glutPassiveMotionFunc``
    * ``glutMouseFunc``

.. py:function:: is_key_pressed(key)

    Queries if a key is pressed. Note that this function cannot be queried for special keys.
    For such keys you must use :func:`is_special_pressed`.

    :param key string: Single character string representing which key we care about

.. py:function:: is_mouse_button_pressed(button)

    Queries if a mouse button is pressed. The ``button`` argument is an integer corresponding to the values in the
    following table.

    ====== ===================
    Button Description
    ====== ===================
    0      Left mouse button
    1      Middle mouse button
    2      Right mouse button
    ====== ===================

.. py:function:: get_mouse_x()

    Get the x position of the mouse in pixels relative to the top left of the window.

.. py:function:: get_mouse_y()

    Get the y position of the mouse in pixels relative to the top left of the window.

.. py:function:: get_mouse_pos()

    Get the mouse position in pixels relative too the top left of the window as a two element tuple of the form (x, y)

.. py:function:: is_special_pressed(key)

    Queries if a special key is pressed. The key argument must be from the Key column of the following table:

    ======== ====================
    Key      Description
    ======== ====================
    100      Left arrow
    101      Up arrow
    102      Right arrow
    103      Down arrow
    112      Shift
    114      Control
    116      Alt (Command on OSX)
    ======== ====================
