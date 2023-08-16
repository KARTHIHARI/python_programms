from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
import pytesseract

# Setting up the Chrome driver
driver = webdriver.Chrome()

# Maximizing the browser window
driver.maximize_window()

# Navigate to the website
driver.get("https://www.irctc.co.in/nget/train-search")

# Click on OK button and then on LOGIN
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='LOGIN']"))).click()

# Capture the captcha image
image_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[@id='nImgContainer']//following::img)[2]")))
path = "captcha.png"
image_element.screenshot(path)

# Use pytesseract to extract text from the image
image = Image.open(path)
captcha_text = pytesseract.image_to_string(image)

print(captcha_text)

# Cleanup (optional)
driver.quit()
