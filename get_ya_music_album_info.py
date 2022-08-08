try:
    from yandex_music import Client
    from pprint import pprint
    import time
    import get_token
except ImportError:
    import os
    os.system('pip install yandex-music --upgrade')
    from yandex_music import Client
    from pprint import pprint
    import time
    import get_token

TOKEN = get_token.get_token()
client = Client(TOKEN).init()


def get_album_id():
    print('Зайдите на сайт: https://music.yandex.ru/home \nВыберите альбом, информацию о котором хотите получить. \n'
          'Из адресной строки скопируйте id альбома.\n')
    album_id = int(input('Album_id: '))
    return album_id


def get_info_for_album(album_id: int):
    album = {}
    album_info = client.albumsWithTracks(str(album_id))
    album['title'] = album_info['title']
    album['name_artist'] = album_info['artists'][0]['name']
    album['release_date'] = album_info['release_date'][0: 10]
    album['genre'] = album_info['genre']

    for i in range(len(album_info['volumes'][0])):
        valumes = {}
        valumes['title'] = album_info['volumes'][0][i]['title']
        valumes['id'] = album_info['volumes'][0][i]['id']
        duration_ms = int(album_info['volumes'][0][i]['duration_ms'])
        duration = time.strftime("%H:%M:%S", time.gmtime((duration_ms // 1000)))
        valumes['duration_ms'] = duration
        album.setdefault(f'volumes_{i}', valumes)

    pprint(album)


get_info_for_album(get_album_id())
