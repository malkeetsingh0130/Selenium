from selenium import webdriver
#by is used for locating elements on webpage
from selenium.webdriver.common.by import By
# Specify the path to the Edge WebDriver
driver = webdriver.Edge()

# Open a website
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

#wait
driver.implicitly_wait(5.0)


# Find an element
text_box = driver.find_element(By.NAME, 'my-text')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button')

driver.implicitly_wait(5.0)


# Take action on the element
text_box.send_keys('Selenium')
submit_button.click()
driver.implicitly_wait(5.0)

# Request element information
message = driver.find_element(By.ID, 'message')
print(message.text)
driver.implicitly_wait(5.0)

# End the session
driver.quit()
