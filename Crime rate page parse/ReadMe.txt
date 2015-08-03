Step 1: Scrape data from crimedata

execute Parser3

Output: crime3


Step 2: Calculate averages

Run MapReduce code named crime.jar

Input: crime3

Output: part-r-00000


Step 3: Find the minimum average crime

Run hive script named hive and pipe result to a file
example: hive -f hive > hiveoutput

Input: part-r-00000

Output: hiveoutput


Step 3: Execute jsoncreator program

Run JSONCrime

Input: crime3,hiveoutput

Output: crime3.json



