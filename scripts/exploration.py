import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def correlation_matrix(df, title):
    # Remove the row id from the data frame
    df = df.drop('row id', 1)

    # Set up the matrix plot and display
    f, ax = plt.subplots(figsize=(20, 16))
    corr = df.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax).set_title(title)
    plt.show()


def event_plot(df, title):
    # Load in the values to a vertical event plot
    plt.eventplot(df, orientation='vertical')

    # Set the graph values and display
    plt.title(title)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.show()

    plt.show()
