import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20.48, 10.24))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.subplots_adjust(bottom=0.15)
    plt.xlim(1875, 2050)
    plt.ylim(0, 16)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(25))
    plt.xticks(rotation=45)
    plt.setp(ax.spines.values(), linewidth=1.5)
    plt.tick_params(axis='both', length=8, direction='out', width=1.5)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    regress = linregress(x, y)
    slope = regress.slope
    intercept = regress.intercept
    x_vals = np.linspace(1880.0, 2050.0, num=171)
    y_vals = np.array(slope * x_vals + intercept)
    plt.plot(x_vals, y_vals, color='firebrick', linewidth=2)


    # Create second line of best fit
    df_recent = df[(df['Year'] >= 2000) & (df['Year'] <= 2013)].copy()
    x_2 = df_recent['Year']
    y_2 = df_recent['CSIRO Adjusted Sea Level']
    regress_2 = linregress(x_2, y_2)
    slope_2 = regress_2.slope
    intercept_2 = regress_2.intercept
    x_2_vals = np.linspace(2000.0, 2050.0, num=51)
    y_2_vals = np.array(slope_2 * x_2_vals + intercept_2)
    plt.plot(x_2_vals, y_2_vals, color='red', linewidth=2)


    # Add labels and title
    plt.title('Rise in Sea Level', fontsize=24)
    plt.xlabel('Year', fontsize=20);
    plt.ylabel('Sea Level (inches)', fontsize=20);
    plt.axvline(x=2013, color='black', linestyle='--', label='2013')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

