import psycopg2
import sys

try:
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	inputs = sys.argv[1].split(",")
	k1 = int(inputs[0])
	k2 = int(inputs[1])
	cur.execute("SELECT word, count from tweetwordcount WHERE count >= %s and count <= %s order by count desc;" %(k1,k2))
	records = cur.fetchall()
	print records

	conn.commit()
	conn.close()
except Exception as e:
    print e
