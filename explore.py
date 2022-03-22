import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import seaborn as sns
import acquire

df = acquire.get_df()
df.head()

df.rename(columns= {'Unix Timestamp':'unix','Date':'date','Symobl':'symbol','Open':'open','High':'high','Low':'low','Close':'close','Volume':'volum'}, inplace = True)

df.date = pd.to_datetime(df.date)

df = df.set_index('date').sort_index()
df['day_of_week'] = df.index.day_name()

### Looks like there is enough data to use a percentage split
train_size = .70
n = df.shape[0]
test_start_index = round(train_size * n)

train = df[:test_start_index] # everything up (not including) to the test_start_index
test = df[test_start_index:] # everything from the test_start_index to the end

plt.plot(train.index, train.close)
plt.plot(test.index, test.close)

# With the massive hike in bitcoin in 2021, cutting earlier dates as outliers may be beneficial.