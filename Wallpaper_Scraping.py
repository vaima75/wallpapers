'''
@uther : VIPER
Web Scrapping for www.8muses.com. Extract the desired comic book images
Instructions:
1. Copy and paste the url of desired wallpaper web page.
    Remember, the wallpaper web page must contains thumbnails
    For Ex:
    https://wallpaperscraft.com/catalog/<any category>/1366x768
2. Run the file.
3. Wait for while for 'Onging File Operations' to end
4  After  'All done' message go to folder comics.
    All images of the comic have been extracted.
'''
import requests # install Before use
from bs4 import BeautifulSoup # install Before use
import os

#### Function Declaration ###################

'''
def wall_paper_Images_extraction(url_img, filename):
    # make a directory
    os.makedirs (filename, exist_ok=True)
    res = requests.get (url_img)
    res.raise_for_status ()
    soup = BeautifulSoup (res.text, "html.parser")
    WPElem = soup.select ('.wallpapers__list .wallpapers__item .wallpapers__link .wallpapers__canvas img')
    # print(type(WPElem))
    # print(WPElem)
    print ('Wallpaper Category : ', filename)
    print ('Wallpaper Images:', len (WPElem))
    print ("Downloading Wallpapers....")
    for i in range (len (WPElem)):
        WPUrl = WPElem[i].get ('src')
        pic_url = WPUrl.replace ('300x168', '1366x768', 1)
        
        # pic_name = os.path.basename (pic_url)
        # new_pic_name = pic_name.replace (pic_name, str (i) + '.jpg')

        res_url = requests.get (pic_url)
        res_url.raise_for_status ()

        imageFile = open (os.path.join (filename, os.path.basename (pic_url)), 'wb')
        for chunk in res_url.iter_content (100000):
            imageFile.write (chunk)
        imageFile.close ()

    print ('Download Complete !')
'''





def wall_paper_Images_link(url_img, filename):
    # make a directory
    os.makedirs (filename, exist_ok=True)
    print('Input URL: ',url_img)
    res = requests.get (url_img)
    res.raise_for_status ()
    soup = BeautifulSoup (res.text, "html.parser")
    WPElem = soup.select ('.wallpapers__list .wallpapers__item .wallpapers__link .wallpapers__canvas img')
    # print(type(WPElem))
    # print(WPElem)
    print ('Wallpaper Category : ', filename)
    #print ('Wallpaper Images:', len (WPElem))
    WPNxtPage = soup.select ('.pager .pager__list .pager__item a')
    WPLastURL = WPNxtPage[2].get ('href')
    last_url = 'https://wallpaperscraft.com'+WPLastURL
    j = 1
    #print ("Last URL: ", last_url)
    while j >= 1:
        if url_img == last_url:
            print ('Wallpaper Images:', len (WPElem))
            print ("Dowloading Wallpapers.......")

            for i in range (len (WPElem)):
                WPUrl = WPElem[i].get ('src')
                pic_url = WPUrl.replace ('300x168', '1366x768', 1)

                res_url = requests.get (pic_url)
                res_url.raise_for_status ()

                imageFile = open (os.path.join (filename, os.path.basename (pic_url)), 'wb')
                for chunk in res_url.iter_content (100000):
                    imageFile.write (chunk)
                imageFile.close ()

            print ('Extraction Done !!!')
            break
        else:
            print ('Wallpaper Images:', len (WPElem))
            print ("Dowloading Wallpapers.......")

            for i in range (len (WPElem)):
                WPUrl = WPElem[i].get ('src')
                pic_url = WPUrl.replace ('300x168', '1366x768', 1)

                res_url = requests.get (pic_url)
                res_url.raise_for_status ()

                imageFile = open (os.path.join (filename, os.path.basename (pic_url)), 'wb')
                for chunk in res_url.iter_content (100000):
                    imageFile.write (chunk)
                imageFile.close ()

            # Extracting next url
            print ("Extraction End!!")
            #print ("Previous URL: ", url_img)
            print ('Jump to Next URL...')
            j += 1
            url_img = 'https://wallpaperscraft.com/catalog/tv-series/1366x768/page' + str (j)
            print ('Next URL: ', url_img)

            res_nxt = requests.get (url_img)
            res_nxt.raise_for_status ()
            soup_nxt = BeautifulSoup (res_nxt.text, "html.parser")
            WPElem = soup_nxt.select ('.wallpapers__list .wallpapers__item .wallpapers__link .wallpapers__canvas img')

    print ('Wallpapers Extracted !')

#########################################################

filename = 'tv-series'
#copy paste the URL
url_img = 'https://wallpaperscraft.com/catalog/tv-series/1366x768/page1'
wall_paper_Images_link(url_img, filename)



'''
filename = 'tv-series'
url_img = 'https://wallpaperscraft.com/catalog/tv-series/1366x768'
os.makedirs (filename, exist_ok=True)
res = requests.get (url_img)
res.raise_for_status ()
soup = BeautifulSoup (res.text, "html.parser")
WPNxtPage = soup.select('.pager .pager__list .pager__item a')
print(type(WPNxtPage))
print(len(WPNxtPage))
print(WPNxtPage[2])
#print(WPNxtPage[1].get('src'))
WPNxtUrl = WPNxtPage[1].get ('href')
print('https://wallpaperscraft.com'+WPNxtUrl)
'''
