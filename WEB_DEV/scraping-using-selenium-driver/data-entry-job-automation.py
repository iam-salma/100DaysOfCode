import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "html.parser")

address_tags = soup.select("a address")
addresses = [address_tag.getText().strip().replace("|", "") for address_tag in address_tags]
price_tags = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [price_tag.getText()[:6] for price_tag in price_tags]
link_tags = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
links = [link_tag.get("href") for link_tag in link_tags]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/sdUTZTzT5cnUeteFA")
time.sleep(3)

for i in range(len(addresses)):
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(addresses[i])
    price.send_keys(prices[i])
    link.send_keys(links[i])
    submit.click()
    time.sleep(2)
    submit_another_response = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()
    time.sleep(2)
