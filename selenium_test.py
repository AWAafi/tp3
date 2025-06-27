from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Chemin local vers ton index.html
file_path = r"C:\Users\yombe\Downloads\tp3_use_case\index.html"
file_url = 'file:///' + file_path.replace('\\', '/')

driver = webdriver.Firefox()

driver.get(file_url)

number_input = driver.find_element(By.ID, "number")
number_input.send_keys("5")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

# Attente explicite que le résultat apparaisse
wait = WebDriverWait(driver, 10)
result_element = wait.until(EC.text_to_be_present_in_element((By.ID, "result"), "Résultat : 25"))

result_text = driver.find_element(By.ID, "result").text
print("Résultat affiché :", result_text)

assert "25" in result_text

driver.quit()
