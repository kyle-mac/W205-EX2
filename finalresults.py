import psycopg2
import sys

try:
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	if len(sys.argv) > 1:
		word = sys.argv[1]
		cur.execute("SELECT word, count from tweetwordcount WHERE word = '%s';" %word)
		result = cur.fetchone()
		print result
	else:
		cur.execute("SELECT word, count from Tweetwordcount order by word asc")
		records = cur.fetchall()
		print records
	conn.commit()
	conn.close()
except Exception as e:
    print e
