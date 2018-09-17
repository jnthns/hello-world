### 									PYTHON NOTES
#--------------------------------------------------------------------------------------------------
## VOWEL CHECKER
# Count the number of vowels that appear in a string, using an if statement.

# x = input('Please enter a word.')

# def vowelcheck(x):
# 	count = 0
# 	if x in 'aeiouAEIOU':
# 		count += 1
# 		print('There are ' + str(count) + ' vowels in this word.')
# 	else:
# 		print('There are ' + str(count) + ' vowels in this word.')

# # Now using a list comprehension. 

# x = input('Please enter a word.')

# print('There are ' + str(sum([1 for i in x if i in 'aeiouAEIOU'])) + ' vowels in this word.')

#--------------------------------------------------------------------------------------------------
# def sleep_in(weekday):
#   weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#   if weekday in weekdays:
#     return True
#   elif weekday not in weekdays:
#     return False

# def monkey_trouble(a_smile, b_smile):
#   if a_smile == True and b_smile == False:
#     return False
#   elif a_smile == False and b_smile == True:
#     return False
#   else:
#     return True

# def sum_double(a, b):
#   if a == b:
#     return (a + b) * 2
#   elif a != b:
#     return (a + b)

#--------------------------------------------------------------------------------------------------
## USING SQL THROUGH PANDAS/PYTHON

# https://www.youtube.com/watch?v=M-4EpNdlSuY
# import pandas as pd 
# import sqlalchemy
# # # sqlalchemy designed for python 
# # # also need to pip install PyMySQL - another module used for SQL and Python 

# # # create engine with PyMySQL, using MySQL and select schema
# # mysql+module://user:password@localhost:3306/schema name
# engine = sqlalchemy.create_engine('mysql+pymysql://root:h3llsb3lls$@localhost:3306/Tutorial')

# # read table in schema using Pandas dataframes
# # table name, engine, columns(optional)
# ## in this example, referred to as 'engine' but also commonly referred to as 'conn' for connection
# df = pd.read_sql_table('athena', engine, columns=['active', 'sourcename', 'bestsid', 'Account', 'Domain', 'MEI'])
# # # print(df.head(25))

# # SQL query
# query = ''' SELECT active, sourcename, bestsid, account, domain FROM athena WHERE `MEI` > 20 ''' 

# # Read SQL query into dataframe
# df = pd.read_sql_query(query, engine)
# print(df.head(5))

# df = df.to_csv('readsql.csv')

#--------------------------------------------------------------------------------------------------
### READ DATA FROM CSV INTO PANDAS, THEN INTO SQL

import pandas as pd 
import sqlalchemy

# Read in CSV with specific columns 
colnames = [0,1,2,9,10,21,28]
df = pd.read_csv('Truveris ES Ads List Match Q3 2018_2018-07-16_126842_output.csv', usecols=colnames)

# Rename columns to make SQL querying easier
# Can also change columns in workbench by using ALTER TABLE 
# ALTER TABLE Truveris CHANGE COLUMN `Source Name` `Sourcename` VARCHAR(255) NOT NULL
df.rename(columns={
	'Source Name': 'Sourcename',
	'Best SID': 'Bestsid',
	'Source Domain': 'Sourcedomain'
	}, inplace=True)

# Write dataframe to SQL database
# df.to_sql(
# 	name='Truveris',
# 	con=engine,
# 	index=False,
# 	)
# Now Truveris is loaded as a table in test.Tutorial
#--------------------------------------------------------------------------------------------------
# ### Attributes and Methods 
# # Methods can be thought of as functions ending with parentheses that return a result. For example:
# print(df.head())
# # prints the first five rows of a dataframe
# print(df.describe())
# # prints a description of the data

# # Whereas attributes can are thought of as returning information about data.
# print(df.shape)
# # prints number of rows, number of columns





