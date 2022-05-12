from bs4 import BeautifulSoup
import os
from color_print import *
import requests as req
from urllib.parse import urlparse
#TODO  https://www.facebook.com/tr/?id= - попадают в запросы - пофиксить функцию отчистки
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
HEADERS = {
    'User-Agent': USER_AGENT,
}
class Site:
    FIX_BASE_TAG_PATH = False
    REMOVE_IMG_SRCSET = False
    KLOAK = False
    IGNORED_URLS = [
        'accounts.google.com',
        'fonts.googleapis.com',
    ]
    DIR_TO_LOAD = '/home/vlad/lands/work/saved_lands/'

    def __init__(self, url, req_urls: set, sours_html='', add_prefix='', rename=False):
        self.url = url
        self.req_urls = req_urls
        self.main_page = sours_html
        self.dir_save_files = ''
        self.base_tag = False
        self.path_to_remove = ''
        self.prefix = add_prefix
        self.rename = rename

        self.make_site_dir()


    def process(self):
        self.req_urls.remove(self.url)
        self.load_main_page()
        self.fix_main_page()
        self.clean_req_urls()
        self.load_n_save_files()

        # with open(os.path.join(self.dir_save_files, 'index.html'), 'w') as file:
        #     file.write(str(self.main_page))

    def fix_main_page(self):
        """Внесение изменений в главную страницу"""
        if Site.FIX_BASE_TAG_PATH:
            self.find_remove_base_tag()
        if Site.REMOVE_IMG_SRCSET:
            self.img_src_remove()

    def load_main_page(self):
        """Загрузить главную страницу"""
        res = req.get(self.url, headers=HEADERS)
        with open(os.path.join(self.dir_save_files, 'index.html'), 'wb') as file:
            for chunk in res:
                file.write(chunk)

        # if Site.KLOAK:
        #     if len(res.text) < len(self.main_page):
        #         prRed('Load MAIN From DriverSource')
        #     else:
        #         self.main_page = res.text
        #         prRed('Load MAIN From Request')
        # else:
        #     prRed('Load MAIN From Request')
        #     self.main_page = res.text

    # def load_main_page(self):
    #     """Загрузить главную страницу"""
    #     res = req.get(self.url, headers=HEADERS)
    #     if Site.KLOAK:
    #         if len(res.text) < len(self.main_page):
    #             prRed('Load MAIN From DriverSource')
    #         else:
    #             self.main_page = res.text
    #             prRed('Load MAIN From Request')
    #     else:
    #         prRed('Load MAIN From Request')
    #         self.main_page = res.text

    def find_remove_base_tag(self):
        """Пооиск и удаление тэга <base>"""
        soup = BeautifulSoup(self.main_page, 'lxml')
        base_tag = soup.find('base')
        try:
            href = base_tag['href']
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
            del (tag['srcset'])

    def load_n_save_files(self):  # TODO - что если файл без расширения?? будет ошибка!
        """Загрузка файлов и запись"""
        for url in self.req_urls:
            # url = url.replace('http://45.32.144.228/lander/chat-ro/', 'https://juwix.xyz/bixaj/')
            file_path = urlparse(url).path
            if file_path.startswith('/'):
                file_path = file_path[1:]
            file_path = os.path.join(self.dir_save_files, file_path)
            if self.base_tag:
                file_path = file_path.replace(self.path_to_remove, '')
            dir_path = os.path.split(file_path)
            if not os.path.exists(dir_path[0]):
                os.makedirs(dir_path[0])
            try:
                res = req.get(url, headers=HEADERS)
            except (ConnectionRefusedError, req.exceptions.ConnectionError) as error:
                prRed(f'ConnError: {url}')
            else:
                if res.status_code == 200:
                    print(f'file_path: {file_path}')
                    if '%20' in file_path:
                        file_path = file_path.replace('%20', ' ')
                    try:
                        with open(file_path, 'wb') as file:
                            for chunk in res:
                                file.write(chunk)
                        prGreen(f'Load n write: {url}')
                    except (IsADirectoryError, NotADirectoryError):
                        prRed(f'Error, not file: {url}')
                else:
                    prRed(f'No connect to: {url}')
        prRed('**** End LOAD ****')

    def make_site_dir(self):
        """Формирует путь для сохранения файлов"""
        domain_name = urlparse(self.url).netloc
        if self.prefix:
            domain_name = self.prefix + domain_name
        if self.rename:
            domain_name = self.prefix[:-1]
        path_to_save = os.path.join(Site.DIR_TO_LOAD, domain_name)
        print(path_to_save)
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

