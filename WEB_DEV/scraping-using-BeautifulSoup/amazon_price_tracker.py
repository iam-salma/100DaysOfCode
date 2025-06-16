import requests
import smtplib
from bs4 import BeautifulSoup

email = "salmasyed1360@gmail.com"
password = "aogwjrpypuekxykk"

product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# https://httpbin.org/headers for headers
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(product_url, headers=header)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())

# price = soup.find(class_="a-offscreen").get_text()
# price_without_currency = price.split("$")[1]
dollars = soup.find(name="span", class_="a-price-whole").getText()
cents = soup.find(name="span", class_="a-price-fraction").getText()
price = float(dollars + cents)

title = soup.find(id="productTitle").get_text().strip()

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{title} is on sale for {price}!\n{product_url}".encode("utf-8")
        )