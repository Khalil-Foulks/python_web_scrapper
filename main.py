from bs4 import BeautifulSoup
import requests

# grabs and prints all news article titles on a page
# URL = 'https://opencritic.com'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'lxml')
# news_article_titles = soup.find_all('h3')

# # print(soup.prettify())

# # print(news_article_titles)

# for title in news_article_titles:
#     print(title.text)

#--------------------------

# grabs and prints all game titles on a page
URL = 'https://opencritic.com/browse/ps5/upcoming'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
games = soup.find_all('div', class_='game-name col')
release_dates = soup.find_all('div', class_='first-release-date')

# print(soup.prettify())

# print(titles)

for game in games:
    print(game.text)

for date in release_dates:
    print(date.text)