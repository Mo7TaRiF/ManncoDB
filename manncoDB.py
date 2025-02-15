from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(options=chrome_options)

url = "https://mannco.store/item/440-mann-co-supply-crate-key"

driver.get(url)
print(driver.find_element(By.XPATH, value='//*[@id="transacContent"]/tr[1]/td[3]').text)

sleep(3600)