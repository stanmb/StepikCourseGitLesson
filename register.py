from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_register():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first").send_keys("123")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second").send_keys("123")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third").send_keys("123")

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()