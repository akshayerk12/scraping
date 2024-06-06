import requests
from bs4 import BeautifulSoup

url = 'https://infopark.in/companies/job-search'
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text, 'lxml')
jobs = soup.find_all('div', {'class':"row company-list joblist"})
# print(jobs)
for job in jobs:
    title_element = job.find('a')
    title = title_element.text
    link = title_element['href']
    company = job.find('div', {'class':'jobs-comp-name'})
    company_name = company.text
    date = job.find('div', {'class':'job-date'}).text
    print(title, '-', company_name, '-', date)

    
    