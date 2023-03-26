#!/usr/bin/env python3
import sys
import random
from tkinter import Y
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

seedvalue = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def drawrectangle(x, y, a, b):

    #uznajemy x,y za wierzcholek prostokata
    glClear(GL_COLOR_BUFFER_BIT)

    random.seed(seedvalue)
    
    red = random.random()
    green = random.random()
    blue = random.random()

    glColor3f(red, green, blue)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-(b/2), y+(a/2))
    glVertex2f(x-(b/2), y-(a/2))
    glVertex2f(x+(b/2), y+(a/2))
    glEnd()

    glColor3f(red, green, blue)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-(b/2), y-(a/2))
    glVertex2f(x+(b/2), y+(a/2))
    glVertex2f(x+(b/2), y-(a/2))
    glEnd()
    glFlush()    


def render(time, x, y, a, b):
    drawrectangle(x, y, a, b)


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

    x = float(input('x: '))
    y = float(input('y: '))
    a = float(input('a: '))
    b = float(input('b: '))
    d = float(input('d: '))
    a = a*d
    b = b*d 

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), x, y, a, b)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()