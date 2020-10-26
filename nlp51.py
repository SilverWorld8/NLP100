# -*- coding: utf-8 -*-

import csv
import pandas as pd/Users/hayashidanaoki/Desktop/python_sample/nlp51.py
import numpy as np

from sklearn.model_selection import train_test_split

path1 = './input/train.txt'
path2 = './input/valid.txt'
path3 = './input/test.txt'

col_name = ['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP']

df = pd.read_csv( path1, sep='\t', header=None, names=col_name)

df = df.get_dummies["title"]

print(df.head())
