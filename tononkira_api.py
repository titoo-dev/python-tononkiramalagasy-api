from requests import get
from bs4 import BeautifulSoup

#  those urls is for testing
# 'https://tononkira.serasera.org/tononkira/hira/index/903/0'
# 'https://tononkira.serasera.org/tononkira/hira/index/34/20'

def get_artists(page = 0):
    url = 'https://tononkira.serasera.org/tononkira/mpihira/results/'
    artists = []
    if page != 0:
        url = 'https://tononkira.serasera.org/tononkira/mpihira/results/{}'.format(page)
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data_odd = soup.find_all('tr', class_='odd')
    data_even = soup.find_all('tr', class_='even')

    for row in data_odd:
        song_url = row.find_all('td')[2].find('a')['href']
        artists.append({
            "id": int(row.find_all('td')[0].text.strip()),   
            "name": row.find_all('td')[1].text.strip(),
            "songsCount": int(row.find_all('td')[2].text.strip()),
            "songsIndex": song_url.split('/')[-2],
        })
    
    for row in data_even:
        song_url = row.find_all('td')[2].find('a')['href']
        artists.append({
            "id": int(row.find_all('td')[0].text.strip()),   
            "name": row.find_all('td')[1].text.strip(),
            "songsCount": int(row.find_all('td')[2].text.strip()),
            "songsIndex": song_url.split('/')[-2],
        })
    artists.sort(key=lambda x: x['id'])
    return artists

def get_artist_songs(index, page):
    index = index
    url = 'https://tononkira.serasera.org/tononkira/hira/index/{}/{}'.format(index, page)
    songs = []
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data_odd = soup.find_all('tr', class_='odd')
    data_even = soup.find_all('tr', class_='even')
    for row in data_odd:
        id = int(row.find_all('td')[0].text.strip())
        title = row.find_all('td')[1].text.strip()
        songs.append({
            "id": id,   
            "title": title,
            "content": row.find_all('td')[1].find('a')['href'],
        })

    for row in data_even:
        id = int(row.find_all('td')[0].text.strip())
        title = row.find_all('td')[1].text.strip()
        songs.append({
            "id": id,   
            "title": title,
            "content": row.find_all('td')[1].find('a')['href'],
        })
    
    songs.sort(key=lambda x: x['id'])
    return songs

def get_lyrics(title, artist):  
    url = 'https://tononkira.serasera.org/hira/{}/{}'.format(artist, title)
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all('div', class_='col l-2-3 s-1-1')
    b_tags = soup.find_all('b')
    a_tags = soup.find_all('a')

    for b in b_tags:
        b.decompose()
    
    for a in a_tags:
        a.decompose()

    return str(content[0].text.strip())

def get_all_songs(page):
    url = 'https://tononkira.serasera.org/tononkira/hira/results/{}'.format(page)
    html = get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    data_odd = soup.find_all('tr', class_='odd')
    data_even = soup.find_all('tr', class_='even')

    songs = []

    for row in data_odd:
        songs.append({
            "id": int(row.find_all('td')[0].text.strip()),   
            "title": row.find_all('td')[1].text.strip(),
            "songUrl": row.find_all('td')[1].find('a')['href'],
            "artist": row.find_all('td')[2].text.strip(),
            "ArtistUrl": row.find_all('td')[2].find('a')['href'],
        })
    
    for row in data_even:
        songs.append({
            "id": int(row.find_all('td')[0].text.strip()),   
            "title": row.find_all('td')[1].text.strip(),
            "songUrl": row.find_all('td')[1].find('a')['href'],
            "artist": row.find_all('td')[2].text.strip(),
            "ArtistUrl": row.find_all('td')[2].find('a')['href'],
        })
    
    songs.sort(key=lambda x: x['id'])
    
    return songs