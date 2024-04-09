from bs4 import BeautifulSoup
import requests
from core.config import URL, DOMEN, HEADERS

response = requests.get(URL, headers=HEADERS)
if response.status_code == 200:
    src = response.text
    soup = BeautifulSoup(src, "html.parser")

    base_url = DOMEN.rstrip('/')

    def update_url(attribute, tags, attribute_name='src'):
        for tag in soup.find_all(tags, **{attribute: True}):
            url = tag[attribute]
            if not url.startswith(('http://', 'https://', '#', 'mailto:', 'tel:', 'data:')):
                tag[attribute] = f"{base_url}/{url.lstrip('/')}"

    update_url('src', 'img')

    update_url('srcset', 'source')

    update_url('href', 'a')

    update_url('href', 'link')

    updated_html_code = soup.prettify()


    # file_path = "../../index.html" 
    file_path = "modified.html"

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_html_code)
        print(f"Successfully wrote updated HTML to {file_path}")
    except Exception as e:
        print(f"Error writing the file: {e}")
else:
    print(f"Failed to fetch the webpage, status code: {response.status_code}")
