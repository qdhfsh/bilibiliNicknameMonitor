# coding:gbk

import requests
import time
import pygame
from bs4 import BeautifulSoup
from builtins import input


url = "https://space.bilibili.com/"

muc = "dididi.mp3"
pygame.mixer.init()
musicTrack = pygame.mixer.music.load(muc)

page = requests.get(url)

if len(url) == 27:
    UID = input("输入监控的UID: ")
    url += UID
    print("开始监控...")

page = requests.get(url)

while(page.status_code == 404):
    url = "https://space.bilibili.com/"
    UID = input("用户不存在重新输入UID: ")
    url += UID
    page = requests.get(url)
    
soup = BeautifulSoup(page.content,'html.parser')
oriName = soup.find('title').string[:-35]
    
while True:
    page = requests.get(url)

    if (page.status_code == 200):
          
        soup = BeautifulSoup(page.content,'html.parser')
        usrName = soup.find('title').string[:-35]
        print(usrName)
        if(usrName != oriName):
            pygame.mixer.music.play(-1)
            print("名字修改了！原来的名字："+ oriName)
        time.sleep(10)
          
    elif (page.status_code == 404):
        print("!404PAGE!")
        time.sleep(10)
          
    else:
        print("!Wrong!")
        time.sleep(10)
    