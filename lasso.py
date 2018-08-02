import pandas as pd
import numpy as np
from skrebate import ReliefF
from sklearn import preprocessing
from sklearn.linear_model import Lasso
import sys


# filenames = ['alon', 'borovecki', 'burczynski', 'chiaretti', 'chin', 'chowdary', 'christensen', 'golub', 'gordon', 'gravier', 'khan', 'nakayama', 'pomeroy', 'shipp', 'singh', 'sorlie', 'su', 'subramanian', 'sun', 'tian', 'west', 'yeoh']

name = sys.argv[1]

features = pd.read_csv('data/' + name + '_inputs.csv', header = None)
labels = pd.read_csv('data/' + name + '_outputs.csv', header = None)

features.fillna(0, inplace = True)

features = np.asarray(features.values)
labels = np.transpose(np.asarray(labels.values.ravel() - 1, dtype=int))

min_max_scaler = preprocessing.MinMaxScaler()
features = min_max_scaler.fit_transform(features)

lasso = Lasso(alpha=0.001)
lasso.fit(features, labels)

indexes = np.asarray(np.where(lasso.coef_ != 0))

np.savetxt('features/' + name + '_lasso.txt', lasso.coef_)

print(name, ': ', indexes.shape)
