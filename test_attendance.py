
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
    print("JOURNEY 4: ATTENDANCE VALIDATION STARTED")

    # Capture the dashboard before interacting
    driver.save_screenshot("journey4_before.png")
    print("Dashboard screenshot saved")

    print("Tap Attendance on the phone.")
    input("After Attendance screen opens, press Enter here...")

    time.sleep(2)
    driver.save_screenshot("journey4_attendance.png")

    with open("journey4_attendance.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Attendance screen evidence saved")
    print("RESULT: Attendance screen captured for review")

    input("Press Enter to finish Journey 4...")

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))

finally:
    driver.quit()
