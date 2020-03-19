from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
email = 'akshigupta@gmail.com'
password = 'akshi@gupta'
driver.get("http://localhost/Devops/Facebook/")
driver.find_element_by_id("Email_phone").send_keys(email)
driver.find_element_by_id("Password").send_keys(password)
driver.find_element_by_id("LogIn").click()