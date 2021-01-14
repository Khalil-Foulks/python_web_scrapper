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

def cache_mapping(cache, game_titles, game_info):
    for idx_g, game in enumerate(game_titles):
        if game not in cache:
            for idx_j, info in enumerate(game_info):
                if idx_g == idx_j:
                    cache[game] = [info]

        else:
            for idx_j, info in enumerate(game_info):
                if idx_g == idx_j:
                    old_val = cache[game]
                    old_val.append(info)   

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

    cache_mapping(cache, game_titles, dates)
    cache_mapping(cache, game_titles, scores)
    cache_mapping(cache, game_titles, platforms)
    
    # print(cache)
    
    for game in cache:
        print(f'''
        Game Name: {game} 
        Release Date: {cache[game][0]}, 2020
        Platforms: {cache[game][2].strip()} 
        Score: {remove(cache[game][1])} 
        ''')     


game_info()