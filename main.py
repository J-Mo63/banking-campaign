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


# Perform binarisation for 'marital'
binarised_marital = prep.binarise_marital(df['marital'])


# Create a combined data frame of pre-processed data for analysis
processed_df = pd.DataFrame({
    'Married': binarised_marital['married'],
    'Single': binarised_marital['single'],
    'Divorced': binarised_marital['divorced'],
})

# Combine the original data to the processed data for analysis
concatenated_df = pd.concat([df, processed_df], axis=1, sort=False)

# Display a correlation matrix
exp.correlation_matrix(concatenated_df)
