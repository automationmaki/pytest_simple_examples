import requests

def test_twitter_is_present():
    resp = requests.get("https://google.com")
    assert "google" in resp.text