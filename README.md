# learning-playwright
# 🎯 Learning Playwright Automation

## 📌 Description

Project ini dibuat sebagai bagian dari pembelajaran Automation Testing menggunakan Playwright dengan Python.

Test case yang dibuat fokus pada:

* Fungsional Login
* Positive & Negative testing

Website yang digunakan:
https://practice.expandtesting.com/login

---

## 🧪 Test Case

### ✅ Test Case 1 - Successful Login

* Launch the browser.
* Navigate to the login page URL.
* Verify that the login page is displayed successfully.
* Enter Username: practice.
* Enter Password: SuperSecretPassword!.
* Click the Login button.
* Verify that the user is redirected to the /secure page.
* Confirm the success message "You logged into a secure area!" is visible.
* Verify that a Logout button is displayed.

---

### ❌ Test Case 2 - Invalid Username

* Launch the browser.
* Navigate to the login page URL.
* Verify that the login page is displayed successfully.
* Enter an incorrect Username (e.g., wrongUser).
* Enter Password: SuperSecretPassword!.
* Click the Login button.
* Verify that an error message "Invalid username." is displayed.
* Ensure the user remains on the login page.

### ❌ Test Case 3 - Invalid Password

* Launch the browser.
* Navigate to the login page URL.
* Verify that the login page is displayed successfully.
* Enter Username: practice.
* Enter an incorrect Password (e.g., WrongPassword).
* Click the Login button.
* Verify that an error message "Invalid password." is displayed.
* Ensure the user remains on the login page.

---

## 🛠️ Tech Stack

* VSCode
* Python
* Playwright
* Pytest

---

## ⚙️ Setup Project

1. Clone repository:
   git clone https://github.com/fxadityo/learning-playwright.git

2. Masuk folder:
   cd learning-playwright

3. Buat virtual environment:
   python -m venv venv

4. Aktifkan venv:
   venv\Scripts\activate

5. Install dependencies:
   pip install pytest playwright

6. Install browser:
   python -m playwright install

---

## ▶️ Run Automation Test

Jalankan semua test:
pytest

Jalankan 1 file:
pytest tests_login/test_login_success.py

---

## 📂 Project Structure

tests_login/
├── test_login_success.py
├── test_login_invalid_username.py
├── test_login_invalid_password.py

---

## 🚀 Goal

Project ini dibuat untuk:

* Belajar automation testing
* Improve skill sebagai QA Tester/Engineer
* Menjadi portfolio automation testing

---

## 👤 Author

Adityo Nugroho

