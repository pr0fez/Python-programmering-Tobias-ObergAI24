# Labb3


## Program description.
This program reads in unlabelled data from a csv file. It adds two columns, X and Y. X for left column and Y for right column. Using example-values for y = kx + m. It checks if the points from the data is either right and above the line or left and below the line. It loops through the whole dataframe.

The next function classifies the points. If the point is right and above the line it will be labeled as 1 and if the point is left and below the line it will be labeled as 0. It then writes to the csv file and creates a new column called "position". This is used for the labels. 

Finally it scatters all the points and also plots the line as a reference that is used from the example-values. 



### How to run the program.
If you want to run this program yourself you can use a csv file of your own or just simply run this program. If you want to check different values you can manipulate y = kx + m to your own liking in this program.
