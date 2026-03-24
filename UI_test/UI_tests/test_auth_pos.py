import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.MainPage import MainPage
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authentication_positive(driver):
    page = MainPage(driver)

    page.click_login_button()
    email = os.getenv("login")
    password = os.getenv("password")

    page.authorization_username(email)
    page.authorization_password(password)

    # Проверка перехода на нужную страницу
    WebDriverWait(driver, 30).until(
        EC.url_to_be("https://ru.yougile.com/team/")
    )


assert driver.current_url == "https://ru.yougile.com/team/", (
    f"URL: {driver.current_url} != expected."
)
