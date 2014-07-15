from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, glutCreateWindow
from OpenGL.GLUT import GLUT_DOUBLE, GLUT_RGB, GLUT_DEPTH
from OpenGL.GLUT import glutDisplayFunc, glutReshapeFunc, glutIdleFunc
from OpenGL.GLUT import glutMainLoop
from OpenGL.GLUT import glutSwapBuffers
from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT
from time import time, sleep
from sys import argv

class Window:
    def __init__(self, winname, size=(800, 600), display_func=None, resize_func=None):
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(size[0], size[1])
        self._win_id = glutCreateWindow(winname.encode('ascii'))
        self.display_func = display_func
        self.resize_func = resize_func
        self.width = size[0]
        self.height = size[1]

        if display_func is not None:
            display_func = _display_wrapper(display_func)
            glutDisplayFunc(display_func)
            glutIdleFunc(display_func)

        if resize_func is not None:
            resize_func = _resize_wrapper(self, resize_func)
            glutReshapeFunc(resize_func)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT)

def main_loop():
    glutMainLoop()

_lastTime = 0
def _display_wrapper(display):
    def disp():
        global _lastTime
        display()
        tick = time()
        required_delta = (1/60) - (tick - _lastTime)
        if (required_delta > 0):
            sleep(required_delta)
        _lastTime = tick
        glutSwapBuffers()
    return disp

def _resize_wrapper(window, func):
    def resize(w, h):
        window.width = w
        window.height = h
        func(w, h)
    return resize
