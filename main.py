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

# Calculate the optimal number of bins for normal distribution using Sturges' rule
sturges_rule_bins = math.log2(len(df))+1

# Perform binning for 'campaign'
binned_equi_width_campaign = prep.bin_equi_width(df['campaign'], sturges_rule_bins)
binned_equi_depth_campaign = prep.bin_equi_depth(df['campaign'], 7)

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
    'campaign.equi-width': binned_equi_width_campaign,
    'campaign.equi-depth': binned_equi_depth_campaign,
    'duration.min-max': normalised_min_max_duration,
    'duration.z-score': normalised_z_score_duration,
    'age.discretised': discretised_age,
    'marital.divorced': binarised_marital['divorced'],
    'marital.married': binarised_marital['married'],
    'marital.single': binarised_marital['single']
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

# Display a correlation matrix for the entire data set
# exp.correlation_matrix(concatenated_df, 'Banking Campaign - Correlation Matrix')

# Display an event plot and bar chart for age
# exp.event_plot(df['age'], 'Age', orientation='vertical')
# exp.bar_chart(output_df['age.discretised'], 'Age Groups')

# Display a pie chart for job
# exp.pie_chart(df['job'], 'Job')

# Display a pie chart for marital
# exp.pie_chart(df['marital'], 'Marital Status')

# Display a pie chart for education
# exp.pie_chart(df['education'], 'Education Level')

# Display a pie chart for contact
# exp.pie_chart(df['contact'], 'Medium of Contact')

# Display a pie chart for y
# exp.pie_chart(df['y'], 'Subscription to Term Deposit')

# Display a bar chart for default
# exp.bar_chart(df['default'], 'Defaulted')

# Display a pie and bar chart for housing
# exp.pie_chart(df['housing'], 'Housing')
# exp.bar_chart(df['housing'], 'Housing')

# Display a bar chart for loan
# exp.bar_chart(df['loan'], 'Loan')

# Display a bar chart for poutcome
exp.bar_chart(df['poutcome'], 'Previous Outcome')
exp.pie_chart(df['poutcome'], 'Previous Outcome', l_slice=1)
# Display the mode of pdays
# print('Mode of column \'pdays\': ' + str(exp.mode(df['pdays'])))

# Display the mode of previous
# exp.bar_chart(df.applymap(str)['previous'], 'Pre-Campaign Contacts')
# print('Mode of column \'previous\': ' + str(exp.mode(df['previous'])))