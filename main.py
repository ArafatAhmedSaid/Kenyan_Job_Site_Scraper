# STEP 1: IMPORT LIBRARIES

import requests                                                                    # For Fetch-ing content from the web.
from bs4 import BeautifulSoup                                                      # For Parse-ing HTML content.
import csv                                                                         # For Save-ing data to a CSV file.
#import pandas as pd                                                               # For read/present-ing data in an Excel-like format.



# STEP 2: REQUEST THE WEB

base_url = 'https://www.myjobmag.co.ke/search/jobs?field=Aviation+%2F+Airline'     # Source of information i.e. Job Website

response = requests.get(base_url)                                                  # Sends request to website and get response as a HTML page.
print(f'Status_Code: {response.status_code}')                                      # 200 means request was successful.
#print(response.content[:100])                                                     # Test = Prints the first 100 characters of the HTML content.



# STEP 3: PARSE HTML CONTENT

soup = BeautifulSoup(response.content, 'html.parser')                              # Turns messy HTML into Structured Object (soup) that we can easily search through.
# response.content                                                                 # Raw HTML content returned from the website.
# 'html.parser'                                                                    # Parser used by BeautifulSoup to process the HTML.
# BeautifulSoup (...)                                                              # Creates a BeautifulSoup object which represents the entire HTML document.



# STEP 4: INSPECT/EXTRACT DATA

jobs = soup.find_all('li', class_='job-list-li')
#print(jobs)                                                                       # Tests if the selection/extraction worked.
#containers = len(jobs)
#print (containers)



# STEP 5: SAVE DATA IN A CSV FILE

with open('Aviation_Jobs.csv', 'w', newline='', encoding='utf-8') as file:         # With statement closes the code once you are done with it. newline='' prevents blanklines in the CSV file. encoding='utf-8' ensures special characters are handled correctly (~shown).
    writer = csv.writer(file)                                                      # Creates a 'CSV writer object' that lets us write rows to the file
    writer.writerow(["Aviation Jobs in Kenya:"])                                   # Writes the header row of the CSV file i.e. Aviation Jobs in Kenya:

    for job in jobs:
        job_title_tag = job.find('h2')
        job_title = job_title_tag.text.strip() if job_title_tag else 'N/A'

        company_tag = job.find('li', class_='job-logo')
        company = company_tag.img['alt'] if company_tag else 'N/A'

        date_posted_tag = job.find('li', class_='job-item')
        date_posted = date_posted_tag.text.strip() if date_posted_tag else 'N/A'

        job_description_tag = job.find('li', class_='job-desc')
        job_description = job_description_tag.text.strip() if job_description_tag else 'N/A'

        writer.writerow([job_title, company, date_posted, job_description])        # Writes each job as a new row in the CSV file

print('Scraping completed! Data saved in Aviation_Jobs.csv')
