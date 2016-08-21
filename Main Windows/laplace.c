/*
     Author: Taylor Grubbs
*/
#include "laplace_SOR.h"

int main(int argc, char const *argv[])
{
     //input check
     if(argc != 2){printf("Invalid argument. Program Stopped.\n"); exit(0);}

     const char *fileName = argv[1];

     //read in potential grid file
     double **myPotGrid = gridRead(fileName);
     int rows = getRows(fileName);
     int columns = getColumns(fileName);
     printf("Grid file found\n");

     //solves Laplace's equation on original gridfile and stores in another 2-D array
     printf("Solving Laplace\'s equation...\n");
     laplaceSolve(myPotGrid, rows, columns);

     return 0;
}
