from datetime import datetime as dt
import os
import glob
import random
import urllib.request as url
import bs4
import json

chat=True

greetIntent=['hi','hello','hey','good morning','hey there']
dateIntent=['date','tell me date','please tell me date']
timeIntent=['time','tell me time','please tell me time']
musicIntent=['play music','play song','music','song','please play a song','please play music']
newsIntent=['news','today news','indian news',]
productIntent=['shopping','online shopping','flipkart']
while chat:
    msg=input("Enter your message:").lower()
    
    if msg in greetIntent:
        print("Hello User")
    
    elif msg in dateIntent:
        date=dt.now().date()
        print("Date is ;", date.strftime("%d %B, %Y, %a"))
    
    elif msg in timeIntent:
        time=dt.now().time()
        print("Time is ;",time.strftime("%H:%M:%S %p"))

    elif msg in musicIntent:
        os.chdir(path=r"C:\Users\Chetanya Chauhan\Downloads\Music")
        os.getcwd()
        songs=glob.glob('*mp3')
        random_song = random.choice(songs)
        os.startfile(random_song)
        print("Playing: "+ random_song)
        
    elif msg in newsIntent:
        path = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f9f7ff5f4d54497da1a11029268c25f3"
        response = url.urlopen(path)
        data = json.load(response)
        articles = data['articles']
        for i in range(len(articles)):
            print(articles[i]['title'])
            print("*" * 40)
            
    elif msg in productIntent:
        product = input("Enter Product Name:")
        product = product.replace(" ","+").lower()
        for k in range(1,6):
            path = f"https://www.flipkart.com/search?q={product}&page={k}"
            response =url.urlopen(path)
            page =bs4.BeautifulSoup(response,"html.parser")
            titlelist = page.find_all('div', {'class' : '_4rR01T'})
            pricelist=page.find_all('div',{'class' : '_30jeq3 _1_WHN1'})
            for i in range(len(titlelist)):   
                print(titlelist[i].text)
                print(pricelist[i].text)
                print("*"*30)


    elif msg=="bye":
        print("Bye User")
        chat=False
    
    else:
        print("I didn't understand your message.")
