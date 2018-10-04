# ## 									PYTHON NOTES
# -------------------------------------------------------------------------------------------------------------------------
# ## VOWEL CHECKER

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

# -------------------------------------------------------------------------------------------------------------------------
# ### ATTRIBUTES AND METHODS

# # Methods can be thought of as functions ending with parentheses that return a result. For example:
# print(df.head())
# # prints the first five rows of a dataframe
# print(df.describe())
# # prints a description of the data

# # Whereas attributes can are thought of as returning information about data.
# print(df.shape)
# # prints number of rows, number of columns
# -------------------------------------------------------------------------------------------------------------------------
# ## RANDOM FUNCTION NOTES

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

# -------------------------------------------------------------------------------------------------------------------------
# # USING SQL THROUGH PANDAS/PYTHON

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

# -------------------------------------------------------------------------------------------------------------------------
# ## READ DATA FROM CSV INTO PANDAS, THEN INTO SQL

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

# -------------------------------------------------------------------------------------------------------------------------
# ## TUTORIALS POINT PYTHON3 PYMYSQL TUTORIAL
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
# -------------------------------------------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------------------------------------------
# ## Matplotlib & Seaborn 
# https://elitedatascience.com/python-seaborn-tutorial
# # Seaborn's built-in datasets - https://github.com/mwaskom/seaborn-data

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

# -------------------------------------------------------------------------------------------------------------------------
# ## SQL Queries in Pandas Python format
# # https://codeburst.io/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
# # take airports.csv from http://ourairports.com/data/

# import pandas as pd 
# import sqlalchemy

# airports = pd.read_csv('airports.csv')

# ### BASICS 
# sql = ''' SELECT id FROM airports WHERE ident = "KLAX"''' 
# pdselectid = airports[airports.ident=='KLAX'].id 

# sql = ''' SELECT DISTINCT type FROM airports'''
# pdselectDISTINCT = airports.type.unique()

# sql = ''' SELECT * FROM airports WHERE type IN ('heliport', 'balloonport')'''
# pdin = airports[airports.type.isin(['heliport','balloonport'])]

# sql = ''' SELECT * FROM airports WHERE type NOT IN ('heliport', 'balloonport')'''
# pdnotin = airports[~airports.type.isin(['heliport','balloonport'])]

# # In Pandas, .count() will return the number of non-null/NaN values. To get the same result as the SQL COUNT, use .size().
# sql = ''' SELECT iso_country, type, COUNT(*) FROM airports GROUP BY iso_country, type ORDER BY iso_country, type '''
# pdsize = airports.groupby(['iso_country','type']).size()

# ### GETS HARDER
# sql = ''' SELECT iso_country, type, COUNT(*) FROM airports GROUP BY iso_country, type ORDER BY iso_country, COUNT(*) DESC '''
# pdorderbycountdesc = airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])
# # What is this trickery with .to_frame() and .reset_index()? Because we want to sort by our calculated field (size), this field needs to become part of the DataFrame. After grouping in Pandas, we get back a different type, called a GroupByObject. So we need to convert it back to a DataFrame. With .reset_index(), we restart row numbering for our data frame.

# sql = ''' SELECT type, COUNT(*) FROM airports WHERE iso_country = 'US' GROUP BY type HAVING COUNT(*) > 1000 ORDER BY COUNT(*) DESC '''
# pdhaving = airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)

# # Create new dataframe that contains number of airports per country
# pdbycountry = airports.groupby(['iso_country']).size()

# # Order things by airport count and select the top 10 countries with the largest count
# sql = ''' SELECT iso_country FROM by_country ORDER BY size desc LIMIT 10 '''
# pdn = pdbycountry.nlargest(10)
# # nlargest(number of rows to pull, which column to pull from)
# # print(airports.nlargest(5, 'id'))


# #-------------------------------------------------------------------------------------------------------------------------
# # Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

# # Equilateral: It's a triangle with 3 sides of equal length.
# # Isosceles: It's a triangle with 2 sides of equal length.
# # Scalene: It's a triangle with 3 sides of differing lengths.
# # Not A Triangle: The given values of A, B, and C don't form a triangle.

# sql = ''' SELECT CASE 
# 					WHEN A + B > C AND B + C > A AND A + C > B THEN 
# 		  		CASE 
# 					WHEN A = B = C THEN "Equilateral"
# 					WHEN A = B OR B = C OR A = C THEN "Isoceles"
# 					ELSE "Scalene"
# 				END
# 			ELSE "Not a Triangle" 
# 		  END
# 		FROM Triangles; '''


