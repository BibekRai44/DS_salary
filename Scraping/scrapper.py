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
time.sleep(3)
driver.get(url)