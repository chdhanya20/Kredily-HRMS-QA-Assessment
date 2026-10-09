
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.app_package = "com.kredily.mobile"
options.set_capability("appium:ignoreHiddenApiPolicyError", True)
options.set_capability("appium:noReset", True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

try:
    print("JOURNEY 3: DASHBOARD VALIDATION STARTED")

    # Enter the registered email
    email = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//*[contains(@hint, "you@company.com")]')
    ))
    email.click()
    email.clear()
    email.send_keys("peoplekredily1@yopmail.com")
    print("Registered email entered")

    # Scroll to the password login option
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 300, "width": 880, "height": 700,
        "direction": "up", "percent": 0.5
    })

    option = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//*[contains(@text, "Sign in with password")]/..')
    ))
    rect = option.rect
    driver.execute_script("mobile: clickGesture", {
        "x": rect["x"] + rect["width"] // 2,
        "y": rect["y"] + rect["height"] // 2
    })

    # Enter password
    time.sleep(2)
    password = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//*[@class="android.widget.EditText"]')
    ))
    password.click()
    password.send_keys("Pass@9865")
    driver.hide_keyboard()
    print("Password entered")

    # Tap Sign in
    sign_in = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//*[contains(@text, "Sign in")]')
    ))
    rect = sign_in.rect
    driver.execute_script("mobile: clickGesture", {
        "x": rect["x"] + rect["width"] // 2,
        "y": rect["y"] + rect["height"] // 2
    })

    time.sleep(6)

    # Save evidence and verify screen
    source = driver.page_source
    driver.save_screenshot("journey3_dashboard.png")

    with open("journey3_dashboard.xml", "w", encoding="utf-8") as f:
        f.write(source)

    if any(word in source.lower() for word in ["dashboard", "attendance", "clocked", "home"]):
        print("RESULT: Dashboard-related content detected. Inspect screenshot to confirm.")
    else:
        print("RESULT: Dashboard not confirmed. Inspect screenshot/XML.")

    print("Screenshot: journey3_dashboard.png")
    print("XML: journey3_dashboard.xml")
    input("Press Enter to finish Journey 3...")

except Exception as e:
    print("JOURNEY 3 ERROR:", type(e).__name__, str(e))
    driver.save_screenshot("journey3_error.png")
    with open("journey3_error.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    input("Evidence saved. Press Enter to close...")

finally:
    driver.quit()
