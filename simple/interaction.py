from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc, glutSpecialFunc, glutSpecialUpFunc, glutMotionFunc, glutPassiveMotionFunc
_keystates = {}
_specials = {}
_mouse_pos = (0, 0)
_button_states = {}

def _key_down(key, x, y):
    _keystates[key[0]] = True

def _key_up(key, x, y):
    _keystates[key[0]] = False

def _special_down(key, x, y):
    _specials[key] = True

def _special_up(key, x, y):
    _specials[key] = False

def _mouse_pos_listener(x, y):
    _mouse_pos = (x, y)

def _mouse_button_listener(button, state, x, y):
    if state == 0:
        _button_states[button] = False
    else:
        _button_states[button] = True
    _mouse_pos = (x, y)

def register_callbacks():
    glutKeyboardFunc(_key_down)
    glutKeyboardUpFunc(_key_up)

    glutSpecialFunc(_special_down)
    glutSpecialUpFunc(_special_up)

    glutMotionFunc(_mouse_pos_listener)
    glutPassiveMotionFunc(_mouse_pos_listener)

def is_key_pressed(key):
    val = bytes(key, 'ascii')[0]
    if val not in _keystates:
        return False
    return _keystates[val]

def is_mouse_button_pressed(button):
    if button not in _button_states:
        return False
    return  _button_states[button]

def get_mouse_x():
    return _mouse_pos[0]

def get_mouse_y():
    return _mouse_pos[1]

def get_mouse_pos():
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
    if key not in _specials:
        return False
    return _specials[key]
