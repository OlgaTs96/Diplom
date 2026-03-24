import pytest
from selenium import webdriver
from pages.MainPage import MainPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authentication_negative(driver):
    page = MainPage(driver)

    page.click_login_button()

    invalid_email = "incorrect_email@example.com"
    invalid_password = "wrongpassword"

    page.authorization_username(invalid_email)
    page.authorization_password(invalid_password)

    current_url = driver.current_url
    expected_url = "https://ru.yougile.com/team/"

    assert current_url != expected_url, (
        f"URL после неправильной авторизации: {current_url}, "
        "не должно было произойти перенаправление на /team/"
    )
