from base.base_page import BasePage
from pages.selectors import HomePageSelectors
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.jumia.co.ke/"

    def open_homepage(self):
        self.navigate_to_page()
        assert "Jumia" in self.driver.title

    def navigate_to_page(self):
        self.navigate_to(self.url)

    def close_pop_up(self):
        time.sleep(5)
        self.click_element(*HomePageSelectors.SVG_POP_UP_CLOSE)

    def search_for_item(self, item_name):
        self.navigate_to_page()
        self.close_pop_up()
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys(item_name)
        self.click_element(*HomePageSelectors.SEARCH_BTN)

        time.sleep(4)
        element_text = self.find_element(*HomePageSelectors.CARD_TEXT_ELECT_DRY_IRON).text
        assert "Dry Iron" in element_text
        time.sleep(4)


    def login(self):
        self.navigate_to_page()
        self.close_pop_up()

        self.click_element(*HomePageSelectors.ACCOUNT_BUTTON)
        time.sleep(2)

        self.click_element(*HomePageSelectors.SIGN_IN_BUTTON)

        time.sleep(5)
        self.driver.find_element(By.ID, "input_identifierValue").send_keys("assessbill5@gmail.com")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']//span[@class='mdc-button__touch']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Albertbill100%")
        time.sleep(3)




    # Add to cart
    def add_to_cart(self):
        self.navigate_to_page()
        self.close_pop_up()
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys("ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")
        self.click_element(*HomePageSelectors.SEARCH_BTN)
        self.click_element(*HomePageSelectors.CARD_IMAGE)
        time.sleep(5)
        self.click_element(*HomePageSelectors.CART_ADD_BTN)

        time.sleep(5)
        notification_text = self.find_element(*HomePageSelectors.NOTIFICATION_BAR).text
        assert "successfully" in notification_text

    def navigate_to_cart(self):
        # Handles browser load and initial navigation
        self.navigate_to_page()
        self.close_pop_up()

        # Add element to cart
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys(
            "ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")
        self.click_element(*HomePageSelectors.SEARCH_BTN)
        self.click_element(*HomePageSelectors.CARD_IMAGE)
        time.sleep(5)
        self.click_element(*HomePageSelectors.CART_ADD_BTN)
        time.sleep(5)

        # Navigate to cart
        self.click_element(*HomePageSelectors.CART_MENU)

        # Assert if element is in cart
        element_text = self.find_element(*HomePageSelectors.CARD_TEXT_ELECT_DRY_IRON).text
        assert "Dry Iron" in element_text




