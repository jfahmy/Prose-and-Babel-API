import requests
from bs4 import BeautifulSoup


def full_text(url):
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    full_text = ""
    for paragraph in soup.find_all('p'):
        # text_archive.write(paragraph.get_text())
        full_text += paragraph.get_text()

    return full_text
