This serves an overview for how to execute this project on a new AMI (assuming postgres is mounted and started into /data)

Step 1: Run the pip installs  
  pip install tweepy  
  pip install psycopg2==2.6.2

Step 2: Create the postgres database  
  psql -U postgres  
  CREATE DATABASE tcount;

Step 3: Clone down the project  
  git clone https://github.com/kyle-mac/W205-EX2.git  
  cd W205-EX2/

Step 4: Populate the database  
  cd extweetwordcount  
  sparse run

Step 5: Execute scripting  
  cd ..  
  python finalresults.py  
  python histogram.py  
  python top20.py

All .png images for the lab are located within the screenshots folder
