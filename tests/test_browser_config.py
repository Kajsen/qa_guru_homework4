from selene import browser, have, be
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="function")
def my_browser():
    options = Options()
    options.add_argument("--headless=new")
    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://demoqa.com"
    yield browser


def test_fill_form(my_browser):
    # Fill the form
    my_browser.open("/automation-practice-form")
    my_browser.element("h1.text-center").should(have.text("Practice Form"))
    my_browser.element("#firstName").type("Test")
    my_browser.element("#lastName").type("Test")
    my_browser.element("#userEmail").type("test@buba.com")
    my_browser.element('label[for="gender-radio-1"]').click()
    my_browser.element("#userNumber").type("1112223334")

    my_browser.element("#dateOfBirthInput").click()
    my_browser.element(".react-datepicker__month-select").click()
    (
        my_browser.element(
            '.react-datepicker__month-select option[value="5"]'
        ).click()
    )
    my_browser.element(".react-datepicker__year-select").click()
    (
        my_browser.element(
            '.react-datepicker__year-select option[value="1990"]'
        ).click()
    )
    my_browser.element(
        ".react-datepicker__day--010:not(.react-datepicker__day--outside-month)"
    ).click()
    my_browser.element("#dateOfBirthInput").should(have.value("10 Jun 1990"))

    my_browser.element('label[for="hobbies-checkbox-1"]').click()
    my_browser.element("#state").should(be.clickable).click()
    my_browser.element("#react-select-3-option-0").click()
    my_browser.element("#city").click()
    my_browser.element("#react-select-4-option-0").click()
    my_browser.element("#submit").click()

    # Check result
    my_browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )
    my_browser.element('//tr[td[text()="Student Name"]]/td[2]').should(
        have.text("Test Test")
    )
    my_browser.element('//tr[td[text()="Student Email"]]/td[2]').should(
        have.text("test@buba.com")
    )
    (
        my_browser.element('//tr[td[text()="Gender"]]/td[2]').should(
            have.text("Male")
        )
    )
    my_browser.element('//tr[td[text()="Mobile"]]/td[2]').should(
        have.text("1112223334")
    )
    (
        my_browser.element('//tr[td[text()="Date of Birth"]]/td[2]').should(
            have.text("10 June,1990")
        )
    )
    my_browser.element('//tr[td[text()="Hobbies"]]/td[2]').should(
        have.text("Sports")
    )
    my_browser.element('//tr[td[text()="State and City"]]/td[2]').should(
        have.text("NCR Delhi")
    )

    # Close form with result
    my_browser.element("#closeLargeModal").click()
    my_browser.element("h1.text-center").should(have.text("Practice Form"))
