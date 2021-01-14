from bs4 import BeautifulSoup
import requests
import time

def game_scrapper(page_num=70):
    # grabs and prints all game titles on a page
    page_num = page_num
    URL = f'https://opencritic.com/browse/all/2020?page={page_num}'
    print(URL)
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'lxml')

    games_list = soup.find_all('div', class_='row no-gutters py-2 game-row align-items-center')
    # print(games_list)

    # scrapper go through every page
    if len(games_list) > 0:
        for games in games_list:
            # print(games)
            game_rank = games.find('div', class_='rank').text
            game_name = games.find('div', class_='game-name col').text
            release_dates = games.find('div', class_='first-release-date').text
            game_scores = games.find('div', class_='score').text.strip()
            game_platforms = games.find('div', class_='platforms').text.strip()
            game_link = 'https://opencritic.com' + games.a['href']

            # print(f'Game Rank: {game_rank}')
            print(f'Game Name: {game_name}')
            print(f'Release Date: {release_dates}, 2020')
            print(f'Platforms: {game_platforms}')
            print(f'Score: {game_scores}')
            print(f'Link: {game_link}')

            print('')
        page_num += 1
        game_scrapper(page_num)

    else:
        return

    
    # print(games_list)

# runs the game scrapper every set number of minutes
if __name__ == '__main__':
    while True:
        game_scrapper()
        #time in minutes
        time_wait = 1 
        print('')
        print(f'Waiting {time_wait} minute(s)...')
        time.sleep(time_wait * 60)