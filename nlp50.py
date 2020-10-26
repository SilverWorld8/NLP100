# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

path = './input/NewsAggregatorDataset/newsCorpora.csv'
col_name = ['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP']

df = pd.read_csv( path, sep='\t', header=None, names=col_name)

df1 = df[df["PUBLISHER"].isin(["Reuters","Huffington Post","Businessweek","Contactmusic.com","Daily Mail"])]

df2 = df1.sample(frac=1, random_state=0)

narr = df2.values
a_train, a_test = train_test_split(narr, test_size=0.2)
a_test, a_valid = train_test_split(a_test, test_size=0.5)

print(a_train.shape,a_test.shape,a_valid.shape)

np.savetxt('./input/train.txt', a_train, fmt='%s',delimiter='\t')
np.savetxt('./input/valid.txt', a_valid, fmt='%s',delimiter='\t')
np.savetxt('./input/test.txt', a_test, fmt='%s',delimiter='\t')
