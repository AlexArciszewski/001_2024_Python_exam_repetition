
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = sns.load_dataset('tips')

print(df.head())
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4


#wykres
plt.pie(df['day'].value_counts(), labels=df['day'].value_counts().index, autopct='%1.2f%%')
plt.show()