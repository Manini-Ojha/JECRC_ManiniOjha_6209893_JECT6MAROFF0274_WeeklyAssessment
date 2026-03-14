from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.wikipedia.org/")
search=driver.find_elements(By.XPATH,'//input[@id="searchInput"]')
lang=driver.find_elements(By.XPATH,'//a[text()="English"]')
logo=driver.find_elements(By.XPATH,'//span[text="Wikipedia"]')
list_of_langs=driver.find_elements(By.CSS_SELECTOR,'nav[class="central-featured"] a')
print(len(list_of_langs))
driver.back()
driver.forward()
driver.refresh()
print(f'The title of the page is {driver.title}')
driver.quit()

