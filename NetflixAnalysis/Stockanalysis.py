#finding python stock analysis in netflix
#Netflix is a American subscription video on-demand over the top streaming services.
#python visualization
import numpy as np 
import pandas as pd 
#these 2 libraries are used to clean data and preprocessing datas.
import matplotlib.pyplot as plt
import seaborn as sns
#these 2 libraries are used for data visualization 
from datetime import datetime # used for date time format
table=pd.read_csv("NFLX.csv")
print("table")
print(" ")

sns.set(rc={'figure.figsize':(10,5)})
# here in our table it automatically index value is 0,1,2,...We have change the index column as Datetime
table['Date']=pd.to_datetime(table['Date'])
table=table.set_index('Date')
print(table)
#analysing how much volume of stock is traded
sns.lineplot(x=table.index,y=table['Volume'],label='Volume') #x axis is index value (2018,2019,...)
plt.title('Volume of Netflix stock V/S Time')
plt.show()
#next we heve to find the stock price range
table.plot(y=['High','Open','Close'], title='Netflix stock price  analysis')
plt.show()
##next we heve to find the stock price range based on Day, month and year by seperatly
#henece we are using group by concept


fig, (ax1,ax2,ax3) = plt.subplots(3,figsize=(20,10))
table.groupby(table.index.day).mean().plot(y='Volume',ax=ax1,xlabel='Day')
table.groupby(table.index.month).mean().plot(y='Volume',ax=ax2,xlabel='Month')
table.groupby(table.index.year).mean().plot(y='Volume', ax=ax3,xlabel='Year')
plt.show()

#Highest stock price top5
t=table.sort_values(by='High',ascending=False).head(5)
print(t['High'])
print(" ")
#lowest stock price top10
t1=table.sort_values(by='Low', ascending=False).head(15)
print(t1['Low'])

#graph plotting in High and Low
fig,axes=plt.subplots(nrows=1 ,ncols=2,figsize=(20,10))
fig.suptitle('High and Low stock prices graph',fontsize=20)
sns.lineplot(ax=axes[0],y=table['High'],x=table.index,color="Green")
sns.lineplot(ax=axes[1],y=table['Low'],x=table.index,color="Red")
plt.show()






