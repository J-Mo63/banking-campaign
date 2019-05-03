import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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

    # Separate the labels from the counts and create the lists
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

    # Check for custom sorting dictionary in kwargs
    if kwargs.get('sorting_criteria'):
        # Get the kwarg value for the sorting criteria
        sorting_criteria = kwargs.get('sorting_criteria')

        # Create lists of the pre-allocated size
        sizes = [None] * len(sorting_criteria)
        labels = [None] * len(sorting_criteria)
        for i in range(len(value_counts)):
            # Populate the lists by the sorting values
            sorting_value = sorting_criteria[value_counts.index[i]]
            labels[sorting_value] = value_counts.index[i].replace('.', ' ').title()
            sizes[sorting_value] = value_counts[i]
        # Remove null items from the list
        sizes = list(filter(None, sizes))
        labels = list(filter(None, labels))
    else:
        # Separate the labels from the counts and create the lists
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
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'Amount')
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


def box_plot(df, title):
    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.boxplot(df)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.show()


def scatter_plot(df_x, df_y, title, **kwargs):
    plt.scatter(df_x, df_y)

def histogram_3d(df_x, df_y, title, **kwargs):
    # This import registers the 3D projection, but is otherwise unused.
    import mpl_toolkits.mplot3d
    from sklearn import preprocessing

    # Binarise the values and get value counts
    bin_x = preprocessing.LabelBinarizer().fit_transform(df_x).flatten()
    bin_y = preprocessing.LabelBinarizer().fit_transform(df_y).flatten()
    x_names = df_x.value_counts()
    y_names = df_y.value_counts()

    # Calculate the number of bins by the area
    num_bins = len(x_names) * len(y_names)

    # Create the 3D subplot on a histogram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, x_edges, y_edges = np.histogram2d(bin_x, bin_y, bins=num_bins)

    # Construct arrays for the anchor positions of the bars
    x_pos, y_pos = np.meshgrid(x_edges[:-1] + 0.25, y_edges[:-1] + 0.25, indexing="ij")
    x_pos = x_pos.ravel()
    y_pos = y_pos.ravel()
    z_pos = 0

    # Construct arrays with the dimensions for the 16 bars
    dx = dy = 0.5 * np.ones_like(z_pos)
    dz = hist.ravel()
    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, zsort='average')

    # Get the unique values for each axis
    x_vals = x_names.index.values
    y_vals = y_names.index.values

    # Create value strings that incorporate counts
    for i in range(len(x_vals)):
        x_vals[i] = x_vals[i] + ' (' + str(x_names.values[i]) + ')'

    for i in range(len(y_vals)):
        y_vals[i] = y_vals[i] + ' (' + str(y_names.values[i]) + ')'

    # Set the axis ticks to the value strings
    plt.xticks(range(len(x_vals)), x_vals, size='small')
    plt.yticks(range(len(y_vals)), y_vals, size='small')

    # Setup and display the plot
    plt.title(title)
    plt.xlabel(kwargs.get('xlabel') if kwargs.get('xlabel') else 'x value')
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'y value')
    plt.show()