# #-------------------------------------------------------------------------------------------------------------------------
# Random SQL Questions

# Find cities in table Station that start with vowels 
sql = ''' SELECT City FROM Station WHERE City RLIKE '^[aeiou]' ''' 
# Ending with vowels?
sql = ''' SELECT City FROM Station WHERE City REGEXP '[aeiou]$' '''

# Write a query to find the 10th highest employee salary from table employee
sql = ''' SELECT Distinct(salary) from Employee 
		  ORDER BY salary DESC
		  LIMIT 1 OFFSET 9'''

# Make col2 look exactly opposite to col1
# Col1	Col2
# 1		0
# 0		1
# 0		1
# 0		1
# 1		0
# 0		1
# 1		0
# 1		0

sql = ''' UPDATE table set col2 = case when col1 = 1 then 0 else 1 end; '''

sql = ''' SELECT b.emp_id AS Manager_Id, b.Emp_name AS Manager, AVG(a.Salary) AS Average_Salary_under_manager FROM employee a, employee b where a.manager_id = b.emp_id group by b.emp_id, b.emp_name order by b.emp_id '''


# #-------------------------------------------------------------------------------------------------------------------------
# ### HackerRank Medium Difficulty SQL Advanced Select 
# ## https://www.hackerrank.com/challenges/the-company/problem

# Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

# # Can be done without joins 
# # Company table has all codes so only need to select C.company_code, same for founder
# # Total number of managers - select count (DISTINCT) for each manager type and employee
# # Select from multiple tables on common columns 
# # Group then order by company code 

# sql = ''' SELECT c.company_code, c.founder, 
#     COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), 
#     COUNT(DISTINCT m.manager_code),COUNT(DISTINCT e.employee_code) 
# FROM Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e 
# WHERE c.company_code = l.company_code 
#     AND l.lead_manager_code=s.lead_manager_code 
#     AND s.senior_manager_code=m.senior_manager_code 
#     AND m.manager_code=e.manager_code 
# GROUP BY c.company_code ORDER BY c.company_code; '''

# #-------------------------------------------------------------------------------------------------------------------------
# ### HackerRank Medium Difficulty SQL Advanced Select 
# ## https://www.hackerrank.com/challenges/the-pads/problem

# # Generate the following two result sets:
# # Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
# # Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format: 

sql = ''' SELECT name AS '',
			Occupation AS '', CONCAT('(',LEFT(Occupation,1),')') AS ''
		  FROM Occupations 
		  ORDER BY name

		  SELECT CONCAT('There are total ',count(occupation),' ',lower(occupation),'s.') AS total
		  FROM occupations
		  GROUP BY occupation
	      ORDER BY total '''

#-------------------------------------------------------------------------------------------------------------------------

# Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.


sql = ''' SELECT hacker_id, name 
		  FROM hackers h 
		  JOIN submissions s on h.hacker_id = s.hacker_id
		  WHERE score = (SELECT max(score)
		  				 FROM difficulty d JOIN challenges c on d.difficulty_level = c.difficulty_level)
		  AND count(distinct challenge_id) > 2

		  SELECT h.hacker_id, h.name
		  FROM submissions s 
		  inner join challenges c
		  on s.challenge_id = c.challenge_id
		  inner join difficulty d 
		  on c.difficulty_level = d.difficulty_level
		  inner join hackers h 
		  on s.hacker_id = h.hacker_id 
		  where s.score = d.score and c.difficulty_level = d.difficulty_level
		  group by h.hacker_id, h.name
	 	  having count(s.hacker_id) > 1
		  order by count(s.hacker_id) desc, s.hacker_id asc '''
# Before starting this query, look at the tables that has the most important data - submissions
# start by pulling the necessary data from submissions
# inner join the other tables on their respective mutual identifiers 
# then do a where clause that specifies the parameters - score = score because you want the highest score
# difficulty_level must be equal
# group by what we're looking for, find the one with the most scores by count() 
# don't need to count distinct 
#-------------------------------------------------------------------------------------------------------------------------
# https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
# Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

