from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://automationexercise.com/signup")
driver.maximize_window()

wait=WebDriverWait(driver,15)

# home=wait.until(EC.visibility_of_element_located((By.XPATH,'//ul[@class="nav navbar-nav"]/descendant::i[@class="fa fa-home"]')))
# home.click()
# signup=wait.until(EC.visibility_of_element_located((By.XPATH, '//li/descendant::i[@class="fa fa-home"]')))
# signup.click()

name=wait.until(EC.visibility_of_element_located((By.XPATH,'//form[@action="/signup"]/child::input[@name="name"]')))
name.send_keys("Jane")

email=wait.until(EC.visibility_of_element_located((By.XPATH,'//form[@action="/signup"]/child::input[@name="email"]')))
email.send_keys("Jane@yahoo.com")

button=wait.until(EC.element_to_be_clickable((By.XPATH,'//form[@action="/signup"]/child::button[@type="submit"]')))
button.click()
button.click()

ms=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="id_gender2"]')))
ms.click()

newsletter = driver.find_element(By.NAME, "newsletter")
offers = driver.find_element(By.NAME, "optin")
newsletter.click()
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Offers selected:", offers.get_attribute("checked"))

driver.quit()
