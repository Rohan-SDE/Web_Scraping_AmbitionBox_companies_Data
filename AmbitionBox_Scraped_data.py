import pandas as pd
import requests
from bs4 import BeautifulSoup
final = pd.DataFrame()
for j in range(1,2):
    url = f'https://www.ambitionbox.com/list-of-companies?page={j}&campaign=desktop_nav'
    
    headers = {"User-Agent": "Mozilla/5.0"}
    webpage = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage,'lxml')
    company = soup.find_all('div', class_ = 'companyCardWrapper')
    
    name = []
    rating = []
    reviews = []
    services = []
    jobs = []
    salary = []

    for i in company:
        name.append(i.find('h2').text.strip())

        rating_tag = i.find('div', class_='rating_text')

        if rating_tag:
            rating.append(rating_tag.text.strip())
        else:
            rating.append(None)
            
        services.append(i.find('span', class_ = 'companyCardWrapper__interLinking').text.strip())

        metrics = {}

        for item in i.find_all('a', class_='companyCardWrapper__ActionWrapper'):
            title = item.find('span', class_='companyCardWrapper__ActionTitle').text.strip()
            count = item.find('span', class_='companyCardWrapper__ActionCount').text.strip()

            metrics[title] = count

        reviews.append(metrics.get('Reviews'))
        jobs.append(metrics.get('Jobs')) 
        salary.append(metrics.get('Salaries'))

    d = {'Name':name, 'Ratings':rating, 'Reviews':reviews, 'Services/Location':services, 'Jobs':jobs, 'Salary':salary}
    print(
        len(name),
        len(rating),
        len(reviews),
        len(services),
        len(jobs),
        len(salary)
    )
    df = pd.DataFrame(d)
    
    final = pd.concat([final, df], ignore_index=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    
    print(final.to_string())
    final.to_csv('abitionbox_companies (1).xls', index=False)