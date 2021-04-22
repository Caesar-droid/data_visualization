import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename='data/death_valley_2018_simple.csv'
with open (filename) as f:
    reader=csv.reader(f)
    header_row =next(reader)
    
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    
    #Get dates,high and low temperatures from this file.
    dates, highs, lows =[],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high =int(row[4])
            low=int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
    #ploting the high and low temperature.
    plt.style.use('seaborn')
    fig,ax= plt.subplots()
    ax.plot(dates,highs,c='red',alpha=0.5)
    ax.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    
    #format plot.
    plt.title('Daily highs and lows temperatures-2018\n Death Valley,CA',fontsize=20)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    
    plt.show()
    
        
        