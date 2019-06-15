import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
PG.head()

PG.tail()

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
#print (PG['simple_return'])

#plot graph
PG['simple_return'].plot(figsize=(8,5))
plt.show()

#average daily rate of return 
avg_returns_d = PG['simple_return'].mean()


#average return per year
avg_returns_a = PG['simple_return'].mean() * 250
print (str(round(avg_returns_a, 5) * 100) + ' %')