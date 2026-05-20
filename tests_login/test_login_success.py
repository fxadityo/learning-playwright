from playwright.sync_api import sync_playwright, expect

def test_login_success():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Set default timeout (optional, global)
        page.set_default_timeout(7000)

        # Navigate ke login page dengan timeout 30 detik
        page.goto(
            "https://practice.expandtesting.com/login",
            timeout=10000,
            wait_until="domcontentloaded"
        )

        # Verify login page displayed
        expect(page).to_have_url("https://practice.expandtesting.com/login")
        expect(page.get_by_role("heading", name="Test Login page")).to_be_visible()

        # Input username & password
        page.get_by_label("Username").fill("practice")
        page.get_by_label("Password").fill("SuperSecretPassword!")

        # Klik login
        page.get_by_role("button", name="Login").click()

        # Verify redirect
        expect(page).to_have_url("https://practice.expandtesting.com/secure")

        # Verify success message
        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

        # Verify logout button
        logout_button = page.get_by_role("link", name="Logout")
        expect(logout_button).to_be_visible()

        # Klik logout
        logout_button.click()

        # Verify redirect ke login page
        expect(page).to_have_url("https://practice.expandtesting.com/login")

        # Verify logout message
        expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

        # Optional delay biar kelihatan
        page.wait_for_timeout(7000)

        browser.close()