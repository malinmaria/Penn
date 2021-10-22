from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestNewsReleaseDetail():

    def test_newsReleaseDetail(self):
        self.driver.get("https://www.pennmedicine.org/news/news-releases/2020/july/a-proposed-framework-for-integrating-chatbots-and-other-conversational-agents-into-health-care")
        # self.driver.set_window_size(1342, 728)
        element = self.driver.find_element(By.ID, "ctl09_rptMainNav_lnkMainNavItem_3")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        assert self.driver.title == "A Proposed Framework for Integrating Chatbots and Other Conversational Agents into Health Care - Penn Medicine"
        self.driver.find_element(By.ID, "prnewsmaincontent_0_divbanner").click()
        assert self.driver.find_element(By.ID, "prnewsmaincontent_0_divbanner").text == "News Release"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1-main__title").text == "A Proposed Framework for Integrating Chatbots and Other Conversational Agents into Health Care"
        elements = self.driver.find_elements(By.CSS_SELECTOR, "img")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".portlet__title")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".h5").text == "TOPIC:"
        self.driver.find_element(By.ID, "ctl04_rptBreadcrumbs_hypBreadCrumb_1").click()
        assert self.driver.title == "News Releases - Penn Medicine"