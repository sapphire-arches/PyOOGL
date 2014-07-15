from OpenGL.GL import glLoadIdentity, glScalef, glTranslatef
# approximate SDL resize behavior (1:1 units to pixels + top left is 0, 0)
def sdl_resize():
    def resize(w, h):
        glLoadIdentity()
        glTranslatef(-1 , 1, 0)
        glScalef(2 / w, -2 / h, 1)
        pass
    return resize
