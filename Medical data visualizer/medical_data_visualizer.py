import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = (df['weight'] / (df['height'] / 100)**2) >25
df['overweight'] = bmi.replace({False: 0, True: 1})

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'] )
    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio'], as_index=False).value_counts())
    df_cat.rename(columns={'count':'total'}, inplace=True)
    df_cat.sort_values(by=['variable'], inplace=True)

    # Draw the catplot with 'sns.catplot()'
    cplot = sns.catplot(df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')

    # Get the figure for the output
    fig = cplot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & ((df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))) & ((df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)))]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 7))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, square=True, mask=mask, annot=True, fmt='0.1f', linewidths=0.5, vmax=0.25, center=0, cbar_kws={'shrink': 0.5}, annot_kws={'fontsize': 7})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
