from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class Test404Page():

    def test_404page(self):
        self.driver.get("https://www.pennmedicine.org/news/404")
        assert self.driver.title == "Page Not Found - Penn Medicine"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1-main__title").text == "Page Not Found"
        self.driver.find_element(By.LINK_TEXT, "Penn Medicine News home page.").click()
        assert self.driver.title == "Penn Medicine News & Publications | University of Pennsylvania Health System"
        # self.driver.close()