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


def pie_chart(df, title):
    # Get the values and counts from the data frame
    value_counts = df.value_counts()

    # Separate the labels from the counts
    sizes = []
    labels = []
    for i in range(len(value_counts)):
        labels.append(value_counts.index[i].replace('.', ' ').title())
        sizes.append(value_counts[i])

    # Apply the labels and sizes to the graph portions and display
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%.2f')
    ax1.axis('equal')
    plt.title(title)
    plt.show()
