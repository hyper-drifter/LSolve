# LSolve
Requirements: Python 2.7, tkinter, numpy, and matplotlib

A personal project of mine which solves Laplace's equation for electric potentials in the space between a set of electrodes. It currently only works with 2 dimensional arrays. Input files are tsv, csv, and txt. Any nonzero values in the input files are assumed to be boundary conditions and are treated as electrodes with constant voltages. Output files are tsv format. I recently added a simple GUI via python and now there is a simple over-relaxation algorithm to improve speed. After solving, python will then plot a resulting surface potential plot. Due to some Pyplot weirdness I've made it so that the plot automatically closes after about 2 and a half hours.

To run simple execute the LSolve.py script. You will then be asked for an appropriate grid file via a file selection GUI. The output tsv will be stored in the input file's original directory. Some examples are stored in the examples folder. One is a simple small capacitor and the other is a much larger model of a quadrupole.
