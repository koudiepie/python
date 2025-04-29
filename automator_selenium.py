from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

USERNAME = '學號沒差'
PASSWORD = '*************'
LOGIN_URL = 'https://moodle.mcu.edu.tw/'
COURSE_NAME = '11302-75552網路程式開發'

chrome_path = r'C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(executable_path=chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(LOGIN_URL)
time.sleep(2)

driver.find_element(By.ID, 'login_username').send_keys(USERNAME)
driver.find_element(By.ID, 'login_password').send_keys(PASSWORD)

driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary.btn-block').click()
time.sleep(3)

try:
    course_link = driver.find_element(By.LINK_TEXT, COURSE_NAME)
    course_link.click()
    print(f"已點擊進入課程：{COURSE_NAME}")
except:
    print(f"無法找到課程：{COURSE_NAME}")

time.sleep(60)