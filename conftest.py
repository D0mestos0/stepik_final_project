import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Please choose language",
        )

@pytest.fixture
def browser(request):
    name_language = request.config.getoption("language")
    opts = ChromeOptions()  
    opts.add_experimental_option("prefs", {"intl.accept_languages": name_language}) 
    browser = webdriver.Chrome(options=opts)     
    browser.maximize_window()
    yield browser
    print("Close browser")
    browser.quit()




