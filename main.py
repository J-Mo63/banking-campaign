# Import libraries
from sklearn.exceptions import DataConversionWarning
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
import warnings
import math

# Ignore warnings for automatic data conversion
warnings.simplefilter(action='ignore', category=DataConversionWarning)

