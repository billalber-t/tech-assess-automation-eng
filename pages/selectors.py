from selenium.webdriver.common.by import By

class HomePageSelectors:
    SEARCH_BAR = (By.ID, "search")
    SVG_POP_UP = (By.XPATH,  "//svg[@class='ic']")
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    CART_BUTTON = (By.CLASS_NAME, "cart-btn")

class LoginPageSelectors:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
