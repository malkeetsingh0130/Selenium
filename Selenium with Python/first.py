from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

driver.find_element(By.NAME,"username").send_keys("Admin")

driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

actual_title=driver.title
expected_title="OrangeHRM"

if actual_title == expected_title:
    print("Title matches")
else:
    print(f"Actual title is {actual_title}")

driver.close()