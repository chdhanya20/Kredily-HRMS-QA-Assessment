
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
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
    print("JOURNEY 2: INVALID LOGIN STARTED")

    # 1. Enter email
    email = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//*[contains(@hint, "you@company.com")]'
    )))
    email.click()
    email.send_keys("invalid_user_123@example.com")
    print("Email entered")

    # 2. Scroll to password-login option
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 300, "width": 880, "height": 700,
        "direction": "up", "percent": 0.5
    })

    # 3. Open password login
    option = wait.until(EC.presence_of_element_located((
        AppiumBy.XPATH,
        '//*[contains(@text, "Sign in with password")]/..'
    )))
    rect = option.rect
    driver.execute_script("mobile: clickGesture", {
        "x": rect["x"] + rect["width"] // 2,
        "y": rect["y"] + rect["height"] // 2
    })
    print("Password login selected")
    time.sleep(2)

    # 4. Locate password field and retry if UI refreshes
    password = None
    for attempt in range(3):
        try:
            password = wait.until(EC.presence_of_element_located((
                AppiumBy.XPATH, '//*[@class="android.widget.EditText"]'
            )))
            password.click()
            password.send_keys("WrongPassword123!")
            print("Invalid password entered")
            break
        except StaleElementReferenceException:
            time.sleep(1)

    if password is None:
        raise TimeoutException("Password field could not be located")

    # 5. Hide keyboard before finding Sign in
    try:
        driver.hide_keyboard()
    except Exception:
        pass

    time.sleep(1)

    # 6. Find Sign in text and tap its center
    sign_in = wait.until(EC.presence_of_element_located((
        AppiumBy.XPATH, '//*[contains(@text, "Sign in")]'
    )))
    rect = sign_in.rect
    driver.execute_script("mobile: clickGesture", {
        "x": rect["x"] + rect["width"] // 2,
        "y": rect["y"] + rect["height"] // 2
    })
    print("Sign in tapped")

    # 7. Capture the actual result
    time.sleep(5)
    driver.save_screenshot("journey2_invalid_login.png")

    with open("journey2_result.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Screenshot saved: journey2_invalid_login.png")
    print("Screen source saved: journey2_result.xml")
    print("Inspect the phone to confirm login was rejected.")

    input("Press Enter to finish Journey 2...")

except Exception as e:
    print("Journey 2 encountered an error:", type(e).__name__, str(e))
    driver.save_screenshot("journey2_error.png")
    with open("journey2_error.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    input("Error evidence saved. Press Enter to close...")

finally:
    driver.quit()
