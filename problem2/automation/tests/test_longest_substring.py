from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.result_page import ResultPage
from config.config import BASE_URL

def test_longest_unique_substring():
    driver = get_driver()
    driver.get(BASE_URL)

    home = HomePage(driver)
    home.enter_input("abcabcbb")
    home.click_submit()

    result = ResultPage(driver)
    assert result.get_result() == "3"

    driver.quit()
