import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linear_r = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = linear_r.intercept + linear_r.slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label= 'Best Fit Line (1880-2050)')

    # Create second line of best fit
    df_rcnt = df[df['Year'] >= 2000]
    recent_r = linregress(df_rcnt['Year'], df_rcnt['CSIRO Adjusted Sea Level'])
    x_rcnt = pd.Series(range(2000, 2051))
    y_rcnt = recent_r.intercept + recent_r.slope * x_rcnt
    plt.plot(x_rcnt, y_rcnt, 'green', label= 'Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
