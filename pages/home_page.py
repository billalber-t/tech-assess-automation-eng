from base.base_page import BasePage
from pages.selectors import HomePageSelectors
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.jumia.co.ke/"

    def open_homepage(self):
        self.navigate_to(self.url)
    def close_pop_up(self):
        self.search_for_item(*HomePageSelectors.SVG_POP_UP)
    def search_for_item(self, item_name):
        time.sleep(10)
        element = self.driver.find_element(By.XPATH, "//button[@class='cls']")
        element.click()

        # self.click_element(*HomePageSelectors.SVG_POP_UP)
        time.sleep(5)
        self.driver.find_element(By.ID, "fi-q").send_keys(item_name)
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        time.sleep(4)

        self.driver.find_element(By.XPATH, "(//div[@class='dpdw _pcent'])[1]").click()

        time.sleep(4)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")

        time.sleep(4)
        self.driver.find_element(By.ID, "input_identifierValue").send_keys("assessbill5@gmail.com")

        time.sleep(4)
        self.driver.find_element(By.ID, "//button[@type='submit']").click()

        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Albertbill100%")
        # self.find_element(*HomePageSelectors.SEARCH_BAR).send_keys(item_name)

        # self.click_element(*HomePageSelectors.LOGIN_BUTTON)
        # self.click_element(*HomePageSelectors.SVG_POP_UP)


    # Example method to click on a category
    def click_category(self, category_name):
        self.click_element("link text", category_name)
