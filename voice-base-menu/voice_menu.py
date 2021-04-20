import speech_recognition as sr
from pyttsx3 import speak
from os import system
from subprocess import getoutput 

# You may get error if you use pyttsx3 for first use this link and download rpm file and choose (CentOs) url is : https://rpmfind.net/linux/rpm2html/search.php?query=libespeak.so.1()(64bit) 
# Then install yum install file_name(which you just downloaded using above url)
# Now install pyttsx3 : (pip3 install pyttsx3) 

speak("Hello Ankit i am your Personal Assistant")
speak("Tell me what can i do for you")

reco = sr.Recognizer()
global data
def myvoice():
    with sr.Microphone() as source:
        print("start")
        audio = reco.listen(source)
        print("stop")
        data = reco.recognize_google(audio)
        data = data.lower()

myvoice()
print(myvoice.data)



    # LOCAL webserver

def webserver():
            system("clear")
            system('tput setaf 9')
            print('Yum Must Be Configured Before Working on Webserver')
            system('tput setaf 9')
            getoutput('yum install httpd -y')
            page = input('Do you have your web page(y/n): ')
            if page == 'y':
                path = input('Enter path followed by file name: ')
                system(f'cp {path} /var/www/html')
                system('systemctl start httpd')
                exit()
            elif page == 'n':
                system('tput setaf 74')
                print('Create your Web Page')
                system('tput setaf 7')
                fname = input('Enter File name: ')
                print('Enter Data inside your web page')
                data = input()
                system(f"echo \'{data}\' > /var/www/html/{fname}.html")
                system('systemctl start httpd;clear;tput setaf 10')
                print('''
\t\t-------------------------------------------------------------------------------------
\t\t\t\t  Congratulations!!! Your webpage is Ready To Use
\t\t-------------------------------------------------------------------------------------
''')
                print('\nSearch on any web browser with your')
                print(f'system IP/{fname}.html')
                system('tput setaf 7')
                input('Press Enter To continue')
                exit()


            # Main Code

if ('webserver' in data) or ('web server' in data):
    webserver()


