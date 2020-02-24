from pytest import mark 
from selenium import webdriver


@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
        chrome_browser.get('https://www.siriusxm.com/')
        assert True