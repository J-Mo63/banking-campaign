# Import libraries
from sklearn.exceptions import DataConversionWarning
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
import warnings
import math

# Ignore warnings for automatic data conversion
warnings.simplefilter(action='ignore', category=DataConversionWarning)

# Import the data and read from Excel file
df = pd.read_csv('banking_campaign.csv')

# Calculate the optimal number of bins for normal distribution using Sturge's rule
sturges_rule_bins = math.log2(len(df))+1

# Perform binning for 'campaign'
binned_equi_width_campaign = prep.bin_equi_width(df['campaign'], sturges_rule_bins)
binned_equi_depth_campaign = prep.bin_equi_depth(df['campaign'], 4)

# Perform normalisation for 'duration'
normalised_min_max_duration = prep.normalise_min_max(df['duration'])
normalised_z_score_duration = prep.normalise_z_score(df['duration'])

# Perform discretisation for 'age'
discretised_age = prep.discretise_age(df['age'])

# Perform binarisation for 'marital'
binarised_marital = prep.binarise_marital(df['marital'])

# Perform binarisation for 'contact'
binarised_contact = prep.binarise_contact(df['contact'])

# Perform binarisation for 'job'
binarised_job = prep.binarise_job(df['job'])

# Perform binarisation for 'housing'
binarised_housing = prep.binarise_y_n(df['housing'])

# Perform binarisation for 'loan'
binarised_loan = prep.binarise_y_n(df['loan'])

# Perform binarisation for 'poutcome'
binarised_poutcome = prep.binarise_poutcome(df['poutcome'])

# Perform binarisation for 'day_of_week'
binarised_day = prep.binarise_day(df['day_of_week'])

# Perform binarisation for 'month'
binarised_month = prep.binarise_month(df['month'])

# Perform binarisation for 'y'
binarised_y = prep.binarise_y_n(df['y'])

# Create a combined data frame for output
output_df = pd.DataFrame({
    'Equi-Width': binned_equi_width_campaign,
    'Equi-Depth': binned_equi_depth_campaign,
    'Min-Max': normalised_min_max_duration,
    'Z-Score': normalised_z_score_duration,
    'Discretised': discretised_age,
})

# Merge and write the data frame to an excel file
prep.write_to_xls(pd.concat([df, output_df], axis=1, sort=False))

# Create a combined data frame of pre-processed data for analysis
processed_df = pd.DataFrame({
    'Married': binarised_marital['married'],
    'Single': binarised_marital['single'],
    'Divorced': binarised_marital['divorced'],
    'Admin': binarised_job['admin'],
    'Blue-Collar': binarised_job['blue-collar'],
    'Entrepreneur': binarised_job['entrepreneur'],
    'Housemaid': binarised_job['housemaid'],
    'Management': binarised_job['management'],
    'Retired': binarised_job['retired'],
    'Self-Employed': binarised_job['self-employed'],
    'Services': binarised_job['services'],
    'Student': binarised_job['student'],
    'Technician': binarised_job['technician'],
    'Unemployed': binarised_job['unemployed'],
    'Telephone': binarised_contact,
    'Housing': binarised_housing,
    'Loan': binarised_loan,
    'Previous Success': binarised_poutcome['success'],
    'Previous Failure': binarised_poutcome['failure'],
    'No Previous Contact': binarised_poutcome['nonexistent'],
    'Mon': binarised_day['monday'],
    'Tue': binarised_day['tuesday'],
    'Wed': binarised_day['wednesday'],
    'Thu': binarised_day['thursday'],
    'Fri': binarised_day['friday'],
    'Mar': binarised_month['march'],
    'Apr': binarised_month['april'],
    'May': binarised_month['may'],
    'Jun': binarised_month['june'],
    'Jul': binarised_month['july'],
    'Aug': binarised_month['august'],
    'Sep': binarised_month['september'],
    'Oct': binarised_month['october'],
    'Nov': binarised_month['november'],
    'Dec': binarised_month['december'],
    'Y': binarised_y
})

# Combine the original data to the processed data for analysis
concatenated_df = pd.concat([df, processed_df], axis=1, sort=False)

# Display a correlation matrix
exp.correlation_matrix(concatenated_df)
