
import pytest

from playwright.sync_api import Page, expect

def login_data():
    yield "invaliduser@example.com","test123", "invalid"
    yield "invalidxyz@example.com", "test546", "invalid"
    yield "laura.taylor1234@example.com", "test123", "valid"
    yield " ", " ", "invalid"

@pytest.mark.parametrize("email,password,validation",login_data())
def test_login_validation(email,password,validation,page: Page):
    #log in into page
    page.goto("https://demowebshop.tricentis.com/login")
    page.get_by_role("textbox",name="Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator("//input[contains(@class,'login-button')]").click()

    #validation
    if validation == "valid":
        logout_button=page.locator("//li/a[text()='Log out']")
        expect(logout_button).to_be_visible(timeout=3000)

    else:
        page.get_by_text("Login was unsuccessful. Please correct the errors and try again.").is_visible()
