# Basic Libraries for Quantitative Finance
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

style.use(ggplot)

# Initalize basic variable. 
start = dt.datetime(2009, 1, 1)
end = dt.datetime(2019, 12, 31)

# Initalize a dataframe from a specific source during start and end. 
df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head())

# I. BASIC DATAFRAME MANIPULATION

# Convert the dataframe to a csv file, then use pandas to manipulate it. 
df.to_csv('tsla')
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Basic plotting
df.plot()
plt.show()

# Or we can choose to plot only one variable.
df['Adj Close'].plot()

# Creating data columns through calculation. 
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df.dropna(inplace=True)
# inplace = true allows us to manipulate the df variable directly. 


