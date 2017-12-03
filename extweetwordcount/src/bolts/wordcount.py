from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        self.log('%s: %d' % (word, self.counts[word]))

        # Set up connection to the tweetcount table in postgres
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # Set up cursor
        cur = conn.cursor()

        try:
            cur.execute('''CREATE TABLE tweetwordcount(word TEXT PRIMARY KEY NOT NULL,count INT NOT NULL);''')
            print ("created table tweetwordcount")
        except:
            print ("Not Created")

        cur.execute("UPDATE tweetwordcount SET count=count+1 WHERE word=%s", (word,))

        # If word count is 0 set to 1
        if cur.rowcount == 0:
            cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, 1)", (word,))

        conn.commit()


        conn.close()
