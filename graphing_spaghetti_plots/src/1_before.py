import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

# creates dataframe from csv
df = pd.read_csv('../test-data.csv')

# inserts "x" into already existing dataframe
#df.insert(0, "x", range(1,10))
#df.head()
#print(df)

# Create a color palette
palette = plt.get_cmap('Set1')

# Create a figure and axes
# subplots(down, across)
fig, axes = plt.subplots(1, 1, figsize=(12, 12))

# Flatten the axes array for easy iteration
#axes = axes.flatten()

# Multiple line plots
for num, column in enumerate(df.drop('x', axis=1), start=1):
    ax = axes

    # Plot every group, but discrete (lower alpha)
    for v in df.drop('x', axis=1):
        ax.plot(
            df['x'],
            df[column],
            marker='',
            color=palette(num),
            linewidth=1.2,
            alpha=0.3
        )

    # Plot the line plot
    #ax.plot(
    #    df['x'],
    #    df[column],
    #    marker='o',
    #    color=palette(num),
    #    linewidth=2.4,
    #    alpha=0.9,
    #    label=column
    #)

    # Same limits for every chart
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 10)

    # move y-axis ticks to the right
    ax.yaxis.tick_right()

    # move y-axis labels to the right
    ax.tick_params(labelright=True)
    ax.tick_params(labelleft=False)

    # Tick management
#    if num in range(7):
#        ax.tick_params(labelbottom=False)
#    if num in [1, 4, 7, 10]:
#    if num not in [3, 6, 9, 12]:
#        ax.tick_params(labelleft=False)

    # Add title
    ax.set_title(
        "all together",
        loc='left',
        fontsize=12,
        fontweight=0,
        color="black"
    )

# General title
fig.suptitle(
    "This is a test:\nHow to create multiple graphs in Python",
    fontsize=20,
    fontweight=0,
    color='black',
    style='italic',
    y=1.02
)

# Adjust layout
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the graph
plt.show()
