#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv #this function means to open a toolbox full of tools that help you work with lists
#These lists are called CSV files, and they are made up of a lot of little pieces of information
#that are separated by commas.

#When you "import csv," you get to use these special tools that let you open up a CSV file,
#take a look at the information inside it, and even change the information or add more to it.
#Useful for when working with lots of information at once e.g making a chart out of it.



def read_data(): ##This function is to read the spreadsheet into Python.
    data = []
    
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    
    print(data)
    return data

#This function takes in the read function and stores it as a variable/data.
#The data from the spreadsheet is then copied row by row into a list.

def run():
    data = read_data() #data stores the output of read_data function.
    
    sales = [] #empty list created called sales
    for row in data: #for loop created ready to scan through spread sheet and append into the sales list.
        sale = int(row['sales']) #sale is the variable which contains a sale.
        sales.append(sale) #for each row within the spreadsheet, this is appended within the list.

    total = sum(sales) #Finally at this point we have the sum of all sales printed. The output does not appear elegant.        
    print('Total sales: {}'.format(total))

run()

#Below appears less elegant than the pandas output. Must write a lot of commands to manipulate data.
#Based on the advice from the session I decided to look at Pandas.


# In[2]:


import pandas as pd #The lib I used   
#Pandas is a special tool that helps people work with information on the computer. 
# It helps people organise information like a chart or table and find patterns or mistakes.
# You can use it to do many things like sort data
#I saw the option to click on Seaborn which can create statistical graphics. They have different purposes.


# In[3]:


df = pd.read_csv('sales.csv') #stack link 
# This line of code is like opening a book called 'sales.csv' and keeping all the information
# in a special construct called a ********DataFrame******. The DataFrame is a table where the information
# is organised so it's easy to find what you need. By putting the information into the DataFrame
# you can use pandas to do different things with the information, like finding certain information
# or making charts. The 'pd' before the code is like a nickname for pandas, which is a special tool
# that helps people work with information


# In[4]:


df
#total = df['sales'].sum()
#print(total)

#below, I have formatted the data to look tabula


# In[5]:


monthly_change = df['sales'].pct_change() 
# The computer code "monthly_change = df['sales'].pct_change()" can help us find out
# how much a store's sales change from one month to the next.

# The code looks at the numbers in the "sales" column of the "df" dataset to do this.
# It calculates the difference between each number and the one before it
# and then shows us this difference as a percentage.

# The result of this calculation is a new column in the same dataset called "monthly_change".
# This column shows the percentage change in sales from one month to the next.
# By looking at these numbers over time, we can see if the store's sales are going up or down,
# and we can look for patterns to help us understand why this is happening.


# In[6]:


print(monthly_change) #This code calculates the percentage change in sales from one month to the next
#using the pandas library in Python.


# In[7]:


average_sales = df['sales'].mean() 
#This code calculates the mean (average) of the 'sales' column from a pandas DataFrame (df) using
#the pandas library in Python


# In[8]:


print(average_sales)


# In[9]:


sales_month = df.groupby(['month'])['sales'].sum()
#This code helps us organise sales data in a table called "df" based on the different months listed in a column
#called "month".
#It then uses a special tool called the "groupby" method in the pandas program, which adds up all 
#the sales numbers for each group of months.
#This can help us see how much money was made in total for each month, 
#and it makes it easier to compare sales numbers between different months.


# In[10]:


sales_month #self-explanatory


# In[11]:


highest_month = sales_month.idxmax()
#This code helps us figure out which month a store made the most sales.

# We have a chart of the store's sales for each month, which the computer calls "sales_month".
# The "idxmax()" tool helps us find the row in the chart with the biggest number.
# Then we use the "highest_month" label to remember which month that was.
# This helps us know which month the store made the most money.


# In[12]:


highest_month #self-explanatory


# In[13]:


lowest_month = sales_month.idxmin()
#I got this code by Googling how to work out the lowest sales in a month using Pandas in python.
#This code helps us work out which month a store made the least amount of sales.
#We have a chart of the store's sales for each month, which the computer calls "sales_month".
#The "idxmin()" tool helps us find the row in the chart with the smallest number.
#Then we use the "lowest_month" label to remember which month that was.
#This helps us know which month the store made the least amount of money.


# In[14]:


lowest_month


# In[15]:


import seaborn as sns
#Seaborn is a tool that helps people create pictures and graphs to help them understand big sets of numbers.
#These pictures can be used to see patterns.

import matplotlib.pyplot as plt
#Matplotlib is a tool that helps people make pictures and graphs
#It helps people make more detailed and complicated pictures

import pandas as pd


# In[16]:


sns.lineplot(data=df, x=df['month'], y=df['sales'])
#I googled how to make a line plot/chart in Python and came across a website called 'Stackoverflow' but I couldnt find what I wanted.
#I then checked the website 'seaborn.pydata'. There was an example of code to draw a line plot.


# In[17]:


sns.barplot(data=df, x=df['month'], y=df['sales']) 
#I googled how to make a barchart in Python and came across a website called 'datatofish.com' 
#They gave me steps but I couldnt find the code.

#I then lookeed on google 'how to code a barchart in python seaborn'
#I came across code from a website called 'geeksforgeeks.org'
#I played around with the code until it worked.
#I did not choose the colours


# In[18]:


sns.pieplot(data=df, x=df['month'], y=df['sales'])
#this did not work, I thought Python may have had a built in function called pieplot 
#outcome below


# In[19]:


import matplotlib.pyplot as plt
#I googled how to make a piechart in python using seaborn and came across
#this code. 'pyplot'
#import matplotlib.pyplot as plt
#sourced from a website called geeksforgeeks.org


# In[20]:


plt.pie(df['sales'], labels=df['month'], autopct='%1.1f%%')

#I came across this piece of code from a website called 'stackoverflow.com'
#it seemed to work


# In[21]:


plt.title('Sales Pie Chart')


# In[22]:


plt.show()


# In[ ]:




