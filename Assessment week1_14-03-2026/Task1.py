from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/login')
username=driver.find_element(By.CSS_SELECTOR,'input[name="username"]')
password=driver.find_element(By.CSS_SELECTOR,'input[id="password"]')
login=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
link=driver.find_elements(By.CSS_SELECTOR,'div[style="text-align: center;"] a')
print("Script ran successfully")
driver.quit()
