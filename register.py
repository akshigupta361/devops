from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
firstname='Akshi'
surname='Gupta'
email = 'akshigupta@gmail.com'
password = 'akshi@gupta'

driver.get("http://localhost/Devops/Facebook/")
driver.find_element_by_id("firstname").send_keys(firstname)
driver.find_element_by_id("surname").send_keys(surname)
driver.find_element_by_id("emaill").send_keys(email)
driver.find_element_by_id("passw").send_keys(password)
driver.find_element_by_id("submit").click()