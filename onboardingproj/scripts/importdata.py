import pandas as pd
from django.contrib.auth.models import User
from onboardingapp.models import ACCIDENT

# Read CSV file into a DataFrame
csv_file_path = "D:\DataVizPE3\ACCIDENT.csv"
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    # Create or get the ACCIDENT instance
    accident = ACCIDENT(
        ACCIDENT_NO = row['ACCIDENT_NO'],
        ACCIDENT_DATE = row['ACCIDENT_DATE'],
        DAY_WEEK_DESC = row['DAY_WEEK_DESC'],
        NODE_ID = row['NODE_ID'],
        SEVERITY = row['SEVERITY']
    )
    accident.save()


print("CSV data has been loaded into the Django database.")