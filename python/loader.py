from seleniumwire import webdriver  # Import from seleniumwire
import time
from urllib.parse import urlparse
import os
import requests as req
from color_print import prGreen, prRed, prBlack, prYellow
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

HEADERS = {
    'User-Agent': USER_AGENT,
}

def remove_utm(url):
    """Удалить utm метки с url"""
    if '?' in url:
        return url[:url.find('?')]
    return url

TIME_TODO_SOME = 10
class Driver:
    """Класс управление chromedriver"""
    STEP_PX = 250
    STEP_TIME = 0.5
    SCROLL_START_PAUSE = 1.2
    DIE_TIME = 1
    KLOAK = False

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1400,1000")
        self.driver = webdriver.Chrome(options=options)

    def open_page(self, url):
        self.driver.get(url)

    def get_html_content(self):
        return self.driver.page_source

    def scroll_page_down(self):
        """Проскролить страницу вниз"""
        elem = self.driver.find_element(by='tag name', value='body')
        # location = e.location
        size = elem.size
        w, h = size['width'], size['height']
        y = 0
        time.sleep(Driver.SCROLL_START_PAUSE)
        while y <= h:
            time.sleep(Driver.STEP_TIME)
            self.driver.execute_script(f"window.scrollTo(0, {y})")
            y += Driver.STEP_PX

    def get_all_req_urls(self):
        """Получить все запросы выполненые браузером"""
        urls = set()
        for request in self.driver.requests:
            if request.response:
                urls.add(request.url)
                print(request.url)
            else:
                prRed(request.url)
        return urls

    def die(self):
        time.sleep(Driver.DIE_TIME)
        self.driver.close()


class Site:
    FIX_BASE_TAG_PATH = True
    REMOVE_IMG_SRCSET = True
    IGNORED_URLS = [
        'accounts.google.com',
        'fonts.googleapis.com',
    ]
    DIR_TO_LOAD = '/home/vlad/lands/work/saved_sites/'

    def __init__(self, url, req_urls: set, sours_html=''):
        self.url = url
        self.req_urls = req_urls
        self.main_page = sours_html
        self.dir_save_files = ''
        self.base_tag = False
        self.path_to_remove = ''

    def process(self):
        self.req_urls.remove(self.url)
        self.make_site_dir()
        self.load_main_page()
        self.fix_main_page()
        self.clean_req_urls()
        self.load_n_save_files()

        with open(os.path.join(self.dir_save_files, 'index.html'), 'w') as file:
            file.write(str(self.main_page))

    def fix_main_page(self):
        """Внесение изменений в главную страницу"""
        if Site.FIX_BASE_TAG_PATH:
            self.find_remove_base_tag()
        if Site.REMOVE_IMG_SRCSET:
            self.img_src_remove()

    def load_main_page(self):
        """Загрузить главную страницу"""
        res = req.get(self.url, headers=HEADERS)
        if Driver.KLOAK:
            if len(res.text) < len(self.main_page):
                prRed('Load MAIN From DriverSource')
            else:
                self.main_page = res.text
                prRed('Load MAIN From Request')
        else:
            prRed('Load MAIN From Request')
            self.main_page = res.text

    def find_remove_base_tag(self):
        """Пооиск и удаление тэга <base>"""
        soup = BeautifulSoup(self.main_page, 'lxml')
        base_tag = soup.find('base')
        try:
            href = base_tag['href']
            # path_to_remove = os.path.dirname(href)
            # if not path_to_remove.startswith('/'):
            #     path_to_remove = '/' + path_to_remove
            # self.base_tag = True
            # self.path_to_remove = os.path.normpath(path_to_remove)
            # prYellow(f'Remove path: {self.path_to_remove}')
        except TypeError:
            prRed(f'BaseHref not found : {base_tag}')
        else:
            path_to_remove = os.path.dirname(href)
            if not path_to_remove.startswith('/'):
                path_to_remove = '/' + path_to_remove
            self.base_tag = True
            self.path_to_remove = os.path.normpath(path_to_remove)
            prYellow(f'Remove path: {self.path_to_remove}')
        for base_tag in soup.select('base'):
            base_tag.extract()
        self.main_page = soup

    def img_src_remove(self):
        """Удаление тега <srcset> у картинок"""
        for tag in self.main_page.find_all('img', srcset=True):
            del(tag['srcset'])

    def load_n_save_files(self):  # TODO - что если файл без расширения?? будет ошибка!
        """Загрузка файлов и запись"""
        for url in self.req_urls:
            file_path = urlparse(url).path
            if file_path.startswith('/'):
                file_path = file_path[1:]
            file_path = os.path.join(self.dir_save_files, file_path)
            if self.base_tag:
                file_path = file_path.replace(self.path_to_remove, '')
            dir_path = os.path.split(file_path)
            if not os.path.exists(dir_path[0]):
                os.makedirs(dir_path[0])
            res = req.get(url, headers=HEADERS)
            if res.status_code == 200:
                print(f'file_path: {file_path}')
                if '%20' in file_path:
                    file_path = file_path.replace('%20', ' ')
                with open(file_path, 'wb') as file:
                    for chunk in res:
                        file.write(chunk)
                prGreen(f'Load n write: {url}')
            else:
                prRed(f'No connect to: {url}')

    def make_site_dir(self):
        """Формирует путь для сохранения файлов"""
        domain = urlparse(self.url).netloc
        path_to_save = os.path.join(Site.DIR_TO_LOAD, domain)
        if not os.path.exists(path_to_save):
            os.mkdir(path_to_save)
        self.dir_save_files = path_to_save

    def clean_req_urls(self):
        """Убрать сторонние ссылки из списка"""
        req_urls = set()
        domain_name = urlparse(self.url).netloc
        for req_url in self.req_urls:
            if domain_name in req_url:
                req_urls.add(req_url)
            else:
                prRed(f'Dropped: {req_url}')
        self.req_urls = req_urls


URL = 'http://liquidmetal.xcartpro.com/r1/?off=kKbaUdZV&lnk=40854&m=50d1484c33d9'
LOADED_URL = remove_utm(URL)
driver = Driver()
driver.open_page(LOADED_URL)
driver.scroll_page_down()
source_code = driver.get_html_content()
time.sleep(TIME_TODO_SOME)
driver.get_all_req_urls()
driver.die()

site = Site(
    LOADED_URL,
    req_urls=driver.get_all_req_urls(),
    sours_html=source_code,
)
site.process()
