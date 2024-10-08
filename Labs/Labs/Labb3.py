import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(r"C:\Code\Python-programmering-Tobias-ObergAI24\unlabelled_data.csv") 
# print(df)


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
    point = (row['x'], row['y']) 
    position = check_position(point)
    print(f"Point {point} is: {position}")





# def classify_points():



# def write_to_csv(row):
    
#     y_line = k * row['x'] + m
  
#     return 0 if row['y'] < y_line else 1


# df['position'] = df.apply(write_to_csv, axis=1)


# df.to_csv(r"C:\Code\Python-programmering-Tobias-ObergAI24\unlabelled_data.csv", index=False)
# print(df)
    


    




