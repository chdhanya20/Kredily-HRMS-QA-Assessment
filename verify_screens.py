
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.app_package = "com.kredily.mobile"
options.set_capability("appium:ignoreHiddenApiPolicyError", True)
options.set_capability("appium:noReset", True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    time.sleep(2)
    source = driver.page_source
    driver.save_screenshot("final_dashboard_verification.png")

    with open("final_dashboard_verification.xml", "w", encoding="utf-8") as f:
        f.write(source)

    print("SCREEN VERIFICATION")
    for word in ["home", "dashboard", "attendance", "clocked out", "shift"]:
        if word in source.lower():
            print("Visible keyword:", word)

    print("Screenshot and XML saved.")
finally:
    driver.quit()
