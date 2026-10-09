from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.app_package = "com.kredily.mobile"

options.set_capability("appium:ignoreHiddenApiPolicyError", True)
options.set_capability("appium:noReset", True)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

wait = WebDriverWait(driver, 15)

print("Kredily Appium session started successfully!")


# -------------------------------------------------
# STEP 1: Find Email / Mobile field
# -------------------------------------------------

email_field = wait.until(
    EC.presence_of_element_located(
        (
            AppiumBy.XPATH,
            '//*[contains(@hint, "you@company.com")]'
        )
    )
)

print("Email/Mobile field found successfully!")

email_field.click()
email_field.send_keys("peoplekredily1@yopmail.com")

print("Email entered successfully!")


# -------------------------------------------------
# STEP 2: Scroll to "Sign in with password"
# -------------------------------------------------

driver.execute_script(
    "mobile: scrollGesture",
    {
        "left": 100,
        "top": 300,
        "width": 880,
        "height": 700,
        "direction": "up",
        "percent": 0.5
    }
)

print("Login screen scrolled up!")


# -------------------------------------------------
# STEP 3: Click "Sign in with password"
# -------------------------------------------------

password_login = wait.until(
    EC.presence_of_element_located(
        (
            AppiumBy.XPATH,
            '//*[contains(@text, "Sign in with password")]/..'
        )
    )
)

print("Password option found!")

password_login.click()

print("Sign in with password clicked!")


# -------------------------------------------------
# STEP 4: Find password field
# -------------------------------------------------

password_field = wait.until(
    EC.presence_of_element_located(
        (
            AppiumBy.XPATH,
            '//*[@class="android.widget.EditText"]'
        )
    )
)

print("Password field found successfully!")


# -------------------------------------------------
# STEP 5: Enter password
# -------------------------------------------------

password_field.click()
password_field.send_keys("Pass@9865")

print("Password entered successfully!")


# -------------------------------------------------
# STEP 6: Find Sign in button
# -------------------------------------------------

sign_in_button = wait.until(
    EC.presence_of_element_located(
        (
            AppiumBy.XPATH,
            '//*[contains(@text, "Sign in")]/..'
        )
    )
)

print("Sign in button found successfully!")

driver.hide_keyboard()

print("Keyboard hidden!")

rect = sign_in_button.rect

x = rect["x"] + rect["width"] // 2
y = rect["y"] + rect["height"] // 2

print("Sign in button bounds:", rect)
print("Tapping Sign in at:", x, y)

driver.execute_script(
    "mobile: clickGesture",
    {
        "x": x,
        "y": y
    }
)

print("Sign in button tapped!")


# -------------------------------------------------
# STEP 8: Wait for Home/Dashboard
# -------------------------------------------------
import time

time.sleep(5)

with open("after_signin.xml", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

print("Screen after Sign in saved!")

print("Current activity:", driver.current_activity)


# -------------------------------------------------
# Keep app open
# -------------------------------------------------

input("Press Enter to close the app...")
driver.quit()