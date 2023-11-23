from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# User input for job title and location
keyword = input("Enter the job Title: ")
location = input("Enter the location: ")

# Open Chrome browser and navigate to LinkedIn 
driver=webdriver.Chrome()
driver.get("https://in.linkedin.com/")
driver.maximize_window()

time.sleep(5)
# Enter login credentials and sign in
username=driver.find_element(By.ID,"session_key")
username.send_keys("YOUR USERNAME")                  #ENTER YOUR MAIL ID HERE

pwd=driver.find_element(By.ID,"session_password")
pwd.send_keys("YOUR PASSWORD")                       #ENTER YOUR PASSWORD HERE

submit=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
submit.click()


# Format the user input into URL format
#HERE cureentJobId=3764374451 is for ENTRY LEVEL JOBS.If you want any other EXPERIENCE LEVEL you just change the number by vsiting the linkedin jobs page
formatted_keyword = keyword.replace(" ", "%20")
formatted_location = location.replace(" ", "%20")
url = f"https://www.linkedin.com/jobs/search/?currentJobId=3764374451&keywords={formatted_keyword}&location={formatted_location}&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true"
driver.get(url)

time.sleep(15)
# Scrape job titles from the page
jobs_src= driver.page_source
soup = BeautifulSoup(jobs_src,'html.parser')
time.sleep(3)

jobs_html = soup.find_all('a', class_='ember-view job-card-container__link job-card-list__title')

jobs_title=[]

if jobs_html:
    for title in jobs_html:
        jobs_title.append(title.text.strip())
    print(jobs_title) 
else:
    print("No elements found")

    

time.sleep(10)














