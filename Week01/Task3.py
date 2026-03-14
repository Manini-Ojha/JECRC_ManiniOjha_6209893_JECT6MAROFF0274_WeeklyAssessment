from selenium import webdriver
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.hindustantimes.com/")
sleep(3)
print(f'the title of this website is {driver.title}')
driver.get("https://www.myntra.com/")
sleep(3)
print(f'the title of this website is {driver.title}')
driver.get("https://www.flipkart.in/")
sleep(3)
print(f'the title of this website is {driver.title}')

driver.get("https://www.python.org/")
sleep(3)
print(f'the title of this website is {driver.title}')