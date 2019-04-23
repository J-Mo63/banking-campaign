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


    # Display the matrix
    plt.show()
