from selenium import webdriver
from selenium import webdriver


@mark.smoke
@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('https://www.motortrend.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshelf(self):
        assert True