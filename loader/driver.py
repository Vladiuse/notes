from seleniumwire import webdriver  # Import from seleniumwire
import time
from color_print import *
class Driver:
    """Класс управление chromedriver"""
    STEP_PX = 100
    STEP_TIME = 0.05
    SCROLL_START_PAUSE = 0.5
    DIE_TIME = 1
    # KLOAK = False

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1400,1000",)
        self.driver = webdriver.Chrome(
            '/home/vlad/PycharmProjects/save_land/loader/chromedriver',
            options=options
        )

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

            else:
                prRed(request.url)
        return urls

    def die(self):
        time.sleep(Driver.DIE_TIME)
        self.driver.close()
