from bs4 import BeautifulSoup
import urllib.request
from gtts import gTTS
import time
from mutagen.mp3 import MP3
import winsound as ws
from pygame import mixer


def reader(s):
	tts = gTTS(text=s,lang='en')
	tts.save('greeting.mp3')
	
	f=MP3("greeting.mp3")
	n=f.info.length
	mixer.init()
	mixer.music.load('greeting.mp3')
	mixer.music.play()
	time.sleep(n)


sauce = urllib.request.urlopen('https://news.google.co.in/').read()
soup=BeautifulSoup(sauce,'html.parser')
b=soup.body
y=''
m=''

for x in b.find_all('div', class_='esc-lead-article-title-wrapper'):
	y="\n"+x.text+"\n"
	reader(y)