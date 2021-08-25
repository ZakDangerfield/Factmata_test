# Factmata_test
My Tech Challenge for Factmata

Firstly thank you for giving me the oppurtunity to demonstrate my skillsets.

I have Created an ETL Pipeline that:
Reads and Extracts all top URLS in R/news (Newspaper3K)
Extracts data from reddit(r/News)
Transforms the extracted data into a dictionary
Loads the data into a PostgreSQL Database.

My postgreSQL image shows just a snippet of 3 articles being extracted transfomed and loaded in PostgreSQL.
My code has the ability to extract transform and load a vast number of articles with only limitations to those
with Legal safeguards in place. (Unable to be extracted due to legal reasons.)

there is also commented out sections that show that it is also possible 
to filter all articles in (r/News) by keywords and only showing articles 
that obtain these keywords. This function also calculayes how many time they appear in each article.
this was an attempt to mimic a ML grading system for harmful words.

----How to run the code----
Installation of my requirments.txt is needed to be able to run with my selected library.

A docker compose file will need to be created, and a postgreSQL initiated
on a localhost port number: 5432.

The code may be modified to search through other articles of the users choice.

----AWS Setup----

The way my ETL has been created can easily be reworked to be compatable
with storing the data into AWS or any other Data warehouse management system.
By doing so you will be able to take advantage of using the latest technologies I.E Visualisation

This can be acheived by:
- activating a serverless connection to an AWS account using a serverless.yml and creating an EC2 Instance.

- using our serverless.yml that is now connected to our AWS account we can transfer our extracted raw data into an S3 bucket

- creating a lambda we can now activate the handler.py to initiate the ETL and store it into our chosen data Warehouse

I have added examples of how i have previously been successful in creating an ETL that uses
AWS via a serverless connection using a serverless.YML and a Handler.py

