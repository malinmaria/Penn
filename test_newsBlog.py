from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestNewsBlog():

    def test_newsBlog(self):
        # self.driver.get("https://www.pennmedicine.org/news/news-blog")
        self.driver.find_element(By.ID, "ctl06_rptMainNav_spnMainNavItem_1").click()
        assert self.driver.title == "News Blog - Penn Medicine"
        assert self.driver.find_element(By.CSS_SELECTOR, ".h1").text == "News Blog"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".img--large")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "#prrightrail_0_artAboutUs .portlet__title").text == "About this Blog"
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage").click()
        dropdown = self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage")
        dropdown.find_element(By.XPATH, "//option[. = '50']").click()
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_ddlNumPerPage").click()
        # assert self.driver.find_element(By.CSS_SELECTOR, "#prnewsmaincontent_0_divPaginationTop .pagination__status").text == "Showing 1-50 of 1379"
        self.driver.find_element(By.LINK_TEXT, "2").click()
        # assert self.driver.find_element(By.CSS_SELECTOR, "#prnewsmaincontent_0_divPaginationTop .pagination__status").text == "Showing 51-100 of 1379"
        self.driver.find_element(By.ID, "prnewsmaincontent_0_pageTop_hypForward").click()
        self.driver.find_element(By.ID, "prrightrail_1_rptTopics_lnkTopic_0").click()
        assert self.driver.find_element(By.ID, "prnewsmaincontent_0_lblSubtitleLabel").text == "Blog Topic: Cancer"
        self.driver.find_element(By.CSS_SELECTOR, ".general-list").click()
        self.driver.find_element(By.ID, "prrightrail_2_ddlMonths").click()
        dropdown = self.driver.find_element(By.ID, "prrightrail_2_ddlMonths")
        dropdown.find_element(By.XPATH, "//option[. = 'Jan']").click()
        self.driver.find_element(By.ID, "prrightrail_2_ddlMonths").click()
        self.driver.find_element(By.ID, "prrightrail_2_ddlYears").click()
        dropdown = self.driver.find_element(By.ID, "prrightrail_2_ddlYears")
        dropdown.find_element(By.XPATH, "//option[. = '2020']").click()
        self.driver.find_element(By.ID, "prrightrail_2_ddlYears").click()
        self.driver.find_element(By.ID, "prrightrail_2_lnkGo").click()
        assert self.driver.find_element(By.ID, "prnewsmaincontent_0_lblSubtitleLabel").text == "Blog Archives: January, 2020"
        self.driver.find_element(By.ID, "prrightrail_3_ddlAuthors").click()
        dropdown = self.driver.find_element(By.ID, "prrightrail_3_ddlAuthors")
        dropdown.find_element(By.XPATH, "//option[. = 'John Lines']").click()
        self.driver.find_element(By.ID, "prrightrail_3_ddlAuthors").click()
        self.driver.find_element(By.ID, "prrightrail_3_lnkGo").click()
        assert self.driver.find_element(By.ID, "prnewsmaincontent_0_lblSubtitleLabel").text == "Blog Author: John Lines"
        self.driver.find_element(By.ID, "ddlTopics").click()
        dropdown = self.driver.find_element(By.ID, "ddlTopics")
        dropdown.find_element(By.XPATH, "//option[. = 'Cancer']").click()
        self.driver.find_element(By.ID, "ddlTopics").click()
        self.driver.find_element(By.LINK_TEXT, "Apply Filter").click()
        self.driver.find_element(By.ID, "ddlTopics").click()
        dropdown = self.driver.find_element(By.ID, "ddlTopics")
        dropdown.find_element(By.XPATH, "//option[. = 'Cardiology']").click()
        self.driver.find_element(By.ID, "ddlTopics").click()
        self.driver.find_element(By.LINK_TEXT, "Apply Filter").click()
        assert self.driver.find_element(By.ID, "prnewsmaincontent_0_lblSubtitleLabel").text == "Blog Topic: Cardiology"
