from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://mannco.store/item/440-mann-co-supply-crate-key"

driver = webdriver.Chrome()
driver.get(url)
print(driver.find_element(By.XPATH, value='//*[@id="transacContent"]/tr[1]/td[3]').text)

sleep(3600)