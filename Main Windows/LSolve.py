"""
Author: Taylor Grubbs
"""
from Tkinter import Tk #assumes python 2.7
import tkMessageBox
from tkFileDialog import askopenfilename
import os


#creates simple gui for user to choose initial grid file to solve
Tk().withdraw()
tkMessageBox.showinfo("LSolve", "Choose a tsv, csv, or txt file to solve.")

laplaceExecutable = os.path.realpath("laplace.exe") #finds laplace binary file which should be in same directory as this script

initGridFile = askopenfilename()
directory = os.path.dirname(initGridFile)
fileName = os.path.basename(initGridFile)

#checks if file type is correct
if not fileName.endswith('.tsv') and not fileName.endswith('.csv') and not fileName.endswith('.txt'):
    tkMessageBox.showinfo("LSolve", "Invalid file type chosen")
    exit()

#changing working directory so that output is stored with input file
os.chdir(directory)

#string manipulation so that python can tell windows to run the program in windows :P
commandString = ["\"\"",laplaceExecutable,"\""," \"",fileName,"\"\""]
commandString = ''.join(commandString)

os.system(commandString)

outputDirMessage = ["Output saved in ", directory]
tkMessageBox.showinfo("LSolve", ''.join(outputDirMessage))
