import os
from models import StockSet
from models.session import session
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
from sqlalchemy import and_


plt.close('all')


# directory = os.fsencode('./raw_data/stocks')

# meta_df = pd.read_csv("./raw_data/symbols_valid_meta.csv",
#                  names=["Nasdaq Traded", "Symbol", "Security Name", "Listing Exchange", "Market Category", "ETF", "Round Lot Size", "Test Issue", "Financial Status", "CQS Symbol", "NASDAQ Symbol", "NextShares"]).drop(["Nasdaq Traded", "Listing Exchange", "Market Category", "ETF", "Round Lot Size", "Test Issue", "Financial Status", "CQS Symbol", "NASDAQ Symbol", "NextShares"], axis=1)

# meta_df.style.hide_index()
# print(meta_df['Symbol'])
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     pathname = os.path.join('./raw_data/stocks', filename)
#     if filename.endswith(".csv") and os.path.exists(pathname):
#         df = pd.read_csv(pathname, index_col='Date', parse_dates=['Date'], header=0,
#                          names=['Date', 'Open', 'High', 'Low', 'Close', 'ADJ Close', 'Volume']).drop(['Open', 'High', 'Low', 'ADJ Close', 'Volume'], axis=1)
#         df = df.loc['2010-4-02 23:00': '2020-4-01']
#         new_row = StockSet('',
#                         df.first('1D').to_numpy()[0][0],
#                         df.last('1D').to_numpy()[0][0],
#                         df.first('1D').index[0],
#                         df.last('1D').index[0],
#                            meta_df.loc[meta_df['Symbol'] == filename.split('.')[0]]['Security Name'].to_string(index=False),
#                         filename.split('.')[0])
#         print(new_row.last_price)
#         session.add(new_row)
#         session.commit()
#         continue
#     else:
#         continue

dated_sets = session.query(StockSet).filter(
    and_(StockSet.first_date == '2010-4-05', StockSet.first_price >= 4.0)).all()

def calc_growth_rate(first_price, last_price):
     return (100 * (last_price - first_price)/first_price)


stock_growth_rates = [{"name": stock_set.name, "growth_rate": calc_growth_rate(
    stock_set.first_price, stock_set.last_price)} for stock_set in dated_sets]
stock_growth_rates = sorted(stock_growth_rates, key = lambda i: i['growth_rate'], reverse=False)

g_frame = pd.DataFrame.from_dict(stock_growth_rates)


g_frame.growth_rate = g_frame.growth_rate.astype(float)


g_frame[1200:1220].plot.bar(y="growth_rate", x="name")

plt.show()
