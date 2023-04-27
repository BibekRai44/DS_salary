import requests
from bs4 import BeautifulSoup
url="https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm"
response=requests.get(url)
html_content=response.content

soup=BeautifulSoup(html_content,'html.parser')
print(response)