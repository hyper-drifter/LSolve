#!/usr/bin/python
"""
Author: Taylor Grubbs
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#imports grid from file
myGrid = np.loadtxt('quadrupoleV2.tsv', dtype=float)
rows = myGrid.shape[0]
columns = myGrid.shape[1]

#finds nonzero points in intial array (electrode points)
def getElectrodePoints(grid):
    electrodeGrid = np.zeros(grid.shape, dtype=float)
    i = 0
    for row in grid:
        j = 0
        for value in row:
            if value != 0:
                electrodeGrid[i][j] = 1
            j = j+1
        i = i+1
    return electrodeGrid

#solves Laplace's equation
def laplaceSolve(grid):
    electrodes = getElectrodePoints(myGrid)
    rows = grid.shape[0]
    columns = grid.shape[1]
    convergence = 10**-5 #desired convergence value
    deltaV = 1. #stores total change in grid between iterations
    newV = np.copy(grid) #new grid where final array will be stored
    iterNum = 1 #tracks number of iterations
    oldGridValue = 0. #stores grid values before refinement (Gauss-Seidel)
    diff = 0. #difference between new and old grid value
    relax = 2/(1+math.pi/grid.shape[0]) #relaxation factor, would like to have dynamic over-relaxation

    while deltaV >= convergence:
        deltaV = 0
        for i in range(0, grid.shape[0]):
            for j in range(0, grid.shape[1]):

                if electrodes[i][j] == 1:
                    continue

                oldGridValue = newV[i][j]

                #all possible cases
                if i==0 and j==0:
                    newV[i][j] = .5*(newV[i+1][j]+newV[i][j+1])#top left corner
                elif i==0 and j!=0 and j != columns-1:
                    newV[i][j] = 1./3.*(newV[i+1][j]+newV[i][j-1]+newV[i][j+1])#top
                elif i == 0 and j == columns-1:
                    newV[i][j] =.5*(newV[i+1][j]+newV[i][j-1])#top right corner
                elif i!=0 and i != rows-1 and j == columns-1:
                    newV[i][j] = 1./3.*(newV[i-1][j]+newV[i+1][j]+newV[i][j-1])#right side
                elif i == rows-1 and j == columns-1:
                    newV[i][j] =.5*(newV[i-1][j]+newV[i][j-1])#bottom right corner
                elif i == rows-1 and j != columns-1 and j != 0:
                    newV[i][j] =1./3.*(newV[i-1][j]+newV[i][j-1]+newV[i][j+1])#bottom
                elif i == rows-1 and j == 0:
                    newV[i][j] =.5*(newV[i-1][j]+newV[i][j+1])#bottom left corner
                elif i!=0 and i != rows-1 and j == 0:
                    newV[i][j] =1./3.*(newV[i-1][j]+newV[i+1][j]+newV[i][j+1])#left
                else:
                    newV[i][j] = .25*(newV[i+1][j]+newV[i-1][j]+newV[i][j+1]+newV[i][j-1])#everywhere else

                diff = newV[i][j] - oldGridValue
                newV[i][j] = oldGridValue + relax*diff

                deltaV = deltaV + abs(diff)

        iterNum = iterNum + 1

    print('Solved in ' + str(iterNum) + ' iterations\n')
    np.savetxt('output.tsv', newV, delimiter='\t') #storing new grid in output file
    return newV

solvedGrid = laplaceSolve(myGrid)

#Now trying to graph potential surface
xVals,yVals = np.meshgrid(range(0,rows), range(0,columns))

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(xVals, yVals, solvedGrid)
plt.show()
