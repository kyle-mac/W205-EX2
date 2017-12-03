import psycopg2
import sys

try:
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	word = sys.argv[1]
	cur.execute("SELECT word, count from tweetwordcount WHERE word = '%s';" %word)
	result = cur.fetchone()
	print "Total number of occurences of \"%s\": %s" %(result[0], result[1])
	conn.commit()
	conn.close()
except:
    print "Error fetching query"
