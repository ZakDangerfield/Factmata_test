# Factmata_test
My Tech Challenge for Factmata

Firstly thank you for giving me the oppurtunity to demonstrate my skillsets.

I have Created an ETL Pipeline that:
Reads and Extracts all top URLS in R/news using Newspaper3K library.
Extracts data from reddit(r/News) 
Transforms the extracted data into a list and appends a 
Score to each url. The score function used, is there to mimic what we would expect
The layout to look like when we gather score on keywords within each URL.
Finally we Load the data into a PostgreSQL Database.

My postgreSQL image shows a vast array of article Url's, the scores 
from each Url and the textual data.

----How to run the code----

Installation of my requirments.txt is needed to be able to run with my selected library.
It also features other library items that are required, to be able to upload our data
To the cloud. 
A docker compose file will need to be created, and a postgreSQL initiated
on a localhost port number: 5432.

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

