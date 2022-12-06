from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

EMAIL = "" #your fb email
PASS = "" #your fb pass


chrome_driver_path = "/Applications/Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://tinder.com/")

time.sleep(5)
login = driver.find_element(By.XPATH, "//*[text()='Log in']")
login.click()


time.sleep(5)

fb_account_login = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_account_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

time.sleep(5)

email_field = driver.find_element(By.ID, "email")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(PASS)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

location_allow = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[1]')
location_allow.click()

time.sleep(5)

notification = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(5)

cookie = driver.find_element(By.XPATH, '//*[@id="q-401777178"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie.click()

time.sleep(5)

dark_mode = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div[2]/button')
dark_mode.click()

time.sleep(5)


while True:
    while True:
        try:
            button_like = driver.find_element(By.XPATH, '/html/body')
        except NoSuchElementException:
            time.sleep(.5)
            print('error')
        else:
            for like in range(100):
                button_like.send_keys(Keys.ARROW_RIGHT)
                time.sleep(2)
            break

