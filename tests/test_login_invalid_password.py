from playwright.sync_api import sync_playwright, expect

def test_login_invalid_username():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Set default timeout (optional, global)
        page.set_default_timeout(5000)

        # Navigate to login page
        page.goto(
            "https://practice.expandtesting.com/login",
            timeout=10000,
            wait_until="domcontentloaded"
        )

        # Verify login page displayed
        expect(page).to_have_url("https://practice.expandtesting.com/login")
        expect(page.get_by_role("heading", name="Test Login page")).to_be_visible()

        # Input valid username
        page.get_by_label("Username").fill("practice")

        # Input incorrect password
        page.get_by_label("Password").fill("WrongPassword!")
        
        # Click login
        page.get_by_role("button", name="Login").click()

        # Verify error message
        expect(page.locator("#flash")).to_contain_text("invalid")

        # Verify tetap di halaman login
        expect(page).to_have_url("https://practice.expandtesting.com/login")

        # Optional delay (debug)
        page.wait_for_timeout(5000)

        browser.close()
