import requests
from bs4 import BeautifulSoup

webpage_url = 'https://www.worldometers.info/coronavirus/country/us'
browser_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
website_request = requests.get(webpage_url, headers=browser_agent)
website_content = website_request.content

soup_obj = BeautifulSoup(website_content, 'html.parser')
print(soup_obj.title.text)

table_data = soup_obj.findAll("tr")
print(table_data[:2])

state_with_max_mortality = ""
state_with_max_testing = ""
state_with_min_testing = ""
max_mortality_rate = 0.0
max_testing_rate = 0.0
min_testing_rate = float('inf')

for row in table_data[2:53]:
    columns = row.findAll("td")
    state_name = columns[1].text.strip('\n')
    total_cases = float(columns[2].text.replace(",", ""))
    total_deaths = float(columns[4].text.replace(",", ""))
    total_tests = float(columns[10].text.replace(",", ""))
    population_count = float(columns[12].text.replace(",", ""))
    mortality_rate = total_deaths / total_cases
    testing_rate = total_tests / population_count

    if mortality_rate > max_mortality_rate:
        max_mortality_rate = mortality_rate
        state_with_max_mortality = state_name

    if testing_rate > max_testing_rate:
        max_testing_rate = testing_rate
        state_with_max_testing = state_name

    if testing_rate < min_testing_rate:
        min_testing_rate = testing_rate
        state_with_min_testing = state_name

print("\nState with highest mortality rate: ", state_with_max_mortality)
print(f"Mortality Rate: {max_mortality_rate:.2%}")
print("\nState with the highest testing rate:", state_with_max_testing)
print(f"Testing Rate: {max_testing_rate:.2%}")
print("\nState with the lowest testing rate:", state_with_min_testing)
print(f"Testing Rate: {min_testing_rate:.2%}")