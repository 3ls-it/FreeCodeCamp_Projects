#!/data/data/com.termux/files/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
#print(df)

# Clean data
dates_less = df['value'] >= df['value'].quantile(0.025)
dates_more = df['value'] <= df['value'].quantile(0.975)
df = df[dates_less & dates_more]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy(deep=True)
    df_line = df_line.rename(columns={'value': 'Page Views'})
    df_line = df_line.rename_axis(index={'date': 'Date'})

    fig, axes = plt.subplots(figsize=(32,10))
    axes.plot(df_line.index, df_line['Page Views'], color='firebrick', linewidth=3)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=24)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Page Views', fontsize=20)
    plt.setp(axes.spines.values(), linewidth=1.5)
    plt.tick_params(axis='both', length=8, direction='out', width=1.5)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# End draw_line_plot() 


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar = df_bar.rename(columns={'value': 'Page Views'})
    df_bar = df_bar.rename_axis(index={'date': 'Date'})

    # Draw bar plot
    fig, axes = plt.subplots(figsize=(15.14, 13.30))
    axes.plot(df_bar['Page Views'])
    plt.title('', fontsize=24)
    plt.xlabel('Years', fontsize=20)
    plt.ylabel('Average Page Views', fontsize=20)
    plt.setp(axes.spines.values(), linewidth=1.5)
    plt.tick_params(axis='both', length=8, direction='out', width=1.5)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
# End draw_bar_plot() 


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(28.80, 10.80))
    axes.plot(df_box['year'])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
# End draw_box_plot() 

draw_bar_plot()
