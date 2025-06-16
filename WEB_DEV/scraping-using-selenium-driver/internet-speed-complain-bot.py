import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

UP = 50
DOWN = 50
TWITTER_USERNAME = os.getenv("USERNAME")
TWITTER_PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        time.sleep(2)
        go = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CSS_SELECTOR, '.result-data-large.number.result-data-value.download-speed')
        self.up = self.driver.find_element(By.CSS_SELECTOR, '.result-data-large.number.result-data-value.upload-speed')

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        email.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(2)
        tweet_compose = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up"
                f" when I pay for {DOWN}down/{UP}up?")
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        post = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        post.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot("https://www.speedtest.net/")
bot.get_internet_speed()
bot.tweet_at_provider()
