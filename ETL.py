import psycopg2
import psycopg2.extras
import newspaper
from newspaper import Article
import score as sc
from newspaper import news_pool
import threading
import concurrent.futures

import random
import time
import typing


# connecting to Mysql through a docker compose file
mydb = psycopg2.connect(
host="localhost",
user="postgres",
password="password",
database="postgres",
)
mycursor = mydb.cursor()

keywords = sc.get_signals()

reddit_news = newspaper.build("https://www.reddit.com/r/news/", memoize_articles=False)

articles = []

def DownloadArticleText(url):
    arti = {}
    scores = {}
    article = Article(url)
    article.download()
    article.parse()
    arti['url'] = url
    arti['text'] = article.text

    def score(signal: str, text: str) -> (str, float):
        time.sleep(0.2)
        scores[signal] = random.randint(0, 100) / 100

    threads = []

#starting threads
    for word in keywords:
        x = threading.Thread(target=score, args=(word,article.text,))
        threads.append(x)
        x.start()
#itterates and combines threads
    for thread in threads:
        thread.join()

    temp = '';
    for i in keywords:
        temp += str(scores[i]) + ', '
    arti['score'] = temp.strip(', ')
    articles.append(arti)
    
threads = []

for article in reddit_news.articles:
    x = threading.Thread(target=DownloadArticleText, args=(article.url,))
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()


psycopg2.extras.execute_values(mycursor, """INSERT INTO news (score,url,text) VALUES %s;""",
[(
    t["score"],
    t["url"],
    t["text"]
)for t in articles],
template="(%s,%s,%s)")
mydb.commit()
mycursor.close()
mydb.close()

