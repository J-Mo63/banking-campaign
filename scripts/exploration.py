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


def event_plot(df, title, **kwargs):
    # Load in the values to a vertical event plot
    plt.eventplot(df, orientation=kwargs.get('orientation'))

    # Set the graph values and display
    plt.title(title)
    if kwargs.get('orientation') == 'vertical':
        plt.gca().axes.get_xaxis().set_visible(False)
    else:
        plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()


def pie_chart(df, title, **kwargs):
    # Get the values and counts from the data frame
    value_counts = df.value_counts()

    # Separate the labels from the counts
    sizes = []
    labels = []
    for i in range(len(value_counts)):
        labels.append(value_counts.index[i].replace('.', ' ').title())
        sizes.append(value_counts[i])

    # Check for slicing options in the kwargs
    labels = labels[kwargs.get('l_slice'):kwargs.get('r_slice')]
    sizes = sizes[kwargs.get('l_slice'):kwargs.get('r_slice')]

    # Apply the labels and sizes to the graph portions and display
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%.2f')
    ax1.axis('equal')
    plt.title(title)
    plt.show()


def bar_chart(df, title, **kwargs):
    # Get the values and counts from the data frame
    value_counts = df.value_counts()

    # Separate the labels from the counts
    sizes = []
    labels = []
    for i in range(len(value_counts)):
        labels.append(value_counts.index[i]
                      .replace('.', ' ').title() + ' (' + str(value_counts[i]) + ')')
        sizes.append(value_counts[i])

    # Check for slicing options in the kwargs
    labels = labels[kwargs.get('l_slice'):kwargs.get('r_slice')]
    sizes = sizes[kwargs.get('l_slice'):kwargs.get('r_slice')]

    # Apply the labels and sizes to the graph portions and display
    plt.bar(labels, sizes, align='center', alpha=1)
    plt.xticks(labels)
    plt.ylabel('Amount')
    plt.title(title)
    plt.show()


def mode(df):
    # Isolate the mode as a single value
    return df.mode().values[0]


def histogram(df, title, bins, display_range, **kwargs):
    plt.hist(df, density=1, bins=bins, range=display_range)
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'Amount')
    plt.title(title)
    plt.show()

