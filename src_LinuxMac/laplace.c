/*
     Author: Taylor Grubbs
*/
#include "laplace_SOR_E.h"

int main(int argc, char const *argv[])
{
     //input check
     if(argc != 4){printf("Invalid argument. Program Stopped.\n"); exit(0);}

     const char *fileName = argv[1];
     int rows = atoi(argv[2]);
     int columns = atoi(argv[3]);

     //read in potential grid file
     double **myPotGrid = gridRead(fileName, rows, columns);

     printf("Grid file found\n");

     //solves Laplace's equation on original gridfile and stores in another 2-D array
     printf("Solving Laplace\'s equation...\n");
     laplaceSolve(myPotGrid, rows, columns);

     return 0;
}
