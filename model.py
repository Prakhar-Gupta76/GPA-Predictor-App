import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
# We can override the default matplotlib styles with those of Seaborn
sns.set()
raw_data = pd.read_csv("1.03.+Dummies.csv")
## Map the data
data = raw_data.copy()
data['Attendance'] = data['Attendance'].map({'Yes':1,'No': 0})
# data.describe()
y=data['GPA']
x1=data[['SAT','Attendance']]
x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
# results.summary()
import pickle
with open('model.pkl', 'wb') as model_file:
    pickle.dump(results, model_file)
