import requests
from bs4 import BeautifulSoup


# Extract, Transform, Load

# Extract: pulling html from the page
# Soup is an object that contains html parsed content from the url specified.
# The requests module uses specified user-agent, will likely randomize to avoid detection.

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    url = f'https://www.indeed.com/jobs?q=application%20security%20engineer&l=Remote&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


# Transform: find relevant data, make readable
# in div the relevant class that contains job information is listed as divs
# find the item 'span' because that is where the job title is found
# Problem returning job title, the first span tag is

def transform(soup):
    title_div = soup.find_all('div', class_='heading4 color-text-primary singleLineTitle tapItem-gutter')
    for item in title_div:
        title = item.find(lambda tag: tag.name == "span" and "title" in tag.attrs).text
        print(title)

    company_div = soup.find_all('div', class_='heading6 company_location tapItem-gutter companyInfo')
    for item in company_div:
        company = item.find('span').text
        print(company)

    salary_div = soup.find_all('div', class_='metadata salary-snippet-container')
    for item in salary_div:
        salary = item.find('div', class_="attribute_snippet").text
        print(salary)

    summary_div = item.find('div', class_='job-snippet').text
    for item in summary_div:
        summary = item.find(lambda tag: tag.name == "u1" and "marker" in tag.attrs).text
        print(summary)
    return

def joblist

c = extract(0)
transform(c)
