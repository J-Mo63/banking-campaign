import pandas as pd
from sklearn import preprocessing


def bin_equi_width(df, bins):
    # Cut up the data by width
    binned_equi_width = pd.cut(df, bins)

    # Format and listify equi-width list
    bin_equi_width_list = []
    for i in range(binned_equi_width.size):
        left_item = "{0:.2f}".format(binned_equi_width[i].left)
        right_item = "{0:.2f}".format(binned_equi_width[i].right)
        bin_equi_width_list.append([left_item, right_item])

    # Return the results as a list
    return bin_equi_width_list


def bin_equi_depth(df, bins):
    # Cut up the data by width & depth
    binned_equi_depth = pd.qcut(df, bins, duplicates='drop')

    # Format and listify equi-depth list
    bin_equi_depth_list = []
    for i in range(binned_equi_depth.size):
        left_item = "{0:.2f}".format(binned_equi_depth[i].left)
        right_item = "{0:.2f}".format(binned_equi_depth[i].right)
        bin_equi_depth_list.append([left_item, right_item])

    # Return the results as a list
    return bin_equi_depth_list


def normalise_min_max(df):
    # Make the data frame two dimensional
    df = df.values.reshape(-1, 1)

    # Fit the min-max normalised list
    min_max_scaled = preprocessing.MinMaxScaler().fit_transform(df)

    # Return the results as a list
    return pd.DataFrame(min_max_scaled).values.flatten()


def normalise_z_score(df):
    # Make the data frame two dimensional
    df = df.values.reshape(-1, 1)

    # Fit the min-max normalised list
    z_score_scaled = preprocessing.StandardScaler().fit_transform(df)

    # Return the results as a list
    return pd.DataFrame(z_score_scaled).values.flatten()


def discretise_age(df):
    # Isolate the values from the data frame
    df = df.values

    # Discretise the age into categories
    discretised_list = []
    for i in range(df.size):
        item = df[i]
        if item < 45:
            discretised_list.append('Adult')
        elif item <= 65:
            discretised_list.append('Mid-age')
        elif item > 65:
            discretised_list.append('Old-age')
        else:
            discretised_list.append('NaN')

    # Return the results as a list
    return discretised_list


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


def binarise_poutcome(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into three columns
    binarised_failure_list = []
    binarised_nonexistent_list = []
    binarised_success_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_failure_list.append(item[0])
        binarised_nonexistent_list.append(item[1])
        binarised_success_list.append(item[2])

    # Return the results as a dictionary
    return {'failure': binarised_failure_list,
            'nonexistent': binarised_nonexistent_list,
            'success': binarised_success_list}


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


def binarise_y_n(df):
    # Isolate the values from the data frame
    df = df.values

    # Format the binarised items into one boolean column
    binarised_y_n_list = []
    for i in range(len(df)):
        item = df[i]
        if item == 'yes':
            binarised_y_n_list.append(1)
        else:
            binarised_y_n_list.append(0)

    # Return the results as a list
    return binarised_y_n_list


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


def binarise_day(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into 5 columns
    binarised_monday_list = []
    binarised_tuesday_list = []
    binarised_wednesday_list = []
    binarised_thursday_list = []
    binarised_friday_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_friday_list.append(item[0])
        binarised_monday_list.append(item[1])
        binarised_thursday_list.append(item[2])
        binarised_tuesday_list.append(item[3])
        binarised_wednesday_list.append(item[4])

    # Return the results as a dictionary
    return {'monday': binarised_monday_list,
            'tuesday': binarised_tuesday_list,
            'wednesday': binarised_wednesday_list,
            'thursday': binarised_thursday_list,
            'friday': binarised_friday_list}


def binarise_month(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into 10 columns
    binarised_march_list = []
    binarised_april_list = []
    binarised_may_list = []
    binarised_june_list = []
    binarised_july_list = []
    binarised_august_list = []
    binarised_september_list = []
    binarised_october_list = []
    binarised_november_list = []
    binarised_december_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_april_list.append(item[0])
        binarised_august_list.append(item[1])
        binarised_december_list.append(item[2])
        binarised_july_list.append(item[3])
        binarised_june_list.append(item[4])
        binarised_march_list.append(item[5])
        binarised_may_list.append(item[6])
        binarised_november_list.append(item[7])
        binarised_october_list.append(item[8])
        binarised_september_list.append(item[9])

    # Return the results as a dictionary
    return {'march': binarised_march_list,
            'april': binarised_april_list,
            'may': binarised_may_list,
            'june': binarised_june_list,
            'july': binarised_july_list,
            'august': binarised_august_list,
            'september': binarised_september_list,
            'october': binarised_october_list,
            'november': binarised_november_list,
            'december': binarised_december_list}


def write_to_xls(df):
    # Write and save the data to an excel document
    writer = pd.ExcelWriter('output.xls', engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
