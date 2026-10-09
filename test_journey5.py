
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
    print("JOURNEY 5: ATTENDANCE TO PREVIOUS SCREEN")

    before = driver.page_source
    driver.save_screenshot("journey5_before.png")
    print("Starting screen captured")

    # Navigate back using Android's back action
    driver.back()
    time.sleep(3)

    after = driver.page_source
    driver.save_screenshot("journey5_after.png")

    with open("journey5_before.xml", "w", encoding="utf-8") as f:
        f.write(before)

    with open("journey5_after.xml", "w", encoding="utf-8") as f:
        f.write(after)

    if before != after:
        print("RESULT: Screen hierarchy changed after Back.")
        print("Inspect screenshots to confirm the destination.")
    else:
        print("RESULT: Screen hierarchy did not change.")

    print("Evidence saved: journey5_before.png, journey5_after.png")
    print("Evidence saved: journey5_before.xml, journey5_after.xml")

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))

finally:
    driver.quit()
