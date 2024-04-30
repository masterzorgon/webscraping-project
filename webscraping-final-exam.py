import csv
import requests
from bs4 import BeautifulSoup

webpage_url = "https://registrar.web.baylor.edu/exams-grading/spring-2024-final-exam-schedule"
browser_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
website_request = requests.get(webpage_url, headers=browser_agent)
website_content = website_request.content

soup_obj = BeautifulSoup(website_content, 'html.parser')
print(soup_obj.title.text)

html_tables = soup_obj.findAll("table")
finals_table_obj = html_tables[1]
table_rows = finals_table_obj.findAll("tr")

class_schedule_file = open("class_schedule.csv", "r")
class_records = csv.reader(class_schedule_file)

for record in class_records:
    my_class = record[0]
    my_time = record[1]
    for row in table_rows[1:]:
        table_cells = row.findAll("td")
        schedule_class = table_cells[0].text.strip("\n")
        schedule_time = table_cells[1].text.strip("\n")
        exam_day = table_cells[2].text.strip("\n")
        exam_time = table_cells[3].text.strip("\n")
        if schedule_class == my_class and schedule_time == my_time:
            print(my_class, my_time, exam_day, exam_time)