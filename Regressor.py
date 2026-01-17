import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_utils as du

def regression(file):
    df=du.file_reader(file)
    
    if df.shape[1] == 2:
        x = df[:, 0]
        y = df[:, 1]

        x_mean = np.mean(x)
        y_mean = np.mean(y)

        b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
        b0 = y_mean - b1 * x_mean

        return b1, b0

    else:

        X = df[:, :-1]   
        y = df[:, -1]    

        ones = np.ones((X.shape[0], 1))
        X = np.hstack((ones, X))

        beta = np.linalg.inv(X.T @ X) @ X.T @ y

        return beta

    



