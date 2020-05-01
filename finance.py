#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Open and read the csv file containing transaction data
#and store the data into a variable called 'fin_data'
fin_data = pd.read_csv('285866_spend_20200430.csv')

#These next two lines create two lists, the first being
#every purchase from the pandas dataframe variable 'fin_data',
#more specifically the "Amount" column
purchases = fin_data['Amount'].tolist()
balance = [5.61]

#This for loop takes every purchase and generates the balance 
#at the time of the transaction by subtracting the balance 
#by the purchase amount. We have to subtract because the purchase
#amount is given as a negative, so two negatives create a positive
#thereby giving the balance by adding the purchase back into the balance
for i in range(len(purchases)-1):
	balance.append(round(balance[i] - purchases[i], 2))

#Here I take the dataframe 'fin_data' and add the 'Balance'
#column to the dataframe. I then reverse the order of the dataframe
#and store it in a variable called 'fin_data_reversed' which I then
#write to a csv file.
fin_data['Balance'] = balance
fin_data_reversed = fin_data.iloc[::-1]
fin_data_reversed.to_csv('Aspiration_Finance_Data_Reversed.csv')

#I commented these out because they weren't necessary anymore, test prints
# print(fin_data_reversed.head())
# print(fin_data_reversed.tail())


#And finally to plotting out the data with the values in order now ascending by date.
#These two first lines create the x and y values and then the next three lines
#plot and label the data. The last line actually displays the plot
x = fin_data_reversed.Date
y = fin_data_reversed.Balance

plt.scatter(x,y)
plt.ylabel('Balance')
plt.show
plt.savefig('Balance.png')