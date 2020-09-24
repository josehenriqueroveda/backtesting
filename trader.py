import backtrader as bt
import datetime
from matplotlib.dates import (HOURS_PER_DAY, MIN_PER_HOUR, SEC_PER_MIN,
                              MONTHS_PER_YEAR, DAYS_PER_WEEK,
                              SEC_PER_HOUR, SEC_PER_DAY,
                              num2date, rrulewrapper, YearLocator,
                              MicrosecondLocator)
from strategies import TestStrategy


cerebro = bt.Cerebro()

cerebro.broker.set_cash(1000000)

data = bt.feeds.YahooFinanceCSVData(dataname='AMZN.csv',
                                    fromdate=datetime.datetime(2020, 1, 1),
                                    todate=datetime.datetime(2020, 9, 23),
                                    reverse=False)
cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)
cerebro.addsizer(bt.sizers.FixedSize, stake=300)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
