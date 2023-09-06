#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

import os
import requests
import time
import sys

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'


def banner():
    print(f"""
{Kırmızı} __  __            _     _            {Cyan} _   _       _                   
{Kırmızı}|  \/  | ___  _ __| |__ (_)_   _ ___  {Cyan}| | | | ___ | |_ __ ___   ___  ___         
{Kırmızı}| |\/| |/ _ \| '__| '_ \| | | | / __| {Cyan}| |_| |/ _ \| | '_ ` _ \ / _ \/ __|       
{Kırmızı}| |  | | (_) | |  | |_) | | |_| \__ \ {Cyan}|  _  | (_) | | | | | | |  __/\__ \         
{Kırmızı}|_|  |_|\___/|_|  |_.__/|_|\__,_|___/ {Cyan}|_| |_|\___/|_|_| |_| |_|\___||___/      
{Yeşil}
Author: {AUTHOR}
Instagram: {INSTAGRAM}
Github: {GİTHUB}
""")
 
def animasyon(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 100)

def hızlı_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 250)

def insta_ara(ğ):
    curl = 'https://instagram.com/'+ ğ + '/'
    try :
         openurl = urllib.request.urlopen(curl)
         print("\n")
         print(f"{Yeşil}Şüphelinin instagramı bu olabilir: "+curl)
         print("\n")
         print(f"{Beyaz}======================================================================")
    except urllib.error.URLError as msg :
         pass
    except KeyboardInterrupt:
      print('Hosca kal reis, kolay gelsin')
      time.sleep(3)
      sys.exit()


def ara(ğ):
     hesaplar = ['https://www.facebook.com/', "https://www.twitter.com/","https://www.twitter.com/","https://www.youtube.com/","https://plus.google.com/","https://www.reddit.com/user/", "https://www.pinterest.com/", "https://www.github.com/","https://www.flickr.com/people/","https://steamcommunity.com/id/","https://vimeo.com/","https://soundcloud.com/", "https://disqus.com/", "https://medium.com/@","https://vk.com/", "https://about.me/", "https://imgur.com/user/", "https://flipboard.com/","https://slideshare.net/","https://fotolog.com/", "https://open.spotify.com/user/","https://www.mixcloud.com/","https://www.scribd.com/","https://www.badoo.com/en/","https://www.patreon.com/","https://bitbucket.org/","https://www.dailymotion.com/","https://www.etsy.com/shop/","https://cash.me/","https://www.behance.net/","https://www.goodreads.com/","https://www.instructables.com/member/","https://keybase.io/","https://kongregate.com/accounts/","https://angel.co/","https://last.fm/user/","https://dribbble.com/","https://www.codecademy.com/","https://en.gravatar.com/","https://pastebin.com/u/","https://foursquare.com/","https://www.roblox.com/user.aspx?username=","https://www.gumroad.com/","https://www.wattpad.com/user/","https://www.canva.com/","https://creativemarket.com/","https://www.trakt.tv/users/","https://500px.com/","https://buzzfeed.com/","https://tripadvisor.com/members/","https://houzz.com/user/","https://blip.fm/","https://www.wikipedia.org/wiki/User:","https://news.ycombinator.com/user?id=","https://www.codementor.io/","https://www.reverbnation.com/","https://www.designspiration.net/","https://www.bandcamp.com/","https://www.colourlovers.com/love/","https://www.ifttt.com/p/","https://www.ebay.com/usr/","https://www.okcupid.com/profile/","https://www.trip.skyscanner.com/user/","https://ello.co/","https://tracky.com/user/"]
     for i in hesaplar:
       url = i+ğ+'/'
       try:
            openurl = urllib.request.urlopen(curl)

            print("\n")
            print(f"{Yeşil}Şüpheli kişi bu olabilir:  "+curl)
            print("\n")
            print("======================================================================")
       except  urllib.error.URLError as msg :
            pass
       except KeyboardInterrupt:
            print('Hosca kal reis, kolay gelsin')
            time.sleep(2)
            sys.exit()

animasyon(f"{Cyan}[!] Morbius Holmes başlatılıyor [!]")
time.sleep(3)

os.system('clear')
banner()

isim = input(f'{Beyaz}Hedefin İsmi(Küçük Harflerle Yazınız): {Yeşil}')

soyisim = input(f'{Beyaz}Hedefin Soyismi: {Yeşil}')

nick = input(f'{Beyaz}Hedefin Kullandığı/Kullanması Muhtemel Nick: {Yeşil}')

print('\n')
print(f'{Beyaz}{Kalın}İnstagram:{Yeşil}')
insta_list = [isim+'.'+soyisim, isim +'_'+ soyisim, isim + soyisim, nick,'_'+ isim + soyisim+'_', isim+ soyisim, isim + soyisim + 'official', 'official' + isim, 'official' + soyisim, 'official' + soyisim + isim, nick , isim + '.' + soyisim + 'official',isim + '_' + soyisim + 'official' ,'official' + isim, 'official' + soyisim, 'official' + soyisim + isim ]

print(f"{Beyaz}======================================================================")
for i in insta_list:
        insta_ara(i)

hızlı_ani(f'{Beyaz}{Kalın}İnstagram Hariç Diğer Hesaplar:{Bitir}')

print(f"{Beyaz}======================================================================")
ara(nick)