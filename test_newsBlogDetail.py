from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestNewsBlogDetail():

    def test_newsBlogDetail(self):
        self.driver.get("https://www.pennmedicine.org/news/news-blog/2020/july/during-covid19-cancer-surgeons-find-bridges-to-care-for-patients")
        # self.driver.set_window_size(1342, 728)
        assert self.driver.title == "During COVID-19, Cancer Surgeons Find “Bridges” to Care for Patients - Penn Medicine"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1").text == "News Blog"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1-main__title").text == "During COVID-19, Cancer Surgeons Find “Bridges” to Care for Patients"
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div > img")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".h5").text == "TOPICS:"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h3").text == "You Might Also Be Interested In..."
        self.driver.find_element(By.CSS_SELECTOR, ".story-slider__next").click()
        self.driver.find_element(By.CSS_SELECTOR, ".story-slider__next").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#prrightrail_0_artAboutUs .portlet__title").text == "About this Blog"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".portlet--tag-links .portlet__title")
        assert len(elements) > 0
