import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',float_precision='legacy')

    # Create scatter plot
    fig, ax = plt.subplots(1, figsize=(10,5))
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level',alpha=1,figsize=(10,5), ax=ax)

    # Create first line of best fit
    years_extended = np.arange(1880, 2051, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = [slope*i + intercept for i in years_extended]
    ax.plot(years_extended, line, label="Fitting Line", linewidth=1, color='green')

    # Create second line of best fit
    years_extended = np.arange(2000, 2051, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    line = [slope*i + intercept for i in years_extended]
    ax.plot(years_extended, line, label="Fitting Line", linewidth=1, color='red')

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_ylabel("Sea Level (inches)")
    ax.axis(xmin=1850)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()