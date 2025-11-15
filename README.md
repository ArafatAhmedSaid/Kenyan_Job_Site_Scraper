# 1. Project Title
Kenyan_Job_Site_Scraper (Aviation Jobs in MyJobMag)

# 2. Problem Statement:
- Finding recent and relevant aviation job opportunities in Kenya is time-consuming due to the fact that jobs are scattered across many websites. It is therefore inefficient to search for jobs manually via the browsers. This project aims to automate the process of gathering job from a Kenyan website and store them in a structured format for easier search, filtering, and analysis.

# 3. Objectives:
- To develop a Python web scraper that automat icallycollects job data from a Kenyan website  (MyJobMag).
- To extract key information from the website e.g. Job Title, Company Name, Location and Date Posted.
- To store the extracted data in a CSV file.
- To analyze the data to identify popular job roles and trends in Kenya.

# Dataset Description:
The following dataset features will be considered during the scraping process:
- Job Title
- Company Name
- Job Description
- Date Posted

# 4. Tools & Technologies:
The following libraries will be used/imported into Python using VS Code:
- requests
- BeautifulSoup
- csv

# 5. Proposed Methodology:
- Set up environment – Install and import the required libraries as listed above.
- Identify the target website (MyJobMag).
- Inspect the job listing (aviation) using ‘View Page Source’ or DevTools and identify relevant HTML tags.
- Data Extraction – Write a Python script to send a request to the website, parse the HTML content, and extract key job details.
- Data Storage – Save the extracted data into a structured CSV file.

# 6. Expected Outcomes:
- Python script that automatically scrapes job listings from a Kenya website.
- CSV file containing structured job listing data.
