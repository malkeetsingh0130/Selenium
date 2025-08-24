from selenium import webdriver
from selenium.webdriver.common.by import By

d= webdriver.Firefox()

d.get("https://www.saucedemo.com/")
d.maximize_window()

#tag & id

#d.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("abc")

#tag is always optional the below line is same as the above line
d.find_element(By.CSS_SELECTOR,"#user-name").send_keys("abc")

#tag & class
#d.find_element(By.CSS_SELECTOR,"input.input_error form_input").send_keys("abc")

#issue with above line is that input_error form_input is there for 2 elements on the webpage
#to circumvent that i will create a variable and find both the elements and then use 2 element

elements = d.find_elements(By.CSS_SELECTOR,"input.input_error.form_input") # we are using find_elements here
elements[1].send_keys("abc")

#tag and attribute

#d.find_element(By.CSS_SELECTOR,"input[data-test=login-button]").click()

#tag, class and attribute

d.find_element(By.CSS_SELECTOR,"input.input_error.form_input[placeholder=Username]").send_keys("test123")

