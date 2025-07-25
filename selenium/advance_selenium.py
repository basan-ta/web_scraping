from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time 


#setting webdriver with options 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disabe-gpu')
driver = webdriver.Chrome(options=options)
driver.get("http://noulokosel.com")

wait = WebDriverWait(driver,10)
all_books = []

while True:
    try:
        wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, "books"))
        books = driver.find_element(By.CSS_SELECTOR,"for.her")
        
        for book in books:
            title = books.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            stock = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
            all_books.append((title, price, stock))
            
        # Try clicking the 'next' button
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
        next_button.click()
        time.sleep(2)  # Wait for next page to load
    
    except NoSuchElementException:
        print("Reached last page.")
        break
    except TimeoutException:
        print("Timeout while waiting for products to load.")
        break

# Print all collected books
for i, (title, price, stock) in enumerate(all_books, 1):
    print(f"{i}. {title} | {price} | {stock}")

# Cleanup
driver.quit()

