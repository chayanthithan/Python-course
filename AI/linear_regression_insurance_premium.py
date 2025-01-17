# -*- coding: utf-8 -*-
"""Linear_Regression_Insurance Premium.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kt37fRUl4K0gRAgigOcEcvEyMRTuJWe2
"""

!pip install pandas

import pandas as pd
dataset = pd.read_csv("/content/sample_data/simplelinearregression.csv")
print(dataset)

independent = dataset[['Premium']]
print(independent)

dependent = dataset[['Age']]
print(dependent)

!pip install scikit_learn

input = x
output = y
train , test

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(independent,dependent,test_size=0.20,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_predict = regressor.predict(x_test)
print(y_predict)

from sklearn.metrics import r2_score
r_score = r2_score(y_test,y_predict)
print(r_score)