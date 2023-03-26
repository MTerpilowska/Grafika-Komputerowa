#!/usr/bin/env python3
import sys
import numpy as np
import random
from glfw.GLFW import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *

seedvalue = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

n = 50
matrix = np.zeros((n, n, 3))
colors = np.zeros((n, n, 3))

def makeMatrix(matrix, colors):
    random.seed(seedvalue)
    for i in range(0, n):
        for j in range(0, n):
            u = i / n
            v = j / n
            # x
            matrix[i][j][0] = (-90*pow(u, 5) + 225*pow(u, 4) - 270*pow(u, 3) + 180*pow(u, 2) - 45*u)*cos(pi*v)
            colors[i][j][0] = random.random()
            # y
            matrix[i][j][1] = 160*pow(u, 4) - 320*pow(u, 3) + 160*pow(u, 2)
            colors[i][j][1] = random.random()
            # z
            matrix[i][j][2] = (-90*pow(u, 5) + 225*pow(u, 4) - 270*pow(u, 3) + 180*pow(u, 2) - 45*u)*sin(pi*v)
            colors[i][j][2] = random.random()
        


def drawEgg():
    for i in range (0, n):
        for j in range (0, n):
            glBegin(GL_TRIANGLE_STRIP)

            if(i == n-1 and j == n-1):
                glColor3f(colors[i][j][0], colors[i][j][1], colors[i][j][2])
                glVertex3f(matrix[i][j][0], matrix[i][j][1] - 5, matrix[i][j][2])

                glColor3f(colors[0][j][0], colors[0][j][1], colors[0][j][2])
                glVertex3f(matrix[0][j][0], matrix[0][j][1] - 5, matrix[0][j][2])

                glColor3f(colors[i][0][0], colors[i][0][1],  colors[i][0][2])
                glVertex3f(matrix[i][0][0], matrix[i][0][1] - 5,  matrix[i][0][2])

                glColor3f(colors[0][0][0], colors[0][0][1], colors[0][0][2])
                glVertex3f(matrix[0][0][0], matrix[0][0][1] - 5, matrix[0][0][2])
                glEnd()
            else:
                if(i == n-1):
                    glColor3f(colors[i][j][0], colors[i][j][1], colors[i][j][2])
                    glVertex3f(matrix[i][j][0], matrix[i][j][1] - 5, matrix[i][j][2])

                    glColor3f(colors[0][j][0], colors[0][j][1], colors[0][j][2])
                    glVertex3f(matrix[0][j][0], matrix[0][j][1] - 5, matrix[0][j][2])

                    glColor3f(colors[i][j+1][0], colors[i][j+1][1],  colors[i][j+1][2])
                    glVertex3f(matrix[i][j+1][0], matrix[i][j+1][1] - 5,  matrix[i][j+1][2])

                    glColor3f(colors[0][j + 1][0], colors[0][j + 1][1], colors[0][j + 1][2])
                    glVertex3f(matrix[0][j + 1][0], matrix[0][j + 1][1] - 5, matrix[0][j + 1][2])
                    glEnd()
                else:
                    if(j == n-1):
                        glColor3f(colors[i][j][0], colors[i][j][1], colors[i][j][2])
                        glVertex3f(matrix[i][j][0], matrix[i][j][1] - 5, matrix[i][j][2])

                        glColor3f(colors[i + 1][j][0], colors[i + 1][j][1], colors[i + 1][j][2])
                        glVertex3f(matrix[i + 1][j][0], matrix[i + 1][j][1] - 5, matrix[i + 1][j][2])

                        glColor3f(colors[i][0][0], colors[i][0][1],  colors[i][0][2])
                        glVertex3f(matrix[i][0][0], matrix[i][0][1] - 5,  matrix[i][0][2])

                        glColor3f(colors[i + 1][0][0], colors[i + 1][0][1], colors[i + 1][0][2])
                        glVertex3f(matrix[i + 1][0][0], matrix[i + 1][0][1] - 5, matrix[i + 1][0][2])
                        glEnd()
                    else:
                        glColor3f(colors[i][j][0], colors[i][j][1], colors[i][j][2])
                        glVertex3f(matrix[i][j][0], matrix[i][j][1] - 5, matrix[i][j][2])

                        glColor3f(colors[i + 1][j][0], colors[i + 1][j][1], colors[i + 1][j][2])
                        glVertex3f(matrix[i + 1][j][0], matrix[i + 1][j][1] - 5, matrix[i + 1][j][2])

                        glColor3f(colors[i][j+1][0], colors[i][j+1][1],  colors[i][j+1][2])
                        glVertex3f(matrix[i][j+1][0], matrix[i][j+1][1] - 5,  matrix[i][j+1][2])

                        glColor3f(colors[i + 1][j + 1][0], colors[i + 1][j + 1][1], colors[i + 1][j + 1][2])
                        glVertex3f(matrix[i + 1][j + 1][0], matrix[i + 1][j + 1][1] - 5, matrix[i + 1][j + 1][2])
                        glEnd()


def render(time):

    makeMatrix(matrix, colors)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()
    spin(time * 180 / pi)
    drawEgg()
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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()