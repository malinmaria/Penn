import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def setup(request):
    options = Options()
    options.headless = True
    print("initiating chrome driver")
    # driver = webdriver.Chrome(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\PennPRNews\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\PennPRNews\\drivers\\chromedriver.exe", chrome_options=options)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("https://pennmedicine.org/news")
    driver.maximize_window()

    yield driver
    driver.close()
