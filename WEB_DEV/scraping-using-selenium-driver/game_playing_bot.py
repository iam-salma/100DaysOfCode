import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in items]
prices = driver.find_elements(By.CSS_SELECTOR, '#store b')

item_prices = []
for price in prices:
    if price.text != "":
        item_prices.append(int(price.text.split("-")[1].strip().replace(",", "")))

cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

timeout = time.time() + 5
five_min = time.time() + 60*5

is_on = True
while is_on:
    cookie.click()

    if time.time() >= timeout:
        money = driver.find_element(By.ID, 'money').text
        if "," in money:
            money = money.replace(",", "")
        cookies = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookies > cost:
                affordable_upgrades[cost] = id

        driver.find_element(By.ID, affordable_upgrades[max(affordable_upgrades)]).click()
        timeout = time.time() + 5

    if time.time() >= five_min:
        print(driver.find_element(By.ID, 'cps').text)
        is_on = False
