from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    n1 = browser.find_element_by_id("num1")
    x = int(n1.text)
    n2 = browser.find_element_by_id("num2")
    y = int(n2.text)

    sum = x + y

  #  list = browser.find_element_by_id("dropdown")
 #   list.click()

    input = str(sum)
    print(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(input)

    submit_button = browser.find_element_by_class_name("btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()