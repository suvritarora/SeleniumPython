import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")
# time.sleep(2)
# googleSearchBox = driver.find_element(By.ID,"APjFqb")
# googleSearchBox.send_keys("Selenium")
# googleSearchBox.send_keys(Keys.ENTER)

# googleSearchButton = driver.find_element(By.NAME, "btnK")
# googleSearchButton.click()

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID, "fname").send_keys("Suvrit")
driver.find_element(By.ID, "lname").send_keys("Arora")
driver.find_element(By.XPATH, "//button[text()=' Submit']").click()
driver.quit()
print("Done")
print("test case passed")