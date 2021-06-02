from tkinter import *
from datetime import *

import tkinter.font
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.animation import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Graph(object):
    def __init__(self, parent, max):
        self.Fig = plt.figure(facecolor = '#333333')
        self.Ax = plt.subplot(111)
        self.Line = self.Ax.plot(np.arange(max), np.ones(max, dtype=np.float)*np.nan, lw = 1, c = 'white', ms = 1)
        self.X = list()
        self.Y = list()

    def AddData(self, X, Y):
        self.NewData.append(X, Y);

    def Init():
        return self.Line;