from selenium import webdriver
import time
driver = webdriver.Chrome('/Users/bibekrai/workspace/DS_salary/Scraping/chromedriver')
driver.get('https://www.glassdoor.com/profile/login_input.htm')
url="https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm"
username = driver.find_element_by_name('username') 
password = driver.find_element_by_name('password')  
from decouple import config

username = config('username', default='')
password = config('password', default='')


username.send_keys('username')
password.send_keys('password')  
driver.find_element_by_class_name('gd-ui-button').click()

driver.get('https://www.glassdoor.com/Job/jobs.htm')
search = driver.find_element_by_id('sc.keyword')
search.send_keys('data analyst')
location = driver.find_element_by_id('sc.location')  
location.clear()  
location.send_keys('New York, NY')  
driver.find_element_by_id('HeroSearchButton').click()

# Loop through job postings and scrape data  
jobs = driver.find_elements_by_css_selector('[data-test=”jobListing”]')  
for job in jobs:  
      title = job.find_element_by_css_selector('[data-test=”jobTitle”]').text 
      company = job.find_element_by_css_selector('[data-test=”jobListingHeader”]').text 
      try:  salary = job.find_element_by_css_selector('[data-test=”salary”]').text  
      except:  salary = 'Not available'  
      print('Job title:', title)
      print('Company:', company)
      print('Salary:', salary)
      print('\n')
time.sleep(3)
driver.quit()