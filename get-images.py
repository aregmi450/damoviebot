#model scrapping for moviebot
import requests
from bs4 import BeautifulSoup as bs
import os
# website with movie images
url = Paste your URL Link here from which you are going to scrape the picture

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# locate all elements with image tag
image_tags = soup.findAll("img")

#create directory for images
##    os.makedirs('movies')
# move to new directory
#os.chdir('movies')

# image file name variable
x = 296
#writing image
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('movie-' + str(x) + '.jpg', 'wb') as f:
                f.write(source.content)
                f.close()
                x += 1
    except:
        pass
