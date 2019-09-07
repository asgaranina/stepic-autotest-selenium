from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    tres = browser.find_element_by_id("treasure")
    x = tres.get_attribute("valuex")
    y = calc(x)
    print(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    sub = browser.find_element_by_class_name("btn")
    sub.click()

finally:
    browser.quit()