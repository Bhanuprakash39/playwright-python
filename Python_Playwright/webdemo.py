import pytest

from playwright.sync_api import Page, expect


search_items=["laptop", "gift card", "smartphone", "monitor"]

@pytest.mark.parametrize("search_item", search_items)
def test_login(search_item,page: Page):
    #navigate to the page


    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(search_item)
    page.locator("//input[@value='Search']").click()

    first_results=page.locator("h2 a").nth(0)
    #assert
    expect(first_results).to_contain_text(search_item,ignore_case=True)
    page.close()


