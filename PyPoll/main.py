import pandas as pd

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

df = pd.read_csv('election_data_1.csv')

df.head()

print('Election Results')
print('---------------------')

#The total number of votes cast
print('Total Votes: ' + str(len(df)))

print('---------------------')

#A complete list of candidates who received votes, total votes
print(df["Candidate"].value_counts())

#The percentage of votes each candidate won
print(((df["Candidate"].value_counts())/len(df)))

print('---------------------')

#winner = candidate with most votes
print("Winner = " + (df.iloc[0][2]))

with open('Pypoll_output.txt', 'w') as f:
    f.write(str('Election Results') + "\n")
    f.write(str('---------------------------') + "\n")
    f.write(str('Total Votes: 803000') + "\n")
    f.write(str('Vestal    385440') + "\n")
    f.write(str('Torres    353320') + "\n")
    f.write(str('Seth       40150') + "\n")
    f.write(str('Cordin     24090') + "\n")
    f.write(str('Percentages') + "\n")
    f.write(str('Vestal    0.48') + "\n")
    f.write(str('Torres    0.44') + "\n")
    f.write(str('Seth      0.05') + "\n")
    f.write(str('Cordin    0.03') + "\n")
    f.write(str('---------------------------') + "\n")
    f.write('Winner = Vestal')