sql = ''' SELECT id, age, coins_needed, power 
    FROM wands w 
    JOIN wands_property p ON w.code = p.code
    WHERE p.is_evil = 0 AND w.coins_needed = 
    (SELECT MIN(coins_needed) FROM wands ww JOIN wands_property wp ON ww.code = wp.code 
     WHERE ww.power = w.power AND p.age = wp.age)
    ORDER BY w.power desc, p.age desc '''

# id, age, coins_needed, power
# join on code column 
# wand can't be evil and needs to be lowest price
# first select clause finds id, age, price, power where evil = 0 and price = min
# then next select clause finds min(price) while checking power and age
# order by power desc, age desc 

#-------------------------------------------------------------------------------------------------------------------------
# https://www.hackerrank.com/challenges/contest-leaderboard/problem
# Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of 0 from your result.

# join tables on hacker_id 
# score = sum(max(score))
# where score = (select max(sum(score)) from hackers hh JOIN submissions ss on hh.hacker_id = ss.submissions.id where)
# hacker_id, name, total score order by score desc
# sort by asc hacker_id if 


#-------------------------------------------------------------------------------------------------------------------------

### ------------------------------------------|      SQL JOINS      |-------------------------------------------------------------  

# 1) INNER JOIN (a.k.a. “simple join”): Returns all rows for which there is at least one match in BOTH tables. This is the default type of join if no specific JOIN type is specified.

# 2) LEFT JOIN (or LEFT OUTER JOIN): Returns all rows from the left table, and the matched rows from the right table; i.e., the results will contain all records from the left table, even if the JOIN condition doesn’t find any matching records in the right table. This means that if the ON clause doesn’t match any records in the right table, the JOIN will still return a row in the result for that record in the left table, but with NULL in each column from the right table.

# 3) RIGHT JOIN (or RIGHT OUTER JOIN): Returns all rows from the right table, and the matched rows from the left table. This is the exact opposite of a LEFT JOIN; i.e., the results will contain all records from the right table, even if the JOIN condition doesn’t find any matching records in the left table. This means that if the ON clause doesn’t match any records in the left table, the JOIN will still return a row in the result for that record in the right table, but with NULL in each column from the left table.

# 4) FULL JOIN (or FULL OUTER JOIN): Returns all rows for which there is a match in EITHER of the tables. Conceptually, a FULL JOIN combines the effect of applying both a LEFT JOIN and a RIGHT JOIN; i.e., its result set is equivalent to performing a UNION of the results of left and right outer queries.

# 5) CROSS JOIN: Returns all records where each row from the first table is combined with each row from the second table (i.e., returns the Cartesian product of the sets of rows from the joined tables). Note that a CROSS JOIN can either be specified using the CROSS JOIN syntax (“explicit join notation”) or (b) listing the tables in the FROM clause separated by commas without using a WHERE clause to supply join criteria (“implicit join notation”).

# 6) NATURAL JOIN: Joins on one or more columns in two tables, then pulls the rest of the columns from both tables. Only displays one instance of the column that the tables are joined on. Example, column sales_id exists in table Sales and table Customers - select * from sales natural join customers - first column displayed is sales_id, then the rest are all columns from both tables. 

# USING clause - can join on key column with USING instead of usual syntax
sql = ''' SELECT c.name, l.name 
		  FROM countries 
		  INNER JOIN language 
		  USING(code)'''
# where code is the primary key column in both tables

# Can also join without explicity naming JOIN ON...etc
sql = '''SELECT c.name, l.name 
		 FROM countries
		 where c.code = l.code'''

# First table joins on second table - Examples 
# https://www.w3resource.com/sql-exercises/movie-database-exercise/joins-exercises-on-movie-database.php 
# Question #3
# Write a query in SQL to find the name of movie and director (first and last names) who directed a movie that casted a role for 'Eyes Wide Shut'. 
# 		  1) Using Inner Joins
sql = '''
		SELECT mov_title, dir_fname, dir_lname FROM director d
		JOIN movie_direction md ON d.dir_id = md.dir_id
		JOIN movie_cast mc ON md.mov_id = mc.mov_id
		JOIN movie m on mc.mov_id = m.mov_id
		WHERE m.mov_title = 'Eyes Wide Shut'
		
		# 2) Using Natural Joins
		SELECT mov_title, dir_fname, dir_lname FROM director 
		NATURAL JOIN movie_direction
		NATURAL JOIN movie_cast
		NATURAL JOIN movie
		WHERE mov_title = 'Eyes Wide Shut' 

		# 4. Write a query in SQL to find the name of movie and director (first and last names) who directed a movie that casted a role as Sean Maguire.
		SELECT mov_title, dir_fname, dir_lname FROM director
		JOIN movie_direction on director.dir_id = movie_direction.dir_id 
		NATURAL JOIN movie_cast
		NATURAL JOIN movie
		WHERE role = 'Sean Maguire'


	'''

