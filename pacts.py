import pandas as pd
import numpy as np

# Read in the data
df = pd.read_csv('acts_sections.csv', usecols=['ddl_case_id', 'act', 'criminal'])

# clean the data
df = df.dropna()

# Write the data to a csv
df.to_csv('acts_sections_cleaned.csv', index=False)
