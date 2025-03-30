import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Add 'overweight' column, initialise to 0 
df['overweight'] = 0
# height is in cm, so divide  by 100  
bmi = df['weight'] / ((df['height']/100) ** 2)
# if bmi is > 25, set overweight to 1 
df.loc[bmi > 25, 'overweight'] = 1
#print(df['overweight'])

# 3
# Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0.
# If the value is more than 1, set the value to 1.
gluc = df['gluc']
df.loc[gluc == 1, 'gluc'] = 0
df.loc[gluc > 1, 'gluc'] = 1
chol = df['cholesterol']
df.loc[chol == 1, 'cholesterol'] = 0
df.loc[chol > 1, 'cholesterol'] = 1


# 4
def draw_cat_plot():
    # 5
    # Create a DataFrame for the cat plot using pd.melt with values from
    # cholesterol, gluc, smoke, alco, active, and overweight
    # in the df_cat variable.
    df_cat = df.melt(id_vars='cardio',
                     value_vars=['active', 'alco', 'cardio', 'cholesterol',
                                 'gluc', 'overweight', 'smoke'])
    df_cat['total'] = 1

    # 6
    # Group and reformat the data in df_cat to split it by cardio.
    #Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # 7
    # Convert the data into long format and create a chart that shows
    # the value counts of the categorical features using the following method
    # provided by the seaborn library import: sns.catplot().
    cat_plot = sns.catplot(x='variable', y='total', hue='value', data=df_cat,
                           col='cardio', kind='bar').fig

    # 8
    # Get the figure for the output and store it in the fig variable.
    fig = cat_plot

    # 9
    # Do not modify the next two lines.
    fig.savefig('catplot.png')
    return fig
# End draw_cat_plot() 


# 10
def draw_heat_map():
    # 11 
    #Clean the data in the df_heat variable by filtering out the following
    # patient segments that represent incorrect data:
    #
    # -diastolic pressure is higher than systolic
    #(Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    diastolic = df['ap_lo'] <= df['ap_hi']
    # -height is less than the 2.5th percentile
    # (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    height_less = df['height'] >= df['height'].quantile(0.025)
    # -height is more than the 97.5th percentile
    height_more = df['height'] <= df['height'].quantile(0.975)
    # -weight is less than the 2.5th percentile
    weight_less = df['weight'] >= df['weight'].quantile(0.025)
    # -weight is more than the 97.5th percentile
    weight_more = df['weight'] <= df['weight'].quantile(0.975)
    df_heat = df[diastolic & height_less & height_more & weight_less & weight_more]

    # 12 
    # Calculate the correlation matrix and store it in the corr variable. 
    corr = df_heat.corr(method='pearson')

    # 13 
    # Generate a mask for the upper triangle and store it in the mask variable. 
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14 
    # Set up the matplotlib figure.
    fig, axes = plt.subplots(figsize=(11,9))

    # 15 
    # Plot the correlation matrix using the method provided by
    # the seaborn library import: sns.heatmap().
    axes = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5,
                       center=0.0, vmax=0.25, vmin=-0.1, square=True,
                       cbar_kws={"shrink":0.5})

    # 16
    # Do not modify the next two lines.
    fig.savefig('heatmap.png')
    return fig
# End draw_heat_map() 

