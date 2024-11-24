import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, etc."
    )
    parser.addoption(
        "--driver",
        action="store",
        default="Firefox",
        help="Browser driver to use for tests"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    driver_name = request.config.getoption("driver")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if driver_name == "Firefox":
        browser = webdriver.Firefox(options=options)
    elif driver_name == "Chrome":
        browser = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {driver_name}")
    yield browser
    browser.quit()

