from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answ = browser.find_element_by_id("answer")
answ.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

sub = browser.find_element_by_class_name("btn")
sub.click()