from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR, '#articlecount li:nth-child(1) a')
print(articles.text)

driver.get("https://www.python.org/")

date = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last time')
events = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last ul a')

events_dict = {}
for i in range(len(events)):
    events_dict[i] = {"time": '2025-'+date[i].text, "name": events[i].text}
pprint(events_dict)

driver.quit()
