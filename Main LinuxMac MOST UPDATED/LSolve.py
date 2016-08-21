#!/usr/bin/python
"""
Author: Taylor Grubbs
"""
from Tkinter import Tk #assumes python 2.7
import tkMessageBox
from tkFileDialog import askopenfilename
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#creates simple gui for user to choose initial grid file to solve
Tk().withdraw()
tkMessageBox.showinfo("LSolve", "Choose a tsv, csv, or txt file to solve.")

laplaceExecutable = os.path.realpath("laplace") #finds laplace binary file which should be in same directory as this script

initGridFile = askopenfilename()
directory = os.path.dirname(initGridFile)
fileName = os.path.basename(initGridFile)

#checks if file type is correct
if not fileName.endswith('.tsv') and not fileName.endswith('.csv') and not fileName.endswith('.txt'):
    tkMessageBox.showinfo("LSolve", "Invalid file type chosen")
    exit()

#cheeky way of allowing command line to handle files with spaces
fileName = fileName.split()
for i in range(len(fileName)):
    fileName.insert(2*i, '\\ ')
del fileName[0]
fileName = ''.join(fileName)
print(fileName)

#same thing for laplace executable path
laplaceExecutable = laplaceExecutable.split()
for i in range(len(laplaceExecutable)):
    laplaceExecutable.insert(2*i, '\\ ')
del laplaceExecutable[0]
laplaceExecutable = ''.join(laplaceExecutable)
#I am well aware that this looks awkward but it works and it's a lot simpler than creating my own gui


#changing working directory so that output is stored with input file
os.chdir(directory)
initGrid = np.loadtxt(fileName, dtype=float)#this reduces complexity of input tsv files. One no longer has to put the number of rows and columns in the first line of the file
rows = initGrid.shape[0]
columns = initGrid.shape[1]

commandString = [laplaceExecutable," ",fileName," ",str(rows)," ",str(columns)]
os.system(''.join(commandString))

outputDirMessage = ["Output saved in ", directory]
tkMessageBox.showinfo("LSolve", ''.join(outputDirMessage))

#plotting result
solvedGrid = np.loadtxt('LSolve-output.tsv', dtype=float)

xVals,yVals = np.meshgrid(range(0,rows), range(0,columns))

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(xVals, yVals, solvedGrid)
plt.ion()
plt.show()
#pyplot is annoying. LOL the plot will only stay open for like 2.5 hours
plt.pause(10000)
