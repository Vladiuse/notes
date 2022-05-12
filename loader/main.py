import time

from color_print import *

from driver import Driver

from help_funcs import *

TIME_TODO_SOME = 1
ZIP_AFTER = False


urls_from_file = get_url_data_from_file(with_geo=True)
for url_data in urls_from_file:
    url = url_data['url']
    geo = url_data['geo'] + '_' if url_data['geo'] else ''
    # LOADED_URL = remove_utm(URL)
    driver = Driver()
    driver.open_page(url)
    driver.scroll_page_down()
    source_code = driver.get_html_content()
    time.sleep(TIME_TODO_SOME)
    driver.get_all_req_urls()
    driver.die()

    site = Site(
        url,
        req_urls=driver.get_all_req_urls(),
        sours_html=source_code,
        add_prefix=geo,
        rename=True,
    )
    site_dir = os.path.join(site.DIR_TO_LOAD, site.dir_save_files)
    try:
        site.process()
    except BaseException as error:
        error_msg = f'SiteError{error}: {site_dir}'
        prRed(error_msg)
        shutil.rmtree(site_dir)
        with open('log.txt', 'a') as log_file:
            log_file.write(error_msg + '\n')

if ZIP_AFTER:
    get_zips_of_lands()
