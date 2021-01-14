from bs4 import BeautifulSoup
import requests
import time
import os.path

# uncomment code below if reaching recursion limit
# import sys
# sys.setrecursionlimit(2000)

def game_scrapper(file_mode, page_num=1):
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
        for idx, games in enumerate(games_list):
            # print(games)
            game_rank = games.find('div', class_='rank').text.strip()
            game_name = games.find('div', class_='game-name col').text
            release_dates = games.find('div', class_='first-release-date').text
            game_scores = games.find('div', class_='score').text.strip()
            game_platforms = games.find('div', class_='platforms').text.strip()
            game_link = 'https://opencritic.com' + games.a['href']

            # print(f'Game Rank: {game_rank}')
            with open(f'games/game_list.txt', f'{file_mode}', encoding='utf-8') as f:
                # Move read cursor to the start of file.
                f.seek(0)
                f.write(f'Game Name: {game_name} \n')
                f.write(f'Release Date: {release_dates}, 2020 \n')
                f.write(f'Platforms: {game_platforms} \n')
                f.write(f'Score: {game_scores} \n')
                f.write(f'Link: {game_link} \n')
                f.write('\n')
            print(f'File saved: {game_name} at Rank:{game_rank} was added')
        page_num += 1
        # adds another page of games to txt file
        game_scrapper('a', page_num)

    else:
        return

    
    # print(games_list)

# runs the game scrapper every set number of minutes
if __name__ == '__main__':
    while True:
            # overwrites existing game_list txt file if it exists, otherwise creates a new file
            game_scrapper('w')
            # time in minutes
            time_wait = .5 
            print('')
            print(f'Waiting {time_wait} minute(s)...')
            time.sleep(time_wait * 60)