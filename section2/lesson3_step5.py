from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

tres = browser.find_element_by_id("input_value")
x = tres.text
y = calc(x)

input_y = browser.find_element_by_id("answer")
input_y.send_keys(y)

robot_check = browser.find_element_by_id("robotCheckbox")
robot_check.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

radio = browser.find_element_by_id("robotsRule")
radio.click()

button.click()
assert True
browser.quit()