from tqdm.notebook import tqdm
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import os

# loading the data
df_test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'timeseries/Gun_Point/Gun_Point_TEST'), sep=',', header=None)
df_train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'timeseries/Gun_Point/Gun_Point_TRAIN'), sep=',', header=None)

X_train = df_train.iloc[:,1:].values
y_train = df_train[0].values

def euclidean_distance(ts_a, ts_b):
    """
    Computes the Euclidean distance between two time series
    """
    dist = 0
    for i in range(len(ts_a)):
        print(f'Comparing index {i}: {ts_a[i]} vs {ts_b[i]}')
        dist += (ts_a[i] - ts_b[i]) ** 2
    return math.sqrt(dist)

distance = euclidean_distance(X_train[0], X_train[1])
print(f'Euclidean Distance between first two training samples: {distance}')

plt.plot([i for i in range(0,len(X_train[0]))],X_train[0])   
plt.xlabel('Timestep')
plt.ylabel('Value')
plt.title('Gun Point Time Series Example')
plt.show()