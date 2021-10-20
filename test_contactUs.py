from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestContactUs():

    def test_contactUs(self):
        self.driver.get("https://www.pennmedicine.org/news/contact-us")
        # self.driver.set_window_size(1342, 728)
        assert self.driver.title == "Contact Us - Penn Medicine"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1").text == "Contact Us"
        assert self.driver.find_element(By.CSS_SELECTOR, ".rtf > h3").text == "Media Inquiries & Requests: 215-662-2560"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".general-list__item:nth-child(1) .general-list__item-title")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".general-list__item:nth-child(1) .general-list__item-thumb")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".general-list-wrap:nth-child(3) .general-list__item:nth-child(2) .general-list__item-title").text == "Brandon Lausch"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".general-list__item:nth-child(2) .general-list__item-thumb")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".general-list__item:nth-child(3) .general-list__item-title").text == "Rachel Ewing"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".general-list__item:nth-child(3) .general-list__item-thumb")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".general-list__item:nth-child(4) .general-list__item-title").text == "Debbie Foster"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".general-list__item:nth-child(4) .general-list__item-thumb")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".portlet__title")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "ctl03_lnkHomepageLink").click()
        self.driver.find_element_by_xpath("//nav[2]/ul/li/a/span").click()
        assert self.driver.title == "Contact Us - Penn Medicine"
