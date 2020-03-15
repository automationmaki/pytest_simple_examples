import requests

def test_get_succesful_response():
    resp = requests.get("https://google.com")
    assert resp.status_code == 200