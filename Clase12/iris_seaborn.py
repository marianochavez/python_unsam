# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:12:00 2021

@author: mariano
"""
from sklearn.datasets import load_iris
import seaborn as sns

iris_dataset = load_iris()

iris_dataframe['target'] = iris_dataset['target']

sns.pairplot(iris_dataframe, hue = 'target')