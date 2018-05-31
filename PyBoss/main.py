import pandas as pd

df = pd.read_csv('employee_data1.csv')

df.head()

# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into MM/DD/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.



us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#creating new column (state_abrev) by using State column and abbrev dict
df['state_abbrev'] = df['State'].map(us_state_abbrev)

name_list = df['Name'].str.split(' ')

print(name_list)



df["first_name"] = [x[0] for x in name_list]

df["last_name"] = [x[-1] for x in name_list]

df.head()

"***-**-" + df.iloc[0]["SSN"][-4:]

def masked_ssn(ssn_str):
    return "***-**-" +ssn_str[-4:]

df['masked_ssn'] = df['SSN'].map(masked_ssn)

column_order = ['Emp ID', 'first_name', 'last_name', 'DOB', 'masked_ssn', 'state_abbrev']
#listing columns in the order that you want

df = df[column_order]

df.head()

#df1 = df.copy()
#used to make different copy of dataframe so you can edit without messing with original data

df.DOB

#turn DOB column data from ojects into date time and then reordering to MM/DD/YYYY
df['DOB'] = pd.to_datetime(df.DOB).dt.strftime('%m-%d-%Y')

df.head()