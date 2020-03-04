from pytest import fixture
import json
from selenium import webdriver


data_path = 'test_data.json'

def load_test_json(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data 


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr 
    drvr.quit()


# @fixture(params=load_test_data(data_path))
# def tv_brand(request):
#     data = request.param
#     return data
