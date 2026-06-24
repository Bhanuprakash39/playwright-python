import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("file:///C:/Users/bbhan/Downloads/hrms-20260622T165744Z-3-001/hrms/index.html")

    #login with respected credentials
    page.get_by_role("textbox").first.fill("admin")
    page.get_by_role("textbox").last.fill("admin123")
    page.get_by_role("button").click()

    #validation
    expect(page.get_by_text(" Payroll for June has been processed successfully.")).to_be_visible()

    #page actions
    page.get_by_role("link",name="Employees").click()
    page.get_by_role("link",name="+ Add Employee").click()
    page.get_by_role("textbox").nth(0).fill("Bhanuprakash")
    page.get_by_role("textbox").nth(1).fill("bbhanuprakash0101@gmail.com")
    page.get_by_role("textbox").nth(2).fill("9102920393")
    page.locator("#field-dob").fill("1996-05-30")
    page.get_by_role("textbox",name="Emergency contact").fill("9183744672")
    page.get_by_role("textbox").nth(5).fill("010290")
    page.get_by_role("radio").first.check()
    page.get_by_label("Department ").select_option("design")
    page.get_by_role("textbox",name="Designation").fill("Senior Engineer")
    page.get_by_label("Employment type").select_option("Contract")
    page.get_by_role("textbox",name="Date of joining").fill("2026-06-23")
    page.get_by_label("Reporting manager").select_option("Vikram Nair")

    print("Task Completed Successfully")

    #close the browser
    browser.close()