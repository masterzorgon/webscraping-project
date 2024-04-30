import requests
from bs4 import BeautifulSoup

webpage_url = "https://www.webull.com/quote/us/gainers"
browser_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
website_request = requests.get(webpage_url, headers=browser_agent)
website_content = website_request.content

soup_obj = BeautifulSoup(website_content, 'html.parser')
print(soup_obj.title.text)

stock_table_cells = soup_obj.findAll("div", attrs={"class": "table-cell"})
print(stock_table_cells[0])
print()
print(stock_table_cells[1].text)

counter = 1
for _ in range(5):
    company_name = stock_table_cells[counter].text
    price_change = float(stock_table_cells[counter + 2].text.strip("+").strip("%"))
    current_price = float(stock_table_cells[counter + 3].text)
    previous_price = round(current_price / (1 + (price_change / 100)), 2)
    print(f"Company Name: {company_name}")
    print(f"Change: {price_change}%")
    print(f"Price: {current_price}")
    print(f"Previous price: {previous_price}")
    print()
    counter += 11