# Numerical Operations
import math
import numpy as np

# Reading/Writing Data
import pandas as pd
import csv

import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression



train_data, test_data = pd.read_csv('covid_train.csv') , pd.read_csv('covid_test.csv')

a = train_data.iloc[:,1:88]
b = train_data.iloc[:,88:89]
# print(a)
# print(b)

#print(test_data.target)

selector = SelectKBest(score_func=f_regression, k=17)
bf = selector.fit_transform(a,b.values.ravel())
selector.get_support()
a.columns[selector.get_support()]
s = list(a.columns[selector.get_support()])
print(s)

# selected_features = selector.get_support(indices=True)

#feature_names = list(a.feature_names[selected_features])
# print("Selected features:", feature_names)