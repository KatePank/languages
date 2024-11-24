import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_busket_button(browser):
	browser.get(link)
	browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
