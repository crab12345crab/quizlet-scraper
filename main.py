from bs4 import BeautifulSoup
import requests
import csv

scrape_site = input("Type Quizlet URL to be Scraped:")
html_req = requests.get(scrape_site, headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
})
print(html_req)

soup = BeautifulSoup(html_req.text, 'html.parser')
for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
    data = [question.get_text(strip=True),answer.get_text(strip=True)]
    print(data)
    f = open("quizlet.csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
