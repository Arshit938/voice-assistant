import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import os
import webbrowser
import random
import glob
import GoogleNews
import smtplib
import pywhatkit
import pyautogui
from pynput.keyboard import Key,Controller
from googlesearch import search
from youtubesearchpython import VideosSearch
import time

#all the work performed globaly ---->
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')# returns a list of voices in system
engine.setProperty('voice' , voices[1].id)# sets the voice from the diffrent voices
    
dt= datetime.datetime.now() 


#all the email_id in contacts are here
gmail_ids={'chetan': 'Chetanchawlaofficial@gmail.com',
           'garima' : 'kgarima0808@gmail.com',
           'arshit' : 'karshit48@gmail.com'

        }
#all the contacts 
contacts={'chetan' : '+919319888883 ',
          'ishan' : '+918607353361',
          'ankit' : '+919996458866',
          'anushk': '+918528701871',
          'anjali arora':'+917009921756',
          'bhumika' : '+919896633417',
          'pooja' : '+918569874194',
          'anjali kumari':'+916284402210',
          'mummy':'+918708997483',
          'papa':'+919255121931',
}        


# all the functions used -----> 


def speak(*sentence):
    '''
    this function takes a *arg(used to give multiple arguments when we dont know how many arguments will be there) as input and 
    pronounce it.this can take as many sentences as you want as input
    '''
    for s in sentence :
        engine.say(s)
        engine.runAndWait()

def great():
    '''
    this function greats the user with respect to current time
    it makes use of speak function
    '''
    hour=dt.hour
    if hour >= 4 and hour < 12:
        speak('good morning sir','i am coco','how may i help you')
    elif hour >= 12 and hour < 17:
        speak('good afternoon sir','i am coco','how may i help you')        
    elif hour >= 17 and hour < 23:
        speak('good evening sir','i am coco','how may i help you')
    elif hour >=0 and hour <= 4:
        speak('good evening sir','i am coco','how may i help you')    
def takeRequest():
    '''
    it is a function which is used to take voice commands from user

    COMPONENTS USED :
    ->recogniser is an object of Recognizer class
    ->Microphone is a class which represents the microphone in computer or headphones
    ->source is the input device used to capture audio
    ->listen() function is used to take audio from source
    ->recognize_google() is a function which recognize the audio and convert it into string and then returns the string
    '''
    recogniser=sr.Recognizer()
    recogniser.energy_threshold=400
    with sr.Microphone() as source :
        print("listening....")
        recogniser.pause_threshold=1.2
        audio = recogniser.listen(source=source)
    try:
        print("Recognising....")
        query=recogniser.recognize_google(audio_data=audio,language='en-in')
    except Exception as e:
        print("Unable to recognize")
        speak('i am unable to recognize it can you please say that again sir')
        query=takeRequest()   
    return query 
def tellTime():
    '''
    it tells the current time 
    '''
    hr=dt.hour
    min=dt.minute
    if hr >= 12 :
        time= str(hr-12) + ' , ' +str(min) +' '
        speak('it is ' + time + 'p m')
    else :
        time=str(hr) + ' , ' + str(min) + ' '
        speak('it is '+time+'a m')

def tellDate():
    '''
    it tells the current date
    '''
    date=dt.day
    month=dt.month
    year=dt.year 
    cd= str(date) + ' ' + str(month) + ' ' + str(year) + ' '
    speak('today is ' + cd)
               
