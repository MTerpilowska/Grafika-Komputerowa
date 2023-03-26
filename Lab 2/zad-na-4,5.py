#!/usr/bin/env python3
import sys
import random
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

seedvalue = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(1.0, 1.0, 1.0, 1.0)


def shutdown():
    pass

def drawrectangle(x, y, a, b):

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glVertex2f(x + a, y + b)
    glEnd()

def drawcarpet(x, y, a, b, level):  
    if(level == 0):
        drawrectangle(x, y, a, b)
    else:
        level = level-1
        newa = a/3
        newb = b/3
        for i in range(3):
            for j in range(3):
                if(i!=1 or j!=1):
                    newy = y - newb + j*newb
                    newx = x - newa + i*newa
                    drawcarpet(newx, newy, newa, newb, level)


def render(time, level):

    glClear(GL_COLOR_BUFFER_BIT)

    random.seed(seedvalue)
    red = random.random()     
    green = random.random()
    blue = random.random()
    glColor3f(red, green, blue)

    drawcarpet(0, 0, 156, 146, level)
    glFlush() 


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    level = int(input('Podaj poziom samopodobienstwa: '))    

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), level)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()