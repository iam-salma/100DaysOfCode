import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.pythonanywhere.com/")

log_in = driver.find_element(By.CLASS_NAME, 'login_link')
log_in.click()

username = driver.find_element(By.NAME, 'auth-username')
username.send_keys("salmasyed1360@gmail.com")
password = driver.find_element(By.NAME, 'auth-password')
password.send_keys("Syedali2000!")

button = driver.find_element(By.ID, 'id_next')
button.click()

tasks = driver.find_element(By.ID, 'id_tasks_link')
tasks.click()

time.sleep(5)
extend_expiry = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.extend_scheduled_task.task_action")
extend_expiry.click()

log_out = driver.find_element(By.CSS_SELECTOR, '.btn-link.logout_link')
log_out.click()
