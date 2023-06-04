from time import sleep
import requests
from pynput import keyboard

lastKey = ''

#url = 'http://192.168.100.20:41111/v1/'
url = 'http://localhost:5001/v1/'

def youNeverStop():
    while True:
        try:
            slide = requests.get(url+'status/slide?chunked=false')
        # print(slide.text)
            if(slide.json()['current']['notes'] == 'Intro' and lastKey != 'a'):
                keyboard.press('a')
                keyboard.release('a')
                lastKey = 'a'
            if(slide.json()['current']['notes'] == ('V1' or 'V3') and lastKey != 'b'):
                keyboard.press('b')
                keyboard.release('b')
                lastKey = 'b'
            if(slide.json()['current']['notes'] == 'V2' and lastKey != 'c'):
                keyboard.press('c')
                keyboard.release('c')
                lastKey = 'c'

            sleep(0.5)
        except:
            pass

def hindsight():
    print()

def sinkingDeep():
    print()

def awaken():
    print()

def endlessPraise():
    print()

def wontLetGo():
    print()

def undefeated():
    print()

def singWhereverIgo():
    print()

def houseOfTheLord():
    print()

def weWillGo():
    print()

def main():
    while True:
        try:
            r = requests.get(url+'presentation/active?chunked=false')
            song = r.json()['presentation']['id']['name'] 
            if(song in 'You Never Stop'):
                print(song)
            elif(song in 'Hindsight'):
                print(song)
            elif(song in 'Sinking Deep'):
                print(song)
            elif(song in 'Awaken'):
                print(song)
            elif(song in 'Endless Praise'):
                print(song)
            elif(song in "Won't Let Go"):
                print(song)
            elif(song in 'Undefeated'):
                print(song)
            elif(song in 'Sing Wherever I Go'):
                print(song)
            elif(song in 'House Of The Lord'):
                print(song)
            elif(song in 'We Will Go'):
                print(song)
            
        except:
            pass

main()