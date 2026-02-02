from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    result_value = (By.ID, "resultValue")

    def get_result(self):
        return self.driver.find_element(*self.result_value).text
