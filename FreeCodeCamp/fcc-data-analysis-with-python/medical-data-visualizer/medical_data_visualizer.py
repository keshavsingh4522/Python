import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def bmi(row):
  if row['weight'] / ((row['height'] / 100) ** 2) > 25:
    return 1
  else: 
    return 0

df['overweight'] = df.apply(bmi, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']).sort_values(['variable']).reset_index(drop=True)

    # Draw the catplot with 'sns.catplot()'
    df_cat = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")
    df_cat.set_ylabels('total')
    fig = df_cat.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask = (df['ap_lo'] > df['ap_hi']) | (df['height'] < df['height'].quantile(0.025)) | (df['height'] > df['height'].quantile(0.975)) | (df['weight'] < df['weight'].quantile(0.025)) | (df['weight'] > df['weight'].quantile(0.975))
    
    aa = df.drop(df[mask].index).reset_index(drop=True)

    # Calculate the correlation matrix
    corr = aa.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True,  ax=ax, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

