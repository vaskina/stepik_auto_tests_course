#Задание: ждем нужный текст на странице

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 15 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    
    button = browser.find_element(By.ID, "book")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
      
    def calc(aa):
        return str(math.log(abs(12*math.sin(int(aa)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)
  
    option3 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()