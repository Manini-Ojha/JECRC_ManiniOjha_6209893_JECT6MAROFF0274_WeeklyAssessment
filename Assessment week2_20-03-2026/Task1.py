from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

print(driver.title)
# assert "Amazon" in driver.title,"title not found"
assert "amazon.in" in driver.current_url, "url not found"
wait=WebDriverWait(driver,10)
cat=wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="searchDropdownBox"]')))
select=Select(cat)
select.select_by_visible_text("Books")
search=wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="twotabsearchtextbox"]')))
search.send_keys("Harry Potter",Keys.ENTER)

titles=driver.find_elements(By.XPATH,'//div[@data-cy="title-recipe"]/descendant::h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/child::span')

count=0
for i in titles:
    if(count<5):
        print(i.text)
        count+=1

first_ele=wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@data-cy="title-recipe"]/descendant::h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/child::span)[1]')))
first_ele.click()