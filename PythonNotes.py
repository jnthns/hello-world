### 									PYTHON NOTES
#--------------------------------------------------------------------------------------------------
### VOWEL CHECKER

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
# ### ATTRIBUTES AND METHODS

# # Methods can be thought of as functions ending with parentheses that return a result. For example:
# print(df.head())
# # prints the first five rows of a dataframe
# print(df.describe())
# # prints a description of the data

# # Whereas attributes can are thought of as returning information about data.
# print(df.shape)
# # prints number of rows, number of columns
#--------------------------------------------------------------------------------------------------
### RANDOM FUNCTION NOTES

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

# import pandas as pd 
# import sqlalchemy

# # Read in CSV with specific columns 
# colnames = [0,1,2,9,10,21,28]
# df = pd.read_csv('Truveris ES Ads List Match Q3 2018_2018-07-16_126842_output.csv', usecols=colnames)

# # Rename columns to make SQL querying easier
# # Can also change columns in workbench by using ALTER TABLE 
# # ALTER TABLE Truveris CHANGE COLUMN `Source Name` `Sourcename` VARCHAR(255) NOT NULL
# df.rename(columns={
# 	'Source Name': 'Sourcename',
# 	'Best SID': 'Bestsid',
# 	'Source Domain': 'Sourcedomain'
# 	}, inplace=True)

# Write dataframe to SQL database
# df.to_sql(
# 	name='Truveris',
# 	con=engine,
# 	index=False,
# 	)
# Now Truveris is loaded as a table in test.Tutorial

#--------------------------------------------------------------------------------------------------
### TUTORIALS POINT PYTHON3 PYMYSQL TUTORIAL
# Create test database, test table EMPLOYEE 

# import pymysql

# # Open database connection - Schema is synonymous with Database in MySQL 
# db = pymysql.connect("127.0.0.1","root","h3llsb3lls$","Tutorial")

# # prepare a cursor object using cursor() method
# cursor = db.cursor()
# #----------------(Find SQL Version)-----------------
# # # execute SQL query using execute() method.
# # cursor.execute("SELECT VERSION()")

# # # Fetch a single row using fetchone() method.
# # data = cursor.fetchone()
# # print ("MySQL Workbench version: %s " % data)
# #---------------------------------------------------
# # create table employee
# # sql = ''' CREATE TABLE EMPLOYEE (
# # 	firstname VARCHAR(20) NOT NULL,
# # 	lastname VARCHAR(20),
# # 	age int,
# # 	sex char(1),
# # 	income float ) '''

# # # cursor object executes script
# # try:
# # 	cursor.execute(sql)
# # 	# commit changes in the db
# # 	db.commit()
# # except: 
# # 	# rollback in case error happens
# # 	db.rollback()

# # Write query in triple ''' 
# # firstrow = ''' INSERT INTO EMPLOYEE VALUES (
# # 	'Jon', 'Shek', '23', 'M', '300000') '''

# # cursor.execute(query)
# # cursor.execute(firstrow)

# # commit changes to database
# # hit refresh in workbench to see results
# db.commit()

# # Use %d instead of numerical value (1000) for easier editing 
# income = '''SELECT * FROM EMPLOYEE \
# 			WHERE income > "%d"''' % (1000)

# cursor.execute(income)

# # fetches all rows called in query
# results = cursor.fetchall()
# for row in results:
# 	firstname = row[0]
# 	lastname = row[1]
# 	age = row[2]
# 	sex = row[3]
# 	income = row[4]
# 	print(('His name is %s %s, he\'s %s years old and he makes $%s a year.') % (firstname, lastname, age, income))

# # can also use double quotes, do not break formatting like select statement above 
# demoted = "UPDATE EMPLOYEE SET income = 0 WHERE age = '%d'" % (66)

# cursor.execute(demoted)
# db.commit()
# db.rollback()
# # disconnect from server
# db.close()
#--------------------------------------------------------------------------------------------------
# ### Requests Tutorial
# # https://stackabuse.com/the-python-requests-module/

# # Reading Response of a HTTPS using GET

# import requests

# r = requests.get('http://httpbin.org/get')  
# # for HTML text 
# # print(r.text)

# # inspect element, network tab, click get under name, headers tab on the right
# # response headers section - dictionary 
# print(r.headers['content-type']) # to see what the response format is, which is JSON

# # Requests has built-in json parser .json()
# response = r.json()
# print(response)

# # Requests POST - submitting data rather than getting it 
# payload = {'user_name': 'admin', 'password': 'password'}
# r = requests.post('http://httpbin.org/post', data=payload)

#--------------------------------------------------------------------------------------------------
### Matplotlib & Seaborn 
# https://elitedatascience.com/python-seaborn-tutorial
## Seaborn's built-in datasets - https://github.com/mwaskom/seaborn-data

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns 

# df = pd.read_csv('Pokemon.csv', encoding='windows-1252', index_col=0)

# # Before plotting graph, choose a theme 
# # darkgrid also makes a grid except with a darker background
# sns.set_style('whitegrid')

# # Compare attack and defense columns 
# # fit_reg is the regression line, removed to show just scatter plot
# ## can also remove scatter plot and keep just the regression line by setting scatter=False
# # hue is the color of the points. Set hue to csv column 'stage' to show evolution stage of each pokemon
# sns.lmplot(x='Attack', y='Defense', data=df, fit_reg=False, hue='Stage')

