from pathlib import Path

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
    my_browser.element("#subjectsInput").click().type("M")
    my_browser.all(".subjects-auto-complete__option").element_by(
        have.text("Math")
    ).click()
    browser.element("#uploadPicture").send_keys(
        str(Path("picture.jpg").resolve())
    )
    my_browser.element("#currentAddress").type("My address")
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
    browser.all(".table-responsive tbody tr td:nth-child(2)").should(
        have.exact_texts(
            "Test Test",
            "test@buba.com",
            "Male",
            "1112223334",
            "10 June,1990",
            "Maths",
            "Sports",
            "picture.jpg",
            "My address",
            "NCR Delhi",
        )
    )

    # Close form with result
    my_browser.element("#closeLargeModal").click()
    my_browser.element("h1.text-center").should(have.text("Practice Form"))
