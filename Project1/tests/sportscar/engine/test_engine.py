from pytest import mark 
import time


@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    my_browser = chrome_browser
    my_browser.get('https://www.google.com')
    time.sleep(5)
    second_browser = chrome_browser
    second_browser.get('https://www.amazon.com')
    chrome_browser.get('https://www.artofmanliness.com/articles/how-a-cars-engine-works/')
    assert True
