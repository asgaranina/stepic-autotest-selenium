from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

submit = browser.find_element_by_class_name("btn-primary").click()
alert = browser.switch_to.alert
alert.accept()

magic = browser.find_element_by_id("input_value")
x = magic.text
y = calc(x)

answer = browser.find_element_by_id("answer").send_keys(y)
submit = browser.find_element_by_class_name("btn-primary").click()
