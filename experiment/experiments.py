import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

file_path_white = '/Users/U756064/PycharmProjects/MLOps_pilot/data/winequality-white.csv'
file_path_red = '/Users/U756064/PycharmProjects/MLOps_pilot/data/winequality-red.csv'
df_white = pd.read_csv(file_path_white, delimiter = ";")
df_red = pd.read_csv(file_path_red, delimiter = ";")

df_white.head()
