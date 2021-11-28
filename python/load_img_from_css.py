import os

import requests as req
from bs4 import BeautifulSoup
from shutil import copy2

def copy_modal_files(dir_to_save):
    # modal_dir = 'C:\\Users\\Влад\\OneDrive\\Рабочий стол\\lands\\modal'
    modal_dir = '/home/vlad/lands/modal/'
    modal_css = modal_dir + '/' + 'modal.css'
    modal_js = modal_dir + '/' + 'modal.js'
    for file in modal_css, modal_js:
        copy2(file, dir_to_save)
    print('Files copy Modal')

def find_css(main_dir):
    all_dirs = os.walk(main_dir)
    css_files = []
    for path, dirs, files in all_dirs:
        for name in files:
            if name.endswith('.css'):
                # css = {'path': path, 'name': name}
                css = path + '/' + name
                css_files.append(css)

    return css_files




def find_img_css(css_path):
    img_urls = []
    with open(css_path, encoding='utf-8') as css_file:
        for line in css_file:
            # if 'sblock' in css_path:
            #     print(line)

            if 'background' in line and 'url' in line:
                for char in [' ', '"', "'"]:
                    line = line.replace(char, '')
                start = line.find('url(')
                end = line.find(')', start)
                path = line[start + 4:end].strip('.')
                if 'url(' not in path:
                    img_urls.append(path)
    # print(css_path, img_urls)
    return img_urls


def get_image_name(url):
    point_pos = url.rfind('/')
    name = url[point_pos + 1:]
    # print(name)
    return name


def save_image_from_url(response_image, path_to_save):
    with open(path_to_save, 'wb') as file:
        for chunk in response_image:
            file.write(chunk)
        print('**************SUCCESS**************')


#
# def get_random_name():
#     abc = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#     name = ''
#     while len(name) < 5:
#         name += r.choice(abc)
#     return name
HTML_PATH = ''
def get_orig_url_from_html(dir):
    global HTML_PATH
    files = os.listdir(dir)
    for file_name in files:
        if file_name.endswith('.html'):
            HTML_PATH = dir + '/' + file_name
            with open(dir + '/' + file_name, encoding='utf-8') as html_file:
                for line in html_file:
                    if '<!-- saved from' in line:
                        start = line.find('http')
                        end = line.find(' -->', start)
                        url = line[start:end]
                    # else:
                    #     url = ''
    if '?' in url:
        url = url[:url.find('?')]

    return url
def check_sharp_links(main_dir):

    main_dir_ = main_dir

    for file in os.listdir(main_dir_):
        if file.endswith('.html'):
            with open(f'{main_dir_}/{file}', encoding='utf-8') as file:
                text = file.read()
            break
    soup = BeautifulSoup(text, 'lxml')
    links = soup.find_all('a')
    hrefs = []
    for link in links:
        try:
            hrefs.append(link['href'])
        except KeyError:
            print(f'No href: {link}')

    for i in hrefs:
        print('#' in i, i)
    DROP_LINKS = ['policy.html', 'terms.html', '.png', '.jpg', '.jpeg']
    print('Есть ссылки!!' if not all([href.startswith('#') for href in hrefs if href not in DROP_LINKS]) else 'Все ок')




# main_dir = 'C:\\Users\\Влад\\OneDrive\\Рабочий стол\\lands\\'
main_dir = '/home/vlad/lands/'
dir_name = 'auto_organaizer'
main_dir += dir_name
MAIN = None
CHECK_LINKS = None
COPY_MODAL = None

START = False


if START:
    MAIN = True
    COPY_MODAL = True
else:
    CHECK_LINKS = True

if MAIN:
    # URL = 'http://modelchehol.xcartpro.com/r1'
    URL = get_orig_url_from_html(main_dir)
    # URL = 'https://lifeproducti.com/assets_page/db435ae4aa7848df1933ae897becf02f368d47f1/'
    print(URL)
    URL += ''  # уточнение нахождения картинов
    css_files = find_css(main_dir)
    print(f'файлов css: {len(css_files)}')
    print(css_files)
    for file in css_files:
        urls = find_img_css(file)
        # print(urls)
        for url in urls:
            # print('img url ', url)
            url = url.strip('../')
            if len(url) == 0:
                print('NO LEN IMAGE URL')
                continue
            # URL = 'https://kazax-domenm1.xyz/assets_page/e14627c23740595bdac235c4b05c83cf66789a0d/'
            image_url = URL + url
            print(image_url)
            headers = {
                'User-Agent': 'My User Agent 1.0',
                'From': 'youremail@domain.com'  # This is another valid field
            }
            res = req.get(image_url, headers=headers)
            # print(res.status_code, '<html>' not in res.text)
            if '<html>' not in res.text:
                # name = get_random_name()
                try:
                    os.mkdir(main_dir + '/images')
                except FileExistsError:
                    pass
                dir_to_save = main_dir + '/images/' + get_image_name(image_url)
                save_image_from_url(res, dir_to_save)
            else:
                print('skip img')




if CHECK_LINKS:
    check_sharp_links(main_dir)
if COPY_MODAL:
    copy_modal_files(main_dir)

# test problems
# http://mimishkaa.xcartpro.com/d1/?off=rrXzTYqd&lnk=39653&m=f5cc7b948b61 - бэкграунд в html!