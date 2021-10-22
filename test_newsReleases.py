from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestNewsReleases():
  
    def test_newsReleases(self):
        # self.driver.get("https://www.pennmedicine.org/news")
        # self.driver.set_window_size(1342, 728)
        self.driver.find_element(By.ID, "ctl06_rptMainNav_spnMainNavItem_0").click()
        assert self.driver.title == "News Releases - Penn Medicine"
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage").click()
        dropdown = self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage")
        dropdown.find_element(By.XPATH, "//option[. = '50']").click()
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage").click()
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_hypForward").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".portlet__title")
        assert len(elements) > 0