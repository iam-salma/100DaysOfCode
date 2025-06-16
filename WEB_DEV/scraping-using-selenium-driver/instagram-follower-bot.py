import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "one_message_foundation_"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.USERNAME = "curioussoul1360"
        self.PASSWORD = "Syedali2000!"
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        username.send_keys(self.USERNAME)
        password.send_keys(self.PASSWORD, Keys.ENTER)

        time.sleep(5)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        # time.sleep(3.7)
        # # Click "not now" on notifications prompt
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(4)
        followers = self.driver.find_element(by=By.CSS_SELECTOR, value='ul li:nth-child(2) div a')
        followers.click()
        time.sleep(3)

        modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        follow_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='div.x1dm5mii > div > div > div > div > div > button')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
