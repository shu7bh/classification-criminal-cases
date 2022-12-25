import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('cases/cases_2014.csv', usecols=['ddl_case_id','year', 'judge_position', 'female_defendant', 'female_petitioner', 'female_adv_def', 'female_adv_pet','type_name', 'purpose_name', 'disp_name'])

df = df.dropna()
df = df.drop_duplicates()

df = df[df['female_defendant'] != -9999]
df = df[df['female_petitioner'] != -9999]
df = df[df['female_adv_def'] != -9999]
df = df[df['female_adv_pet'] != -9999]
df = df[df['female_defendant'] != -9998]
df = df[df['female_petitioner'] != -9998]
df = df[df['female_adv_def'] != -9998]
df = df[df['female_adv_pet'] != -9998]
df = df[df['female_defendant'] != '-9999 missing name']
df = df[df['female_petitioner'] != '-9999 missing name']
df = df[df['female_adv_def'] != '-9999 missing name']
df = df[df['female_adv_pet'] != '-9999 missing name']
df = df[df['female_defendant'] != '-9998 unclear']
df = df[df['female_petitioner'] != '-9998 unclear']
df = df[df['female_adv_def'] != '-9998 unclear']
df = df[df['female_adv_pet'] != '-9998 unclear']

df = df.replace('0 male', 0)
df = df.replace('1 female', 1)

df.to_csv('cases/cases_2014_cleaned.csv', index=False)