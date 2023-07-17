from coco import great,takeRequest,speak,tellTime,tellDate,play_movie,play_music,play_youtube,search_from_wikipedia,search_news,send_mail,send_whatsapp_message,google_search
from coco import gmail_ids,contacts
import webbrowser,os
def assistant(): 
    great()
    while True :
        command=takeRequest().lower()
        '''the functions to be performent with respect to command given ----->'''
        if  'quit' in command:
            command = ''
            speak('ok sir','let me know if something comes up')
            break
        elif 'hello' == command:
            command=''
            speak('hello sir')
        elif (('time' in command)):
            command=''
            tellTime()
            speak('can i do anything else for you')
        elif (('date' in command)):
            command=''
            tellDate()
            speak('can i do anything else for you')
        elif 'open google' in command:
            webbrowser.open('google.com') 
            speak('can i do anything else for you')  
            command='' 
        elif 'open youtube' in command:
            webbrowser.open('youtube.com')
            speak('can i do anything else for you ')
            command=''
        elif ('open geeks for geeks' in command) or ('open gfg' in command):
            webbrowser.open('https://www.geeksforgeeks.org/')
            speak('can i do anything else for you') 
            command=''  
        elif 'open stack overflow' in command:
            webbrowser.open('stackoverflow.com')
            speak('can i do anything else for you')
            command=''
        elif 'open whatsapp' in command:
            webbrowser.open(url="https://web.whatsapp.com/")
            command=''
            speak('can i do anything else for you')
        elif 'open instagram' in command:
            webbrowser.open('instagram.com')
            speak('can i do anything else for you')
            command=''  
        elif 'open' in command:
            url=google_search(command)
            webbrowser.open(url=url)
            speak('can i do anything else for you')
            command=''
        elif 'music' in command:
            play_music()
            speak('can i do anything else for you')
            command=''
        elif 'movie' in command:
            play_movie()
            speak('can i do anything else for you')
            command=''    
        elif 'play' in command :
            command.replace('play','')
            play_youtube(command)
            speak('can i do anything else for you')
            command=''
        elif 'play video' in command:
            speak('what do you want to play')
            query=takeRequest().lower()   
            play_youtube(query)
            speak('can i do anything else for you')
            command=''
        elif 'wikipedia' in command:
            command.replace('wikipedia','')
            search_from_wikipedia(command)
            speak('can i do anything else for you')
            command=''  
        elif 'search' in command:
            command.replace('search','')
            search_from_wikipedia(command)
            speak('can i do anything else for you')
            command=''   
        elif 'news' in command:
            search_news()
            speak('can i do anything else for you')
            command=''
        elif 'mail' in command:
            speak('to whom should i send it ')
            name=takeRequest().lower()
            if name in gmail_ids.keys():
                to=gmail_ids[name]
            else:
                speak('i am unable to find a person with name '+str(name)+' was found ',' can you please type his/her email for future reference ')
                to=input('enter email :')
                gmail_ids.update({name : to})
            speak('what should i say...')
            content=takeRequest().lower()
            send_mail(to,content) 
            command=''   
        elif 'message' in command:
            speak('to whom i should message')
            name=takeRequest().lower()
            if name in contacts.keys():
                to=contacts[name]
            else:
                speak('i am unable to find person ith name '+str(name)+'please tell the phone no for fuure reference')
                to=input('enter the no :')
                contacts.update({name:to})
            speak('what should i say')
            message=takeRequest().lower()
            send_whatsapp_message(to,message)
            command=''
        else:
            search_from_wikipedia(command)
            speak('can i do anything else for you')
            command=''

# if __name__ == '__main__':
#     main()

