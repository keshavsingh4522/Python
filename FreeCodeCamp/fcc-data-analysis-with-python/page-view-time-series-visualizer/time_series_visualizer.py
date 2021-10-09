import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
mask = (df['value'] <= df['value'].quantile(0.025)) | (df['value'] >= df['value'].quantile(0.975))
df = df.drop(df[mask].index).reset_index(drop=True)
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']
df = df.drop('date', axis = 1)

def draw_line_plot():
    # Draw line plot
    fig = df.plot.line(xlabel = 'Date', ylabel = 'Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', figsize=(12,5), legend = False, color = 'blue', rot=0, linewidth=0.85).figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dc = df.reset_index()

    # Draw bar plot
    dc = dc.groupby([dc['date'].dt.year.rename('year'), dc['date'].dt.month.rename('month')]).mean()
    dc = dc.unstack()
    fig = dc.plot(kind='bar', figsize=(10,7)).figure
    plt.legend([calendar.month_name[i] for i in range(1,13)], title = 'Months')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.ticklabel_format(style='plain', axis='y')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("num")

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2,figsize=(15,6))
    sns.boxplot(x="year", y="value", data=df_box,ax=ax[0])
    sns.boxplot(x="month", y="value", data=df_box,ax=ax[1])
    ax[0].set(ylabel='Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set(ylabel='Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
