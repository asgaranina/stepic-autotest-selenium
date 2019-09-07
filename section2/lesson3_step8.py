import os
from selenium import webdriver

browser = webdriver.Chrome()

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

browser.get("http://suninjuly.github.io/file_input.html")

name = browser.find_element_by_name("firstname").send_keys("Имярек")
last_name = browser.find_element_by_name("lastname").send_keys("Фамильевич")
email = browser.find_element_by_name("email").send_keys("email@email.ru")

element = browser.find_element_by_id("file")
element.send_keys(file_path)

submit = browser.find_element_by_class_name("btn-primary")
submit.click()