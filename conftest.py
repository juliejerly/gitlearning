import json

import pytest
from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@fixture
def get_test_data():
    with open("C:/Users/julie.g.DC/PycharmProjects/learnplaywright/data/test_data.json") as f:
        return json.load(f)