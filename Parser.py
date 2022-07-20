import requests #Парсинг
from bs4 import BeautifulSoup #Извлечение из данных
import random

page = 1 #Страница сайта
counter = 0 #Счётчик записей

while True:
    url = f"https://ruo.morsmusic.org/top?page={page}"

    r = requests.get(url).text

    b = BeautifulSoup(r,"lxml")
    headers = b.find_all("div",{"class":"wrapper-elem header-info header-info-single"}) #Заголовок с 1 страницы
    search_of_track = b.find_all("div",{"class":"track-info"}) #Информация по каждому треку

    if len(search_of_track)!=0: #Пока существует информация на странице
        if(page==1): #Только на 1-ой странице есть заголовок
            for header in headers:
                print(header.text) #Вывод заголовка

        with open("TOP OF TRACKS.txt",'a',encoding="UTF-8") as f: #Запись данных в файл
            for i in search_of_track:
                counter += 1
                link = i.find('a').get('href') #Получаем ссылку на каждый трек
                name_of_track = " ".join(i.text.split()) #Название трека
                f.write(f"{counter}. {name_of_track} https://ruo.morsmusic.org{link}\n") #Название + ссылка
                f.write("-------------------------------------------------\n")
            page += 1 #Переходим к следующей странице
    else:
        break

with open("TOP OF TRACKS.txt",'r',encoding="UTF-8") as f: #Читаем файл с данными и выводим на экран
    s = f.readlines()
    for i in s:
        print(i)

