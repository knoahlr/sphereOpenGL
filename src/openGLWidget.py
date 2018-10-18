
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import random
import sys


from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFormLayout, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, \
QLabel, QTextEdit, QLineEdit, QPushButton, QFrame, QOpenGLWidget

from defaultMenuBar import DefaultMenuBar


class OpenGLWidget(QOpenGLWidget):

    def __init__(self):

        super().__init__()

        ''' Fields '''
        n   = 20
        r   = 0.05
        g   = 9.8
        dt  = 0.001
        cor = 0.6

        balls = []
        tm  = 0.0
        th  = 0.0
        max =  1.0-r
        min = -1.0+r
        rt = False



    def initalizeGL(self):

        glutInit(())
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(500,500)
        glutCreateWindow("GLUT Bouncing Ball in Python")
        # glutDisplayFunc(display)
        glutIdleFunc(self.update)
        # glutMouseFunc(mouse)
        self.g_init()
        # glutMainLoop()

    def g_init(self):
        global tm
        for i in range(self.n):
            p = [
                min + random()*(max-min),
                min + random()*(max-min),
                0.9]
            v = [
                -1.5 + random()*3.0,
                -1.5 + random()*3.0,
                -1.0 + random()*2.0]
            self.balls.append({'pos':p,'vel':v})
        print(len(self.balls))
        tm = 0.0

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0,1.0,1.0,1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,1.0,1.0,50.0)
        glTranslatef(0.0,0.0,-3.5)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):

        global balls,th
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(th,0.0,1.0,0.0)
        glRotatef(90.0,-1.0,0.0,0.0)
        glutWireCube(2.0)
        for b in self.balls:
            glPushMatrix()
            glTranslatef(b['pos'][0],b['pos'][1],b['pos'][2])
            glutSolidSphere(self.r,50,50)
            glPopMatrix()
        glPopMatrix()
        glutSwapBuffers()
        

    def update(self):
        
        global balls,g,dt,max,min,cor,rt,th
        for b in self.balls:
            b['vel'][2] += -self.g*self.dt
            b['pos'][0] += b['vel'][0]*self.dt
            b['pos'][1] += b['vel'][1]*self.dt
            b['pos'][2] += b['vel'][2]*self.dt

            if (abs(b['pos'][0]) >= max):
                b['vel'][0] *= -self.cor
                if b['pos'][0] < 0:
                    b['pos'][0] = min
                else:
                    b['pos'][0] = max

            if (abs(b['pos'][1]) >= max):
                b['vel'][1] *= -self.cor
                if b['pos'][1] < 0:
                    b['pos'][1] = min
                else:
                    b['pos'][1] = max

            if (abs(b['pos'][2]) >= max):
                b['vel'][2] *= -self.cor
                if b['pos'][2] < 0:
                    b['pos'][2] = min
                else:
                    b['pos'][2] = max

        if self.rt:
            th += 0.2
            if th>360.0:
                th -= 360.0

        glutPostRedisplay()

    # def mouse(button,state,x,y):
    # global rt
    # if button == GLUT_LEFT_BUTTON:
    #     rt = not state
    # elif button == GLUT_RIGHT_BUTTON:
    #     sys.exit(0)    































