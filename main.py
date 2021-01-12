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
URL = 'https://opencritic.com/browse/all/2020'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

games = soup.find_all('div', class_='game-name col')
release_dates = soup.find_all('div', class_='first-release-date')
game_scores = soup.find_all('div', class_='score')
game_platforms = soup.find_all('div', class_='platforms')

def remove(string): 
    return string.replace(" ", "") 

def game_info():
    cache = {}
    game_titles = []
    dates = []
    scores = []
    platforms = []

    for game in games:
        game_titles.append(game.text)

    for date in release_dates:
        dates.append(date.text)

    for score in game_scores:
        scores.append(score.text)    
    
    for platform in game_platforms:
        platforms.append(platform.text)

    # print(game_titles)
    # print(dates)
    # print(scores)
    # print(platforms)
    # print('')

    for idx_g, game in enumerate(game_titles):
        for idx_d, date in enumerate(dates):
            if idx_g == idx_d:
                cache[game] = [date]

        for idx_s, score in enumerate(scores):
            if idx_g == idx_s:
                old_val = cache[game]
                old_val.append(score)
        
        for idx_p, plat in enumerate(platforms):
            if idx_g == idx_p:
                old_val = cache[game]
                old_val.append(plat)
    
    # print(cache)

    for game in cache:
        print(f'{game} released on {cache[game][0]} for "{remove(cache[game][2])}" and recieved an avg score of {remove(cache[game][1])}')


game_info()