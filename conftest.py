import pytest
from selene import browser


@pytest.fixture()
def setting_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720




@pytest.fixture()
def browser_open_google():
    browser.open('https://google.com')


