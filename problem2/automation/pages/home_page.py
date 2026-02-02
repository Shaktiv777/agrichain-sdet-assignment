from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    input_box = (By.ID, "inputString")
    submit_button = (By.ID, "submitBtn")

    def enter_input(self, text):
        self.driver.find_element(*self.input_box).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
