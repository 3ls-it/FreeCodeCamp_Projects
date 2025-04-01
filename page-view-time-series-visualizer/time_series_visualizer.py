#!/data/data/com.termux/files/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
#print(df)

# Clean data
dates_less = df['value'] >= df['value'].quantile(0.025)
dates_more = df['value'] <= df['value'].quantile(0.975)
df = df[dates_less & dates_more]
#print(df)


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()

    fig, axes = plt.subplots(figsize=(32,10))
    axes = sns.lineplot(data=df_line, x='date', y='value')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# End draw_line_plot() 


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
# End draw_box_plot() 

lnplt = draw_line_plot()
print(lnplt)
