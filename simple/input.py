from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc, glutSpecialFunc, glutSpecialUpFunc
_keystates = {}
_specials = {}

def _key_down(key, x, y):
    _keystates[key[0]] = True

def _key_up(key, x, y):
    _keystates[key[0]] = False

def _special_down(key, x, y):
    _specials[key] = True

def _special_up(key, x, y):
    _specials[key] = False

def register_callbacks():
    glutKeyboardFunc(_key_down)
    glutKeyboardUpFunc(_key_up)

    glutSpecialFunc(_special_down)
    glutSpecialUpFunc(_special_up)

def is_key_pressed(key):
    val = bytes(key)[0]
    if val not in _keystates:
        return False
    return _keystatese[val]

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
