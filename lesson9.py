import os
import requests


def translate_it(file_src, file_dst, lang_src, lang_dst):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    # :param text: <str> text for translation.
    # :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180923T182530Z.59b000eb884fd4a7.25d1fa6936d14d616bfa39de9a960152facf8bf1'

    lang = f"{lang_src}-{lang_dst}"

    params = {
        'key': key,
        'lang': lang,
        'text': '',
    }
    buffer = ''
    with open(file_src, "r", encoding="UTF-8") as f:
        for line in f:
            buffer += line
                
    params['text'] = buffer
    response = requests.get(url, params=params ).json()
    result = ' '.join(response.get('text', []))
    
    with open(file_dst, "w", encoding='UTF-8') as file:
        file.write(result)


language_of_files = {
    'DE.txt': 'de',
    'ES.txt': 'es',
    'FR.txt': 'fr'
}

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'SRC')

dst_path = os.path.join(current_dir, 'DST')

if not os.path.exists(dst_path):
    os.mkdir(dst_path)

list_files = os.listdir(src_path)

for name_file in list_files:
    file_src = os.path.join(src_path, name_file)
    file_dst = os.path.join(dst_path, name_file)
    
    lang_src = ''
    lang_dst = 'ru'
    if  name_file not in language_of_files.keys():
        continue
    language = language_of_files[name_file]
    translate_it(file_src, file_dst, language, 'ru')