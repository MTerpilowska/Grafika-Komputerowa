#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
up_key_pressed = 0
down_key_pressed = 0
mouse_x_pos_old = 0
delta_x = 0
parameters = [0] * 12

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def shutdown():
    pass


def render(time):
    global theta

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    for i in range (12):
        change_parameter(i)

    glRotatef(theta, 0.0, 1.0, 0.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

    glFlush()


def change_parameter(n):
    global light_ambient
    global light_diffuse
    global light_specular
    global up_key_pressed
    global down_key_pressed

    if parameters[n]:
        if n >= 0:
            if n >= 4:
                if n >= 8:
                    n -= 8
                    if up_key_pressed == 1 and light_specular[n] <= 0.9:
                        light_specular[n] = round(light_specular[n] + 0.1, 1)
                        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
                        print('specular = ' + str(light_specular))
                    if down_key_pressed == 1 and light_specular[n] >= 0.1:
                        light_specular[n] = round(light_specular[n]- 0.1, 1)
                        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
                        print('specular = ' + str(light_specular))
                else:
                    n -= 4
                    if up_key_pressed == 1 and light_diffuse[n] <= 0.9:
                        light_diffuse[n] = round(light_diffuse[n] + 0.1, 1)
                        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
                        print('diffuse = ' + str(light_diffuse))
                    if down_key_pressed == 1 and light_diffuse[n] >= 0.1:
                        light_diffuse[n] = round(light_diffuse[n] - 0.1, 1)
                        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
                        print('diffuse = ' + str(light_diffuse))
            else:
                if up_key_pressed == 1 and light_ambient[n] <= 0.9:
                    light_ambient[n] = round(light_ambient[n] + 0.1, 1)
                    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
                    print('ambient = ' + str(light_ambient))
                if down_key_pressed == 1 and light_ambient[n] >= 0.1:
                    light_ambient[n] = round(light_ambient[n] - 0.1, 1)
                    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
                    print('ambient = ' + str(light_ambient))
        
        down_key_pressed = 0
        up_key_pressed = 0


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def actual_parameter(n):
    global parameters
    parameters = [0] * 12
    parameters[n] = 1

def keyboard_key_callback(window, key, scancode, action, mods):
    global down_key_pressed
    global up_key_pressed

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_1 and action == GLFW_PRESS:      #ambient
        actual_parameter(0)
    if key == GLFW_KEY_2 and action == GLFW_PRESS:
        actual_parameter(1)
    if key == GLFW_KEY_3 and action == GLFW_PRESS:
        actual_parameter(2)
    if key == GLFW_KEY_4 and action == GLFW_PRESS:   
        actual_parameter(3)
    
    if key == GLFW_KEY_5 and action == GLFW_PRESS:      #diffuse
        actual_parameter(4)
    if key == GLFW_KEY_6 and action == GLFW_PRESS:
        actual_parameter(5)
    if key == GLFW_KEY_7 and action == GLFW_PRESS:    
        actual_parameter(6)
    if key == GLFW_KEY_8 and action == GLFW_PRESS:
        actual_parameter(7)
    
    if key == GLFW_KEY_Q and action == GLFW_PRESS:      #specular
        actual_parameter(8)
    if key == GLFW_KEY_W and action == GLFW_PRESS:
        actual_parameter(9)
    if key == GLFW_KEY_E and action == GLFW_PRESS:
        actual_parameter(10)
    if key == GLFW_KEY_R and action == GLFW_PRESS:
        actual_parameter(11)
    
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:   # - +
        down_key_pressed = 1
    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        up_key_pressed = 1


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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