from bs4 import BeautifulSoup
import requests

def game_scrapper():
    # grabs and prints all game titles on a page
    URL = 'https://opencritic.com/browse/all/2020'
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'lxml')

    games_list = soup.find_all('div', class_='row no-gutters py-2 game-row align-items-center')

    for games in games_list:
        # print(games)
        game_name = games.find('div', class_='game-name col').text
        release_dates = games.find('div', class_='first-release-date').text
        game_scores = games.find('div', class_='score').text.strip()
        game_platforms = games.find('div', class_='platforms').text.strip()

        print(f'''
            Game Name: {game_name}
            Release Date: {release_dates}
            Platforms: {game_platforms}
            Score: {game_scores}
        ''')


    # print(games_list)
    


game_scrapper()