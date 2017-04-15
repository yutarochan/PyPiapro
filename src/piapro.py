#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PyPiapro: Piarpo (ピアプロ) Python Interface for Data Mining
Author: Yuya Jeremy Ong (yuyajeremyong@gmail.com)
'''
import requests
from bs4 import BeautifulSoup

PIAPRO_BASE_URL = 'http://www.piapro.jp'

''' General Text List '''
def getLyricList(start_index=1, end_index=1):
    lyricList = []

    for i in range(start_index, end_index+1):
        # Initialize BeautifulSoup
        url = PIAPRO_BASE_URL + '/text/?page=' + str(i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        # Parse Query Listing
        lists = soup.findAll('li', class_='_item')

        for l in lists:
            soup = BeautifulSoup(str(l), 'html.parser')
            content = soup.findAll('a')[1]

            lyric = {}
            lyric['title'] = content.text
            lyric['url'] = content.get('href')

            lyricList.append(lyric)
    return lyricList

''' Querried List '''
def getQueryList(query, start_index=1, end_index=1):
    # Initialize BeautifulSoup
    url = PIAPRO_BASE_URL + '/content_list/?view=text&order=sd&tag=' + query + '&order=sd'
    lyricList = []

    for i in range(start_index, end_index+1):
        url += '&page=' + str(i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        # Parse Query Listing
        lists = soup.findAll('li', class_='_item')

        for l in lists:
            soup = BeautifulSoup(str(l), 'html.parser')
            content = soup.findAll('a')[1]

            lyric = {}
            lyric['title'] = content.text
            lyric['url'] = content.get('href')

            lyricList.append(lyric)

    return lyricList

def getLyrics(sub_url):
    # Initialize BeautifulSoup
    url = PIAPRO_BASE_URL + sub_url
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # Parse Text
    text = soup.findAll('p', class_='main_txt')[0].text
    return text

def saveLyrics(lyrics):
    if not os.path.exists('data/'):
        os.makedirs('data')
    for l in lyrics:
        print 'Write lyrics to ' + l['url'].split('/')[2]

        outfile = open('tmp/' + l['url'].split('/')[2] + '.txt', 'w')
        outfile.write(l['text'].encode('utf-8'))
        outfile.close()

if __name__ == '__main__':
    lyrics = getQueryList('切ない')
    # lyrics = getLyricList(1, 1)

    for i in range(0, len(lyrics)):
        url = lyrics[i]['url']
        lyrics[i]['text'] = getLyrics(url)
        print lyrics[i]['title']

    # Save Lyrics
    saveLyrics(lyrics)
