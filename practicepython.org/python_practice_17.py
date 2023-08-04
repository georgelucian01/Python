## July 23nd 2023
## https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

## Decode a web page
## Use the BeautifulSoup and requests Python packages
## To print out a list of all the article titles on the New York Times homepage

from bs4 import BeautifulSoup
import requests


url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

# Use CSS selector to find div elements with class containing "e1ppw5w20" and select the h3 elements within them
titles = soup.select("div[class*=e1ppw5w20] h3")

for title_element in titles:
    title = title_element.text.strip()
    print(title)

