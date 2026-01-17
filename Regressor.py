import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_utils as du

def regression(file):
    df=du.file_reader(file)
    if df.shape[1]==2:
        b1=np.sum((df[:0]-np.mean(df[:0]))@(df[:1]-np.mean(df[:1])))/np.sum((df[:0]-np.mean(df[:0]))@(df[:0]-np.mean(df[:0])))
        b0=np.mean(df[:1])-b1*np.mean(df[:0])
        return b1,b0
    