# # Set color palette 
# # list format
# pkmncolors = ['#78C850',  # Grass
#                     '#F08030',  # Fire
#                     '#6890F0',  # Water
#                     '#A8B820',  # Bug
#                     '#A8A878',  # Normal
#                     '#A040A0',  # Poison
#                     '#F8D030',  # Electric
#                     '#E0C068',  # Ground
#                     '#EE99AC',  # Fairy
#                     '#C03028',  # Fighting
#                     '#F85888',  # Psychic
#                     '#B8A038',  # Rock
#                     '#705898',  # Ghost
#                     '#98D8D8',  # Ice
#                     '#7038F8',  # Dragon
#                    ]

# # violinplot useful for showing distribution instead of summary statistics
# sns.violinplot(x='Type 1', y='Attack', data=df, palette=pkmncolors)

# # swarmplot useful for showing each point while 'stacking' those with similar values 
# sns.swarmplot(x='Type 1', y='Attack', data=df, palette=pkmncolors)

# # can also overlay plots - swarm and violin in this example
# # Set figure size with matplotlib
# plt.figure(figsize=(10,6))
 
# # # Create plot
# sns.violinplot(x='Type 1',
#                y='Attack', 
#                data=df, 
#                inner=None, # Remove the bars inside the violins
#                palette=pkmncolors)
 
# # sns.swarmplot(x='Type 1', 
#               y='Attack', 
#               data=df, 
#               color='k', # Make points black
#               alpha=0.7) # and slightly transparent
 
# # Set title with matplotlib
# plt.title('Attack by Type')

# # Some columns can be removed from the file that wouldn't be useful in the graphs for cleaner representation
# statsdf = df.drop(['Total', 'Stage', 'Legendary'], axis=1)

# # First, the DataFrame to melt.
# # Second, ID variables to keep (Pandas will melt all of the other ones).
# # Finally, a name for the new, melted variable.
# melted_df = pd.melt(statsdf, id_vars=['Name', 'Type 1', 'Type 2'], # variables to keep
# 							 var_name='Stat') # name of melted variable

# ## Display new graph with melted_df
# sns.swarmplot(x='Stat', y='value', data=melted_df, hue='Type 1', palette=pkmncolors)

# ## Set a different ylimit for this swarm plot
# plt.ylim(0,260)
# ## Shift legend to the right
# plt.legend(bbox_to_anchor=(1,1), loc=2)

# # Bar Graph aka Count Plot 
# sns.countplot(x='Type 1', data=df, palette=pkmncolors)

# # Tweak x and y axis limit using Matplotlib
# plt.ylim(0, None)
# plt.xlim(-1, None)


# # Display graph in Python
# plt.show()

#--------------------------------------------------------------------------------------------------
### SQL Queries in Pandas Python format
## https://codeburst.io/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
## take airports.csv from http://ourairports.com/data/

import pandas as pd 
import sqlalchemy

airports = pd.read_csv('airports.csv')

### BASICS 
sql = ''' SELECT id FROM airports WHERE ident = "KLAX"''' 
pdselectid = airports[airports.ident=='KLAX'].id 

sql = ''' SELECT DISTINCT type FROM airports'''
pdselectdistinct = airports.type.unique()

sql = ''' SELECT * FROM airports WHERE type IN ('heliport', 'balloonport')'''
pdin = airports[airports.type.isin(['heliport','balloonport'])]

sql = ''' SELECT * FROM airports WHERE type NOT IN ('heliport', 'balloonport')'''
pdnotin = airports[~airports.type.isin(['heliport','balloonport'])]

# In Pandas, .count() will return the number of non-null/NaN values. To get the same result as the SQL COUNT, use .size().
sql = ''' SELECT iso_country, type, COUNT(*) FROM airports GROUP BY iso_country, type ORDER BY iso_country, type '''
pdsize = airports.groupby(['iso_country','type']).size()

### GETS HARDER
sql = ''' SELECT iso_country, type, COUNT(*) FROM airports GROUP BY iso_country, type ORDER BY iso_country, COUNT(*) DESC '''
pdorderbycountdesc = airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])
# What is this trickery with .to_frame() and .reset_index()? Because we want to sort by our calculated field (size), this field needs to become part of the DataFrame. After grouping in Pandas, we get back a different type, called a GroupByObject. So we need to convert it back to a DataFrame. With .reset_index(), we restart row numbering for our data frame.

sql = ''' SELECT type, COUNT(*) FROM airports WHERE iso_country = 'US' GROUP BY type HAVING COUNT(*) > 1000 ORDER BY COUNT(*) DESC '''
pdhaving = airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)

# Create new dataframe that contains number of airports per country
pdbycountry = airports.groupby(['iso_country']).size()

# Order things by airport count and select the top 10 countries with the largest count
sql = ''' SELECT iso_country FROM by_country ORDER BY size desc LIMIT 10 '''
pdn = pdbycountry.nlargest(10)
# nlargest(number of rows to pull, which column to pull from)
# print(airports.nlargest(5, 'id'))

Random SQL Question
# Find cities in table Station that start with vowels 
sql = ''' SELECT City FROM Station WHERE City RLIKE '^[aeiou]' ''' 
# Ending with vowels?
sql = ''' SELECT City FROM Station WHERE City REGEXP '[aeiou]$' '''





