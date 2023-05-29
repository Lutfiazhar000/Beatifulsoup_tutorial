# import library
from bs4 import BeautifulSoup
import requests
import time

# get html text
print('put skil that you are not familiar with')
unfamiliarSkill = input('>>')
print(f'filtering out {unfamiliarSkill}')

def findJobs():
    htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
    soup = BeautifulSoup(htmlText, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publishedDate = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in publishedDate:
            companyName = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            level = job.find('ul', class_ = 'top-jd-dtl clearfix').li.text
            if 'card_travel' in level:
                level = level.replace('card_travel', '')
            city = job.find('ul', class_ = 'top-jd-dtl clearfix').find_all('li')[1].span.text
            description = job.header.h2.a['href']
            if unfamiliarSkill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"company name: {companyName.strip()}")
                    f.write(f"experience: {level}")
                    f.write(f"required skill: {skills.strip()}")
                    f.write(f"description: {description}")
                    f.write(f"city: {city}")
                print(f'file saved: {index}')

if __name__ == '__main__':
    while True:
        findJobs()
        timeWait = 10
        print(f"waiting {timeWait}")
        time.sleep(timeWait *60)