#-------------------------------------------------------------------------------------------------------------------------
# SQL Joins/Subqueries Practice
# https://www.w3resource.com/sql-exercises/subqueries/sql-subqueries-inventory-exercise-30.php

sql = ''' 

		SELECT o.ord_no, o.purch_amt, c.cust_name, c.city 
		FROM orders o, customer c 
		WHERE o.customer_id = c.customer_id
		AND o.purch_amt BETWEEN 500 and 2000

		SELECT c.cust_name, s.name
		from customer c, salesman s
		where c.salesman_id = s.salesman_id

		SELECT c.cust_name, s.name, s.commission 
		FROM customer c, salesman s
		WHERE c.salesman_id = s.salesman_id
		AND s.commission > .12

		SELECT o.*, c.cust_name as Customer, s.name as Salesman, s.commission
		FROM orders o, customer c, salesman s
		WHERE o.customer_id = c.customer_id and c.salesman_id = s.salesman_id

		SELECT c.*, s.name as Salesman
		FROM customer c 
		LEFT JOIN salesman s ON c.salesman_id = s.salesman_id
		WHERE c.grade < 300
		ORDER BY c.customer_id asc

		SELECT c.cust_name as Customer, c.city, o.ord_no, o.ord_date, o.purch_amt, s.name, s.commission 
		FROM customer c
		LEFT JOIN orders o on c.customer_id = o.customer_id
		LEFT JOIN salesman s on o.salesman_id = s.salesman_id

		SELECT c.cust_name as Customer, c.city, o.ord_no, o.ord_date, o.purch_amt
		from customers c, orders o where c.customer_id = o.customer_id
		where c.grade is not null

		SELECT * FROM Orders 
		where salesman_id = (select salesman_id from salesman where salesman_id = 'Paul Adam')

		# Write a query to find all those customers who hold a different grade than any customer of the city Dallas.
		SELECT * FROM customer 
		WHERE NOT grade = ANY (SELECT grade FROM customer WHERE city = 'Dallas')

		SELECT avg(i.pro_price) as Average Price, c.com_name as Manufacturer FROM item_mast i
		JOIN company_mast c on i.pro_com = c.com_id 

		SELECT rev.rev_name FROM reviewer rev JOIN rating r ON rev.rev_id = r.rev_id 
		WHERE num_o_ratings IS NULL

		# Write a query in SQL to list the first and last names of all the actors who were cast in the movie 'Annie Hall', and the roles they played in that production.
		SELECT a.act_fname as firstname, a.act_lname as lastname, c.role FROM actor a 
		JOIN movie_cast c on a.act_id = c.act_id
		JOIN movie m on c.mov_id = m.mov_id
		WHERE m.mov_title = 'Annie Hall'

		SELECT mov_title, avg(mov_time), count(gen_title) FROM movie m
		JOIN movie_genres mg on m.mov_id = mg.mov_id
		JOIN genres g on mg.gen_id = g.gen_id
		GROUP BY gen_title

		select mov_title, act_fname, act_lname, role FROM movie 
		JOIN movie_cast ON movie.mov_id = movie_cast.mov_id
		NATURAL JOIN actor 
		WHERE actor.act_id IN (SELECT act_id FROM movie_cast GROUP BY act_id HAVING COUNT(*) >= 2)

		SELECT act_fname, act_lname, role, mov_title FROM actor a
		JOIN movie_cast c ON a.act_id = c.act_id
		JOIN movie m ON c.mov_id = m.mov_id
		WHERE mov_title = 'Chinatown' 

		SELECT dir_fname, dir_lname, mov_title, act_fname as firstname, act_lname as lastname, role FROM director  
		NATURAL JOIN movie_direction 
		NATURAL JOIN movie m
		NATURAL JOIN movie_cast
		NATURAL JOIN actor
		WHERE act_fname = 'Claire' and act_lname = 'Danes'

6 + 12
		



