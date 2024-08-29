import pytest
from pages.home_page import HomePage
from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHomePage(BaseTest):
    def test_open_homepage(self):
        home_page = HomePage(self.driver)
        home_page.open_homepage()
        assert "Jumia" in self.driver.title

    def test_search_for_item(self):
        home_page = HomePage(self.driver)
        home_page.open_homepage()
        home_page.search_for_item("ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")