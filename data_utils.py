import pandas as pd
import numpy as np
import os
import paths as paths


data_repo=paths.DATA_REPO

def file_reader(file_name):
    file_path=os.path.join(data_repo+"/"+file_name+".csv")
    df=pd.read_csv(file_path)
    df=df.to_numpy()
    return df


    