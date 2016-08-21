/*
     Author: Taylor Grubbs
     This version uses successive over-relaxation which reduces iteration numbers significantly
*/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//Reads in array from tsv file and returns as a double array
double ** gridRead(const char *fileName, int rows, int columns)
{
     FILE *gridFile = fopen(fileName, "r");
     int i,j;
     double **grid;

     //allocates memory for grid
     grid = (double **) malloc(rows*sizeof(double *));
     for(i = 0; i < rows; i++){
     grid[i] = (double *) malloc(columns*sizeof(double));
     }

     //reads in grid values
     for(i = 0; i < rows; i++){
       for(j = 0; j < columns; j++){
         fscanf(gridFile, " %lf", &grid[i][j]);
       }
     }

     fclose(gridFile);
     return(grid);
}

/*
Iterates over array, numerically solving Laplace's equation using the Jacobi
relaxation method. Will incorporate dynamic over-relaxation
*/
void laplaceSolve(double ** initPotGrid, int rows, int columns)
{

     int i,j;
     int boundaryPoints[rows][columns]; //finds initial nonzero voltages (the electrodes)
     for(i = 0; i < rows; i++){
          for(j = 0; j < columns; j++){
               if(initPotGrid[i][j] != 0){boundaryPoints[i][j] = 1;}
               else{boundaryPoints[i][j] = 0;}
          }
     }

     double convergence = pow(10, -5); //covergence value 10^-6
     double deltaV; //tracks total change in potential per grid iteration
     double **newV = initPotGrid; //new grid where solved potentials are stored, I realize that this is just pointing to the same memory as initPotGrid haha
     int iterNum = 1; //stores current interation number
     int minIter = 10; //defines minimum number of iterations needed
     double oldGridValues; //previous grid value before update
     double diff; //difference between previous and new grid value
     double relax = 2/(1+M_PI/rows); //relaxation parameter aka alpha in some texts

     //this loop solves Laplace's equation
     while (deltaV >= convergence || iterNum < minIter) {
          deltaV = 0;
          for(i = 0; i < rows; i++){
               for(j = 0; j < columns; j++){
                    if(boundaryPoints[i][j] == 1){continue;}
                    oldGridValues = newV[i][j];

                    //checks for every edge case
                    if(i==0 && j==0){newV[i][j] = .5*(newV[i+1][j]+newV[i][j+1]);} //top left corner
                    else if(i==0 && j!=0 && j != columns-1){newV[i][j] = 1./3.*(newV[i+1][j]+newV[i][j-1]+newV[i][j+1]);}//top
                    else if(i == 0 && j == columns-1){newV[i][j] =.5*(newV[i+1][j]+newV[i][j-1]);}//top right corner
                    else if(i!=0 && i != rows-1 && j == columns-1){newV[i][j] = 1./3.*(newV[i-1][j]+newV[i+1][j]+newV[i][j-1]);}//right side
                    else if(i == rows-1 && j == columns-1){newV[i][j] =.5*(newV[i-1][j]+newV[i][j-1]);}//bottom right corner
                    else if(i == rows-1 && j != columns-1 && j != 0){newV[i][j] =1./3.*(newV[i-1][j]+newV[i][j-1]+newV[i][j+1]);}//bottom
                    else if(i == rows-1 && j == 0){newV[i][j] =.5*(newV[i-1][j]+newV[i][j+1]);}//bottom left corner
                    else if(i!=0 && i != rows-1 && j == 0){newV[i][j] =1./3.*(newV[i-1][j]+newV[i+1][j]+newV[i][j+1]);}//left
                    else{newV[i][j] = .25*(newV[i+1][j]+newV[i-1][j]+newV[i][j+1]+newV[i][j-1]);}//everywhere else

                    diff = newV[i][j] - oldGridValues;
                    newV[i][j] = oldGridValues+relax*diff;

                    deltaV = deltaV + fabs(diff);
               }
          }

          iterNum++;
     }
     printf("Solved in %i iterations.\n", iterNum); //prints number of iterations

     //writes new grid values to file
     FILE *gridFile = fopen("LSolve-output.tsv", "w");
     for(i = 0; i < rows; i++){
       for(j = 0; j < columns; j++){
         fprintf(gridFile, " %lf\t", newV[i][j]);
       }
       fprintf(gridFile, "\n");
     }
     fclose(gridFile);

     printf("File saved as \"LSolve-output.tsv\"\n");
}
