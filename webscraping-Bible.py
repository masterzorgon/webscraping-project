import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

# must have leading 0 for single-digit numbers
# 21 chapters in john

def calc_rand_chapter():
    rand_num = random.randint(1, 21)
    return f"{rand_num:02}" 

webpage = f"https://ebible.org/asv/JHN{calc_rand_chapter()}.htm"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
website_request = requests.get(webpage, headers=headers)
website_content = website_request.content

soup_obj = BeautifulSoup(website_content, 'html.parser')

page_verses = soup_obj.findAll("div", class_="p")

my_verses = []
for section_verses in page_verses:
    verse_list = section_verses.text.split(".")

    for v in verse_list:
        my_verses.append(v)

my_verses = [i for i in my_verses if i != " "]

print(my_verses)

my_choice = random.choice(my_verses)
print(my_choice)