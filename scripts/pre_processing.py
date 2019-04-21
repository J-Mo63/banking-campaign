
def binarise_marital(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into three columns
    binarised_married_list = []
    binarised_single_list = []
    binarised_divorced_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_divorced_list.append(item[0])
        binarised_married_list.append(item[1])
        binarised_single_list.append(item[2])

    # Return the results as a dictionary
    return {'married': binarised_married_list,
            'single': binarised_single_list,
            'divorced': binarised_divorced_list}

