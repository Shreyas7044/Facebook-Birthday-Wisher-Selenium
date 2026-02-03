# Automating Happy Birthday posts on Facebook using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize Chrome WebDriver
browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)

# Open Facebook
browser.get("https://www.facebook.com/")
time.sleep(3)

# Facebook username
username = "your_email_here@gmail.com"

# Read password from text file
with open("test.txt", "r") as file:
    password = file.read().strip()

print("Starting Facebook Login...")

# Enter username
browser.find_element(By.ID, "email").send_keys(username)

# Enter password
browser.find_element(By.ID, "pass").send_keys(password)

# Click login
browser.find_element(By.NAME, "login").click()
time.sleep(5)

print("Login successful")

# Navigate to birthdays page
browser.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)

feed = "Happy Birthday! 🎉🎂"

# Locate birthday text boxes
elements = browser.find_elements(
    By.XPATH,
    "//textarea[contains(@aria-label,'Write on')]"
)

count = 0
for el in elements:
    el.send_keys(feed)
    el.send_keys(Keys.RETURN)
    count += 1
    print(f"Birthday wish posted for friend {count}")
    time.sleep(2)

# Close browser
browser.quit()
