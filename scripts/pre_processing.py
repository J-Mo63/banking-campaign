
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


def binarise_contact(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into one boolean column
    binarised_tel_cell_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_tel_cell_list.append(item[0])

    # Return the results as a list
    return binarised_tel_cell_list

def binarise_job(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into 11 columns
    binarised_admin_list = []
    binarised_blue_collar_list = []
    binarised_entrepreneur_list = []
    binarised_housemaid_list = []
    binarised_management_list = []
    binarised_retired_list = []
    binarised_self_employed_list = []
    binarised_services_list = []
    binarised_student_list = []
    binarised_technician_list = []
    binarised_unemployed_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_admin_list.append(item[0])
        binarised_blue_collar_list.append(item[1])
        binarised_entrepreneur_list.append(item[2])
        binarised_housemaid_list.append(item[3])
        binarised_management_list.append(item[4])
        binarised_retired_list.append(item[5])
        binarised_self_employed_list.append(item[6])
        binarised_services_list.append(item[7])
        binarised_student_list.append(item[8])
        binarised_technician_list.append(item[9])
        binarised_unemployed_list.append(item[10])

    # Return the results as a dictionary
    return {'admin': binarised_admin_list,
            'blue-collar': binarised_blue_collar_list,
            'entrepreneur': binarised_entrepreneur_list,
            'housemaid': binarised_housemaid_list,
            'management': binarised_management_list,
            'retired': binarised_retired_list,
            'self-employed': binarised_self_employed_list,
            'services': binarised_services_list,
            'student': binarised_student_list,
            'technician': binarised_technician_list,
            'unemployed': binarised_unemployed_list}

