#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import random
import sys


from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFormLayout, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, \
QLabel, QTextEdit, QLineEdit, QPushButton, QFrame

from defaultMenuBar import DefaultMenuBar
from openGLWidget import OpenGLWidget

from pathlib import Path
import numpy as np


ICON = Path(r'..\articles\atom.png')

DATA = r"..\data"

class SceneWindow(QMainWindow):

    '''
    Windows for presenting Canvas in real time. Show only one view
    To be Implemented -- Stereo views
    '''


    def __init__(self):

        super().__init__()

        '''Fields'''

        self.rangeIndex = 0



        ''' Window Properties'''

        self.Icon = QtGui.QIcon(str(ICON))
        self.setMinimumSize(self.sizeHint())
        self.resize(1200, 800)
        self.setWindowTitle('Open GL 3D')
        self.setWindowIcon(self.Icon)
    
        self.setMenuBar(DefaultMenuBar(self))

        ''' Setting window layout and central widget '''
        self.centralwidget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignCenter)


        ''' Frames'''
        self.canvasFrame = QGroupBox("Canvas Frame")
        self.controlFrame = QGroupBox("Control Frame")

        self.canvasFrameLayout  = QVBoxLayout(self.canvasFrame)
        self.controlFrameLayout = QFormLayout(self.controlFrame)

        self.canvasWidget = QWidget()
        self.canvasWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.canvasWidgetLayout = QHBoxLayout()
        
        
        '''Labels'''

        self.setFunctionLabel = QLabel("Set Function")
        self.setFunctionBox = QLineEdit() #placeholder="input Function in Cartesian Co-ordSinates"SSS

        self.controlFrameLayout.setWidget(0, QFormLayout.LabelRole, self.setFunctionLabel)
        self.controlFrameLayout.setWidget(0, QFormLayout.FieldRole, self.setFunctionBox)


        # self.canvasFrameLayout.addWidget(self.canvasWidget)
        self.addCanvas()

        self.canvasWidget.setLayout(self.canvasWidgetLayout)
        self.verticalLayout.addWidget(self.canvasFrame)
        self.verticalLayout.addWidget(self.controlFrame)

        self.setCentralWidget(self.centralwidget)


    def addCanvas(self):

        self.openGLWidget = OpenGLWidget()

        self.canvasWidgetLayout.addWidget(self.openGLWidget)

        






        
