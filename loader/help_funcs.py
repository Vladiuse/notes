import shutil
import os
from site_class import Site

def remove_utm(url):
    """Удалить utm метки с url"""
    if '?' in url:
        return url[:url.find('?')]
    return url


def get_zips_of_lands():
    """Заархивировать все папки в saved_lands"""
    my_list = os.listdir(Site.DIR_TO_LOAD)
    for dir_name in my_list:
        path_to_dir = os.path.join(Site.DIR_TO_LOAD, dir_name)
        try:
            shutil.make_archive(path_to_dir, 'zip', path_to_dir)
        except NotADirectoryError as error:
            print(f'{error}: {path_to_dir}')
    print("Sites zip's")



def get_url_data_from_file(with_geo=False):
    """
    Читает файл и возвращает список словарей ссылок и гео
     """
    urls_data = []
    with open('urls.txt') as file:
        for line in file:
            if line.endswith('\n'):
                line = line[:-1]
            if with_geo:
                # url, geo = line.split('\t')
                data = line.split('\t')
                url, *geo = data
                geo = ' '.join(geo)
                urls_data.append({'url': url, 'geo': geo})
            else:
                url = line
                urls_data.append({'url': url, 'geo': ''})
    return urls_data