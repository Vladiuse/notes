# Favacons from https://faviconka.ru/index.php?page=1
# 200, Page#: 32, Fav#:4507

import requests as req
from bs4 import BeautifulSoup
MAIN_URL = 'https://faviconka.ru/'
url = 'https://faviconka.ru/index.php?page='
fav_name_count = 1
with open('test.html') as file:
    text = file.read()
for page in range(1,1311):
    res = req.get(url + str(page))
    if res.status_code != 200:
        print(f'Page {page} not work')
    else:
        text = res.text
        soup = BeautifulSoup(text, 'lxml')
        fav_divs = soup.find_all('div', class_="col-4 col-sm-3 col-md-2 col-lg-1 col-xl-1")
        print(len(fav_divs))
        for div in fav_divs:
            img = div.find('img')
            try:
                fav_url = img['src']
                fav_url = MAIN_URL + fav_url
                res = req.get(fav_url)
                print(f'{res.status_code}, Page#: {page}, Fav#:{fav_name_count}, Url:{fav_url}')
                with open('favicons/' + str(fav_name_count) + '.ico', 'wb') as file:
                    for chunk in res:

                        file.write(chunk)
                fav_name_count += 1
            except TypeError:
                print('Error', img)
