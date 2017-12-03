import psycopg2
import sys

try:
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count from tweetwordcount order by count desc LIMIT 20")
	records = cur.fetchall()
	print records
	conn.commit()
	conn.close()
except Exception as e:
    print e
