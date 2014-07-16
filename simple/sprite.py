from PIL import Image
from OpenGL.GL import *
from math import ceil, log

class Sprite:
    def __init__(self, filename):
        imported_img = Image.open(filename)
        self.x_two = pow(2, ceil(log(imported_img.size[0]) / log(2)))
        self.y_two = pow(2, ceil(log(imported_img.size[1]) / log(2)))
        self.img = imported_img
        padded = Image.new("RGBA", (self.x_two, self.y_two))
        padded.paste(self.img, (0, 0))
        padded = padded.transpose(Image.FLIP_TOP_BOTTOM)

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.x_two, self.y_two, 0, GL_RGBA, GL_UNSIGNED_BYTE, padded.tostring("raw", "RGBA", 0, -1))
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    def get_width(self):
        return self.img.size[0]

    def get_height(self):
        return self.img.size[1]

    def render(self, x, y, w, h):
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glBindTexture(GL_TEXTURE_2D, self.texture)

        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex2f(x, y)

        glTexCoord2f(self.img.size[0] / self.x_two, 0)
        glVertex2f(x + w, y)

        glTexCoord2f(self.img.size[0] / self.x_two, self.img.size[1] / self.y_two)
        glVertex2f(x + w, y + h)

        glTexCoord2f(0, self.img.size[1] / self.y_two)
        glVertex2f(x, y + h)

        glEnd()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)
