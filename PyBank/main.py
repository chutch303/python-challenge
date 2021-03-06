import pandas as pd

df = pd.read_csv('budget_data_2.csv')

df.head()

print('Financial Analysis')
print('---------------------------')

df['Date'].value_counts()
#all values in data column are unique

#The total number of months included in the dataset
total_months = 'Total Months: ' + str(len(df))
print(total_months)

#The total amount of revenue gained over the entire period
print('Total Revenue: ' + str(df['Revenue'].sum()))

#The average change in revenue between months over the entire period
df['revenue_change'] = df['Revenue'].diff()
df.head()

print('Average Revenue Change: ' + str(df['revenue_change'].mean()))

#The greatest increase in revenue over the entire period
print('Greatest Increase in Revenue: ', + df['revenue_change'].max())

#find date with the greatest increase in revenue
df.loc[df['revenue_change'] == 1645140.0, 'Date']
print(df["Date"][66])

#The greatest decrease in revenue over the entire period
print('Greatest Decrease in Revenue: '+ str(df['revenue_change'].min()))

#find date with the greatest decrease in revenue
df.loc[df['revenue_change'] == -1947745.0, 'Date']
print(df["Date"][65])

with open('PyBank_output.txt', 'w') as f:
    f.write(str('Financial Analysis') + "\n")
    f.write(str('---------------------------') + "\n")
    f.write(str('Total Months: 86') + "\n")
    f.write(str('Total Revenue: 36973911') + "\n")
    f.write(str('Average Revenue Change: -5955.305882352941') + "\n")
    f.write(str('Greatest Increase in Revenue:  1645140.0 in Jul-2014') + "\n")
    f.write('Greatest Decrease in Revenue: -1947745.0 in Jun-2014')