# -*- coding: utf-8 -*-
"""bank_customer_churn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GNvEDvXrhWFepAm9X1d8T_j2AAFo7h0r

#import library
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

"""# import data"""

df=pd.read_csv('/content/Customer-Churn-Records.csv')

df.head()

df.info()

"""#Encoding

"""

df['Geography'].value_counts()

df['Gender'].value_counts()

df.replace( {'Gender':{'Male':0,'Female':1}},inplace=True)

df['NumOfProducts'].value_counts()

df.replace( {'NumOfProducts':{1:0,2:1,3:1,4:1}},inplace=True)

df['HasCrCard'].value_counts()

df['IsActiveMember'].value_counts()

df.loc[(df['Balance']==0),'Exited'].value_counts()

df['Zero balance']=np.where(df['Balance']>0,1,0)

df['Zero balance'].hist()

df.groupby(['Exited','Geography']).count()

"""#define label and features"""

df.columns

x=df.drop(['Surname','Exited'],axis=1)

y = df['Exited']

x.shape,y.shape

"""#handling imbalance data
 undersaampling
 oversamlping

"""

df['Exited'].value_counts()

sns.countplot(x='Exited',data=df);

x.shape,y.shape

"""# random under sampling"""

from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=2529)

x_rus,y_rus = rus.fit_resample(x,y)

x_rus.shape,y_rus.shape,x.shape,y.shape

y.value_counts()

y_rus.value_counts()

y_rus.plot(kind='hist')

"""#random over sampling

"""

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=2529)

x_ros,y_ros = ros.fit_resample(x,y)

x_ros.shape,y_ros.shape,x.shape,y.shape

y.value_counts()

y_ros.value_counts()

y_ros.plot(kind='hist')

"""my name is gaurav kuamr!!!"""