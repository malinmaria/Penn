import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestHomepage():
  
    def test_homepage(self):
        # self.driver.get("https://www.pennmedicine.org/news")
        # self.driver.set_window_size(1342, 728)
        assert self.driver.title == "Penn Medicine News & Publications | University of Pennsylvania Health System"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".magic-box-input > input")
        assert len(elements) > 0
        assert self.driver.title == "Penn Medicine News & Publications | University of Pennsylvania Health System"
        self.driver.find_element(By.CSS_SELECTOR, "#prnewsmaincontent_0_rptLatesNewsLeft_lnkNewsItem_0 > p").click()
        self.driver.find_element(By.ID, "ctl03_lnkHomepageLink").click()
        self.driver.find_element(By.CSS_SELECTOR, "#prnewsmaincontent_0_rptLatesNewsLeft_lnkNewsItem_1 > p").click()
        self.driver.find_element(By.ID, "ctl03_lnkHomepageLink").click()
        assert self.driver.title == "Penn Medicine News & Publications | University of Pennsylvania Health System"
        assert self.driver.find_element(By.CSS_SELECTOR, ".mb-half-mq-small").text == "On the News Blog"
        self.driver.find_element(By.ID, "prnewsmaincontent_0_rptLatestBlogs_spnBlogTitle_0").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1").text == "News Blog"
        self.driver.find_element(By.ID, "ctl03_lnkHomepageLink").click()
        self.driver.find_element(By.CSS_SELECTOR, ".story-slider__next").click()
        self.driver.find_element(By.CSS_SELECTOR, ".story-slider__next").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".news-list-external > .mb-2").text == "Penn Medicine In the News"
        self.driver.find_element(By.ID, "ctl09_ctl00_rptUtilNav_spnUtilityNavItem_0").click()
        assert self.driver.title == "Contact Us - Penn Medicine"