def play_movie():
    '''
    this funnction searches a movie present in the device and plays it.If it didn't find the perticular movie you asked it will suggest
    you a movie
    it can also play a random movie if user asks for it
    attributes used----->
    ->movie_path: path of the folder in which all movies are present
    ->movie_folders: all the folders present in the movie_path dir
    ->query: the movie user wants to play
    ->random.randrange(): it is used to generate a random  number within given range
    ->os.chdir(): it is used to setup a directry from which to search
    ->glob.glob(): it is a constructor of glob class used to find a specific extension file
    ->os.startfile(): it is a function used to run a file at given location
    ->os.path.join() : it is used to join two paths 
    ->os.listdir() : is a function used to find list of all the directories present     
    '''
    movie_path='E:\\MOVIES'
    movie_folders=os.listdir(movie_path)
    speak('do you have any specific movie in mind')
    query=takeRequest().lower()
    index=-1
    if 'no' in query:
        index=random.randrange(len(movie_folders))
    else:
        movie_folders_copy=movie_folders
        for i in range(len(movie_folders_copy)):
            if query in movie_folders_copy[i].lower():
                index=i
        if index == -1:
            speak('movie is not present in the device...','let me suggest you one')
            index=random.randrange(len(movie_folders))
    updated_path=os.path.join(movie_path,movie_folders[index])
    os.chdir(updated_path)
    movie=glob.glob('*.mp4')
    if len(movie)==0:
        movie=glob.glob('*.mkv')
    os.startfile(os.path.join(updated_path,movie[0]))  

def play_music():
    '''
    it is used to play mp3 file present in your system
    components---->
    ->music_path: directory in which mp3 files are stored
    '''
    music_path='E:\\music'
    songs=os.listdir(music_path)
    index=random.randrange(len(songs))
    os.startfile(os.path.join(music_path,songs[index]))  

def search_from_wikipedia(query):
    '''
    searches from wiki pedia for summary
    '''
    result=wiki.summary(query,sentences=3)
    speak('according to wikipedia ', result)

def search_news():
    '''
    searches news from google and speaks it
    content:
    ->news:object of GoogleNews and '1d' represents period
    ->search():used to search news
    ->result():returns results from the search
    '''
    news=GoogleNews(period='1d')
    speak('do you want to hear news on sepcific subject ')
    query=takeRequest().lower
    if 'no' in query:
        sub='india headlines'
    else:
        sub=query
    news.search(sub)   
    result=news.result()
    speak(result)
    speak('thats all for today sir')

def send_mail(to,content) :
    '''
    it is used to send automated mails to a reciever 
    app_password : it is the password generated by google account to securely access the senders password name in gmail=python
    smtplib.SMTP : it is a function which is used to create a SMTP connection.Here 587 is port no,smtp.gmail.com is local host name
    .ehlo() : it is used to connect host to port
    .login(): it is used to authenticate the email and app_password    
    '''
    print('trying to send.......')
    senders_id='arshitk643@gmail.com'
    app_password='hmwsthcbxmbbvtio'
    try:
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()#encrypts the data
        server.login(senders_id,app_password)
        server.sendmail(senders_id,to,content)
        server.close()
        speak('email sent successfully')
    except Exception as e:
        speak('unable to send mail..')

def send_whatsapp_message(to,message):
    '''
    this function sends message automaticaly on whatsapp
    keyboard : it is a controller object which is used to control input from keyboard
    pyautogui.click():it is used to automaticaly click on screen
    keyboard.press(),keyboard.release():are function used to press and release specific key
    key.enter:it refrence to enter key on keyboard
    pywhatkit : it is used to send message on whatsapp using python
    pywhatkit.sendwhatmsg_instantly():it is used to type a message to a given phone no 
    '''
    try:
        keyboard=Controller()
        pywhatkit.sendwhatmsg_instantly(phone_no=to,message=message,tab_close=True)  
        time.sleep(5)
        pyautogui.click()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        speak('message sent successfully ')
    except Exception as e:
        speak('unable to send text try again later')  

def google_search(query):
    '''
    searches urls from google
    num:no of urls
    pause: timelapse btw each url search
    '''
    urls=[]
    try:
        for url in search(query=query,tld='co.in',num=1) :
            urls.append(url)
        return urls[0]        
    except Exception as e:
        speak('unable to process your request')

def play_youtube(command):
    '''
    it searches the command on youtube and plays that vedio
    '''
    try:
        videosSearch = VideosSearch(command, limit = 2)
        result=videosSearch.result()
        res=result['result']
        url=res[1]['link']
        webbrowser.open(url)      
    except Exception as e:
        speak('i am unable to find a vedio')
