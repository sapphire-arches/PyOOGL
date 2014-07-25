"""
Provides simple access to standard PC input devices (mouse and keyboard)

To use this module you must first call register_callbacks()

See register_callbacks() for what glut callbacks are registered

"""
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc, glutSpecialFunc, glutSpecialUpFunc, glutMotionFunc, glutPassiveMotionFunc, glutMouseFunc
_keystates = {}
_specials = {}
_mouse_pos = (0, 0)
_button_states = {}

#internal functions

def _key_down(key, x, y):
    _keystates[key[0]] = True

def _key_up(key, x, y):
    _keystates[key[0]] = False

def _special_down(key, x, y):
    _specials[key] = True

def _special_up(key, x, y):
    _specials[key] = False

def _mouse_pos_listener(x, y):
    global _mouse_pos
    _mouse_pos = (x, y)

def _mouse_button_listener(button, state, x, y):
    if state == 0:
        _button_states[button] = True
    else:
        _button_states[button] = False
    _mouse_pos = (x, y)

# public interface

def register_callbacks():
    """
    Registers the following callbacks with GLUT:
        - glutKeyboardFunc
        - glutKeyboardUpFunc

        - glutSpecialFunc
        - glutSpecialUpFunc

        - glutMotionFunc
        - glutPassiveMotionFunc

        - glutMouseFunc
    """
    glutKeyboardFunc(_key_down)
    glutKeyboardUpFunc(_key_up)

    glutSpecialFunc(_special_down)
    glutSpecialUpFunc(_special_up)

    glutMotionFunc(_mouse_pos_listener)
    glutPassiveMotionFunc(_mouse_pos_listener)

    glutMouseFunc(_mouse_button_listener)

def is_key_pressed(key):
    """ returns a boolean representing if a key is pressed """
    val = bytes(key, 'ascii')[0]
    if val not in _keystates:
        return False
    return _keystates[val]

def is_mouse_button_pressed(button):
    """
    returns a boolean representing if a mouse button is pressed

    0 = lmb, 1 = mmb, 2 = rmb
    """
    if button not in _button_states:
        return False
    return  _button_states[button]

def get_mouse_x():
    return _mouse_pos[0]

def get_mouse_y():
    return _mouse_pos[1]

def get_mouse_pos():
    """ returns a tuple of the form (mouse_x, mouse_y). may be more convienint than the individual get_mouse_* calls, but returns the same data """
    return _mouse_pos

# 100 = left        / numpad 4
# 101 = up          / numpad 8
# 102 = right       / numpad 6
# 103 = down        / numpad 2
# 104 = pageup      / numpad 9
# 105 = pagedown    / numpad 3
# 106 = home        / numpad 7
# 107 = end         / numpad 1
# 108 = insert
# 109 = numlock
# 110
# 111
# 112 = shift
# 113
# 114 = control
# 115
# 116 = alt
# 117
# 118
# 119
# 120
# 121

def is_special_pressed(key):
    """
    Gets the state of special keys - arrow keys are the primary keys of interest

    100 = left
    101 = up
    102 = right
    103 = down
    """
    if key not in _specials:
        return False
    return _specials[key]
