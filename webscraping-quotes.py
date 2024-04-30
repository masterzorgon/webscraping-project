from urllib.request import urlopen, Request
from plotly import offline
from plotly.graph_objects import Bar
from collections import Counter
from bs4 import BeautifulSoup

quotes = []
authors = []
xxx = []

x = 1
while x < 11:
    url = f"https://quotes.toscrape.com/page/{x}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    author_spans = soup.find_all("small", attrs={"class": "author"})
    quote_spans = soup.find_all("span", attrs={"class": "text"})
    quote_divs = soup.find_all('div', {"class": 'quote'})

    for span in quote_spans:
        quotes.append(span.text)

    for span in author_spans:
        authors.append(span.text)

    for div in quote_divs:
        tag_div = div.find('div', {"class": "tags"})
        if tag_div:
            tags = tag_div.find_all('a', {"class": "tag"})
            for tag in tags:
                xxx.append(tag.text)

quote_lengths = [len(quote) for quote in quotes]

max_length = max(quote_lengths)
max_index = quote_lengths.index(max_length)

min_length = min(quote_lengths)
min_index = quote_lengths.index(min_length)

average_length = round((sum(quote_lengths) / len(quote_lengths)) - 2)

print(f"\nAvg. Lenght of Quotes: {average_length} characters")
print(f"Longest Quote: {max_length - 2} characters")
print(f"Shortest Quote: {min_length - 2} characters")

tag_count = Counter(xxx)
most_common_tag, most_common_count = tag_count.most_common()[0]
least_common_tag, least_common_count = tag_count.most_common()[-1]

print(f"\nMost Popular Tag: {most_common_tag} | Used {most_common_count} times")
print(f"Uniqe Tags Across All Quotes: {len(tag_count)}")

author_count = Counter(authors)
author_names = list(author_count.keys())
author_quote_counts = list(author_count.values())

for i in range(len(author_names)):
    print(f"Author: {author_names[i]}, Quote Count: {author_quote_counts[i]}")

most_common_author, most_common_count = author_count.most_common()[0]
least_common_author, least_common_count = author_count.most_common()[-1]

print(f"\nAuthor with Most Quotes: {most_common_author} | {most_common_count} quotes")
print(f"Author with Least Quotes: {least_common_author} | {least_common_count} quotes")

top_author_items = author_count.most_common(10)
top_author_keys, top_author_values = zip(*top_author_items)
top_author_names = list(top_author_keys)
top_author_quote_counts = list(top_author_values)
print(top_author_names)
print(top_author_quote_counts)

top_tag_items = tag_count.most_common(10)
top_tag_keys, top_tag_values = zip(*top_tag_items)
top_tag_names = list(top_tag_keys)
top_tag_counts = list(top_tag_values)
print(top_tag_names)
print(top_tag_counts)

author_visual = [
    {
        "type": "bar",
        "x": top_author_names,
        "y": top_author_quote_counts,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {
                "width": 1.5,
                "color": "rgb(25, 25, 25)",
            },
        },
        "opacity": 0.6
    },
]

author_layout = {
    "title": "Top Ten Authors",
    "xaxis": {
        "title": "Author",
    },
    "yaxis": {
        "title": "Number of Quotes",
    },
}

author_fig = {
    "data": author_visual,
    "layout": author_layout
}

offline.plot(author_fig, filename="python_repos1.html")

tag_visual = [
    {
        "type": "bar",
        "x": top_tag_names,
        "y": top_tag_counts,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {
                "width": 1.5,
                "color": "rgb(25, 25, 25)",
            },
        },
        "opacity": 0.6
    },
]

tag_layout = {
    "title": "Top Ten Tags",
    "xaxis": {
        "title": "Tag",
    },
    "yaxis": {
        "title": "Number of Appearances",
    },
}

tag_fig = {
    "data": tag_visual,
    "layout": tag_layout
}

offline.plot(tag_fig, filename="python_repos2.html")