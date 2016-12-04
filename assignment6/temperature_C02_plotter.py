import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


_data_dir = 'assignment6_files/'


def _plot_me(func,func_id):
    """
        Helper funcion
    """
    
    def ploting_me_temp(month,start_time,end_time,y_min,y_max):
        fig = func(month,start_time,end_time,y_min,y_max)
        plt.show()

    def ploting_me_co2(start_time,end_time,y_min,y_max):    
        fig = func(start_time,end_time,y_min,y_max)
        plt.show()
    def ploting_me_co2C(min_co2,max_co2,year = 2013):
        fig = func(min_co2,max_co2,year)
        plt.show() 

    if(func_id == 'temp'):
        ploting_me_temp.data = func.data
        return ploting_me_temp    
    elif(func_id == 'co2'):
        ploting_me_co2.data = func.data
        return ploting_me_co2
    elif(func_id == 'co2C'):
        ploting_me_co2C.data = func.data
        return ploting_me_co2C
    else:
        assert False 
       


def plot_co2_country(min_co2,max_co2,year = '2013'):
    """
        Plots co2 per country
        Args:
            min_co2: min co2 for country to be part of plot
            max_co2: max co2 for counry to be part of plot
            year: year to plot for, default 2013
    """
    data = plot_co2_country.data
    co2 = data[year]
    selector = (co2 <= max_co2) & (co2 >= min_co2)
    country = data["Country Name"][selector].values
    y_pos = np.arange(len(country))
    co2 = co2[selector].values
    fig = plt.figure()
    ax = fig.add_subplot(111) 
    ax.bar(y_pos,co2)
    plt.xticks(y_pos,country)
    plt.title("CO2  per country")
    plt.xlabel("Countrys")
    plt.ylabel("CO2 ") 


plot_co2_country.data = pd.read_csv(_data_dir + 'CO2_by_country.csv')
    


def plot_temperature(month,start_time, end_time,y_min,y_max):
    """
        Plots the temperatur
        Args:
            month: the month to plot temperature from
            start_time: year to start ploting
            end_time: year to end ploting
            y_min: minimum value for temperatur so show in plot
            y_max: maximum value for temperatur so show in plot
    """
    data = plot_temperature.data
    year = data["Year"]
    selector = (year <= end_time) & (year >= start_time)
    year = year[selector].values
    temp = data[month][selector].values
    fig = plt.figure()
    ax = fig.add_subplot(111) 
    ax.plot(year,temp)
    ax.set_ylim(y_min,y_max)
    plt.title("Average temperature per year for " + month)
    plt.xlabel("Years")
    plt.ylabel("Average temperature ") 


#Make the  data from file available to function plot_temperature
plot_temperature.data = pd.read_csv(_data_dir + 'temperature.csv')

    

def plot_CO2(start_time, end_time,y_min,y_max):
    """
        Plots CO2
        Args:
            start_time: year to start ploting from
            end_time: year to end ploting from
            y_min: min value of co2 to show
            y_max: max value of co2 to show
    """
    data = plot_CO2.data
    year = data["Year"]
    selector = (year <= end_time) & (year >= start_time)
    year = year[selector].values
    co2 = data['Carbon'][selector].values
    fig = plt.figure()
    ax = fig.add_subplot(111) 
    ax.plot(year,co2)
    ax.set_ylim(y_min,y_max)
    plt.title("CO2  per year")
    plt.xlabel("Years")
    plt.ylabel("CO2 ") 

plot_CO2.data = pd.read_csv(_data_dir+ 'co2.csv')





if __name__ == '__main__':

    plot_temperature = _plot_me(plot_temperature,'temp')
    plot_CO2 = _plot_me(plot_CO2,'co2')
    plot_co2_country = _plot_me(plot_co2_country,'co2C')

    plot_co2_country(15.0,20.0,'2013')
    plot_temperature("May",1816,1900,0,30)
    plot_CO2(1816,1900,0,1000)  
