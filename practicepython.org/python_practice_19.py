## July 23nd 2023
## https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

## get article text

from bs4 import BeautifulSoup
import requests

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r.html = r.text

soup = BeautifulSoup(r.html, "html.parser")

# Use the select() method to find all div elements with the specified class

content_divs = soup.select('div.ArticlePageChunksContent-etcMtP.bwyLBj')

# Check if any div elements are found before getting the text
if content_divs:
    for div in content_divs:
        content_text = div.text
        print(content_text)
else:
    print("Div elements not found.")