import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Code\Python-programmering-Tobias-ObergAI24\Labs\Labs\unlabelled_data.csv", header= None) 
# print(df.head())

k = 0.78
m = -0.01
# y = 0.78x + -0.01

df.columns = ["x", "y"]                                 # Adds columns x,y in DataFrame.

def check_position(point):                              # Function for checking position of point.
    x, y = point
    y_line = 0.78 * x + -0.01                           # k, m - values.

    if y < y_line:                                      
        if x < 0:
            return "Left and Below"
        else:
            return "Right and Below"
    elif y > y_line:
        if x < 0:
            return "Left and Above"
        else:
            return "Right and Above"
    
for index, row in df.iterrows():                       # Looping each row in DataFrame.
    point = (row["x"], row["y"]) 
    position = check_position(point)
    # print(f"Point {point} is: {position}")


def classify_points(row):                              # Function for classifying x and y as 0 or 1 depending on position.
    y_line = k * row["x"] + m
  
    return 0 if row["y"] < y_line else 1

df["Position"] = df.apply(classify_points, axis=1)     # Creates column: Position and applies it to each row in DF.


df.to_csv(r"C:\Code\Python-programmering-Tobias-ObergAI24\Labs\Labs\labelled_data.csv", index=False)      # Writes and creates file labelled_data.csv
# print(df)


def scatter():                                                      
    data_x = np.linspace(df["x"].min(), df["y"].max(), 100)   # Min and max value between x and y. Makes it possible to plot the line.     
    data_y = 0.78 * data_x + -0.01
    
    for index, row in df.iterrows():
        plt.scatter(row["x"], row["y"], color = "red" if row["Position"] == 1 else "blue") # For-loop for every labelled csv point.
    
    plt.plot(data_x, data_y, color= "black", label= "y = 0.78x - 0.01")                   # Plots the line with "y = 0.78x - 0.01"
    plt.title("Classified Points")
    plt.text(df["x"].min(), df["y"].max(), "Red = Position 1\nBlue = Position 0", 
             fontsize=9, color="black", verticalalignment= "top")
    plt.grid()
    plt.show()

scatter()