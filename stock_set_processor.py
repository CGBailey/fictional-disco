from models import StockSet
from models.session import session
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

plt.close('all')

df = pd.read_csv('./raw_data/stocks/AAPL.csv', index_col='Date', parse_dates=['Date'], header=0,
                 names=['Date', 'Open', 'High', 'Low', 'Close', 'ADJ Close', 'Volume']).drop(['Open', 'High', 'Low', 'ADJ Close', 'Volume'], axis=1)
df = df.loc['2010-4-02 23:00': '2020-4-01']

new_row = StockSet('', 
                   df.first('1D').to_numpy()[0][0],
                   df.last('1D').to_numpy()[0][0],
                   df.first('1D').index[0],
                   df.last('1D').index[0],
                   "Apple",
                   "APPL")
session.add(new_row)
session.commit()
