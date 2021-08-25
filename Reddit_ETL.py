import sys
import re
import psycopg2
import psycopg2.extras
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
import praw
import pandas as pd
import datetime as dt
import config
from newspaper import Article
import mysql.connector

# connecting to Mysql through a docker compose file
mydb = psycopg2.connect(
host="localhost",
user="postgres",
password="password",
database="postgres",
)
mycursor = mydb.cursor()

# Connecting to Reddit Via my App
reddit = praw.Reddit(client_id='vC4RnbqYejlQbk1KkjXJ0w',
                    client_secret='ortSotSwUbt8JQ02aivcQIaw6ZozVg', 
                    user_agent='zak_test', 
                    username ='Urbantrixta', 
                    password='flames09')

# selecting the subreddit
subreddit = reddit.subreddit('news')
top_subreddit = subreddit.top(limit=3)
keyword='sexism','hate speech','racism'

# creating a dataframe for each specific type of data
subarticles = []

# submits the data selected from reddit and temporarily storing it in a variable
for submission in top_subreddit:
    topics_dict = { "title":"",
                    "score":"",  
                    "id":"", 
                    "url":"",  
                    "comms_num": "", 
                    "created": "", 
                    "body":"",
                    "textual_data":""}
    topics_dict["title"]= submission.title
    topics_dict["score"]=submission.score
    topics_dict["id"]=submission.id
    topics_dict["url"]=submission.url
    topics_dict["comms_num"]=submission.num_comments
    topics_dict["created"]=submission.created
    topics_dict["body"]=submission.selftext

    article = Article(topics_dict["url"])
    article.download()

    article.parse()
    topics_dict["textual_data"]=article.text
    
    subarticles.append(topics_dict)

# __________TRAILS TAKEN TO MODIFY DATA____________________________________________________________
    # used to trial a method of calculating keywords.
    # for i in keyword:
    #     while textual_data.find(i) >= 0:
    #         count++
    #         textual_data.replace(textual_data.find(i), ' ')

    # topics_dict["calc"].append(count)
    # count = 0

# # Variable
# URL = pd.DataFrame(topics_dict["url"])

# # creating an empty list
# textual_data = []

# # itterating through the URL's and extracting textual Data (Using Newspaper3K)
# for item in URL.itertuples():
#     # print(item[1])
#     article = Article(item[1])
#     article.download()

#     article.parse()

#     textual_data.append(article.text)
    # if len(textual_data) > 30:
    # print (article.text)
    #     break
    
# for submission in resp:
#     print ("ID: ",submission.id)
#     print ("  Title: ",submission.title.encode('ascii', 'ignore'))
#     print ("  Score: ",submission.score)
#     print ("  URL: ",submission.url.encode('ascii', 'ignore'))
#     print ("  Text: ",submission.selftext[:120].encode('ascii', 'ignore'))
#________________________________________________________________________________


# CONNECTION TO MY POTGRESQL
psycopg2.extras.execute_values(mycursor, """INSERT INTO news (id,title,score,url,text) VALUES %s;""",
[(
    t["id"],
    t["title"],
    t["score"],
    t["url"],
    t["textual_data"]
)for t in subarticles],
template="(%s,%s,%s,%s,%s)")
mydb.commit()
mycursor.close()
mydb.close()
