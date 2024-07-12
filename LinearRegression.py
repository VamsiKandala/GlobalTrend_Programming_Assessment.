import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('/content/drive/MyDrive/ML Data sets/Squares_data.csv')


Num = df[['number']]
Sq = df[['Square']]

poly = PolynomialFeatures(degree=2)
Num_poly = poly.fit_transform(Num)

reg = LinearRegression()
reg.fit(Num_poly, Sq)

Num_new = np.array([[25]])
Num_new_poly = poly.transform(Num_new)
prediction = reg.predict(Num_new_poly)
print(prediction)
