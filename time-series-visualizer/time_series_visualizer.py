#!/data/data/com.termux/files/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
#print(df)

# Clean the data by filtering out days when the page views were in the
# top 2.5% of the dataset or bottom 2.5% of the dataset.
dates_less = df['value'] >= df['value'].quantile(0.025)
dates_more = df['value'] <= df['value'].quantile(0.975)
df = df[dates_less & dates_more]


def draw_line_plot():
    # Create a draw_line_plot function that uses Matplotlib to
    # draw a line chart similar to "examples/Figure_1.png".
    df_line = df.copy(deep=True)
    df_line = df_line.rename(columns={'value': 'Page Views'})
    df_line = df_line.rename_axis(index={'date': 'Date'})

    # The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
    # The label on the x axis should be Date and the label on the y axis
    # should be Page Views.
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
    # Create a draw_bar_plot function that draws a bar chart similar
    # to "examples/Figure_2.png"
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()

    # It should show average daily page views for each month grouped by year.
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack(level='month')
    df_bar = df_bar[['January', 'February', 'March', 'April', 'May',
                     'June', 'July', 'August', 'September', 'October',
                     'November', 'December']]
    fig = df_bar.plot.bar(figsize=(15.14,13.30)).figure

    # The legend should show month labels and have a title of Months.
    plt.legend(title='Months', prop={'size': 20}, title_fontsize=20);

    # On the chart, the label on the x axis should be Years and the
    # label on the y axis should be Average Page Views.
    plt.xlabel('Years', fontsize=20);
    plt.ylabel('Average Page Views', fontsize=20);
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
    fig, axes = plt.subplots(1, 2, figsize=(28.80, 10.80))

    sns.boxplot(data=df_box, ax=axes[0], x='year', y='value')
    axes[0].set_title('Year-wise Box Plot (Trend)', size=16)
    axes[0].set_xlabel('Year', size=16)
    axes[0].set_ylabel('Page Views', size=16)

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, ax=axes[1], order=months, x='month', y='value')
    axes[1].set_title('Month-wise Box Plot (Seasonality)', size=16)
    axes[1].set_xlabel('Month', size=16)
    axes[1].set_ylabel('Page Views', size=16)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
# End draw_box_plot() 

draw_box_plot()
