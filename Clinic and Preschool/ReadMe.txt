Step 1: Scrape data from yelp

Run yelp crawls from scrapy/yelpbreak1000

Output: preschool_nyc_995.json, clinic_nyc_3212.json


Step 2: Convert Json file to txt file

Run the program from json_to_txt/BigdataCleanJson  

Input: preschool_nyc_995.json, clinic_nyc_3212.json

Output: preschool_nyc_995.txt, clinic_nyc_3212.txt


Step 3: Remove repeated lines

Run the RemoveRedundance map_reduce program from mapreduce 

Input: preschool_nyc_995.txt, clinic_nyc_3212.txt

Output: preschool_nyc_839.txt, clinic_nyc_2517.txt


Step 4: Count the number of preschools (clinics) in a zip code; calculate the average rating and count how many reviews in total.

Run the RemoveRedundance map_reduce program from mapreduce 

Input: preschool_nyc_839.txt, clinic_nyc_2517.txt

Output: preschool_count_rating.txt, clinic_count_rating.txt



Step 5: Give a score to a zip code with respect to preschool/clinics based on the count and rating.

Run the Score map_reduce program from mapreduce



Step 6: Normalize the score 

Run the FinalScore map_reduce program from map reduce



Step 7: Convert txt file to json file

Run the program from GenerateJson




