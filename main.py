# This file contains the code for web automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webdriver_path = "C:/chromedriver-win32 (1)/chromedriver-win32/chromedriver.exe"  

chrome_options = webdriver.ChromeOptions()
chrome_options.executable_path = webdriver_path

browser = webdriver.Chrome(options=chrome_options)

website_url = "your_target_website"  
browser.get(website_url)

username_field = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

password_field = browser.find_element(By.ID, "password")

username = "your_username" 
password = "your_password" 

username_field.send_keys(username)
password_field.send_keys(password)

login_button = browser.find_element(By.ID, "loginbtn")  
login_button.click()

# Replace with the URL you want to visit right after loggin into the website

target_url = "your_target_url_after_login"  
browser.get(target_url)


